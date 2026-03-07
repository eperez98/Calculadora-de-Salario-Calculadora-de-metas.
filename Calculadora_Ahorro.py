# ============================================================
#  SALARY & GOALS CALCULATOR / CALCULADORA DE SALARIO & METAS
#  by Erick Perez  |  v0.2 BETA
#  Requires / Requiere: pip install reportlab
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import date
import os, sys, math, json

# ══════════════════════════════════════════════════════════
#  APP STATE — globals
# ══════════════════════════════════════════════════════════
_LANG      = "es"
_DARK_MODE = False
_APP_REF   = None   # reference to CalcApp set after creation

SESSIONS_FILE = os.path.join(os.path.expanduser("~"), ".salary_calc_sessions.json")

def set_lang(lang):
    global _LANG
    _LANG = lang

def toggle_dark():
    global _DARK_MODE
    _DARK_MODE = not _DARK_MODE
    _rebuild_theme()
    if _APP_REF:
        _APP_REF._apply_theme_to_chrome()
        _APP_REF._change_lang(_LANG)  # refresh all content

# ══════════════════════════════════════════════════════════
#  TRANSLATIONS
# ══════════════════════════════════════════════════════════

LANGS = {
    "es": {
        "app_title":        "Calculadora de Salario & Metas  —  by Erick Perez",
        "title_bar":        "  💰  Calculadora de Salario & Metas  —  by Erick Perez",
        "splash_sub":       "Calculadora de Salario & Metas",
        "splash_edition":   "v0.2 BETA  •  Panamá & Colombia",
        "splash_loading":   ["Iniciando...", "Cargando interfaz...",
                             "Configurando impuestos...",
                             "Preparando calculadora...", "¡Listo!"],
        "back":             "← Atrás",
        "next":             "Siguiente →",
        "new_query":        "🔄  Nueva Consulta",
        "step_of":          "Paso {s} de {t}",
        "steps":            ["Perfil","Meta","Ingresos","Hogar","Deudas","Ocio","Extras","Resultado"],
        "dark_mode":        "🌙 Oscuro",
        "light_mode":       "☀️ Claro",
        "save_session":     "💾 Guardar",
        "load_session":     "📂 Cargar",
        "sessions_title":   "Sesiones Guardadas",
        "save_name_prompt": "Nombre para esta sesión:",
        "save_success":     "Sesión guardada como «{name}»",
        "save_error":       "No se pudo guardar la sesión.",
        "load_select":      "Selecciona una sesión para cargar:",
        "load_none":        "No hay sesiones guardadas.",
        "load_success":     "Sesión «{name}» cargada.",
        "delete_session":   "Eliminar",
        "cancel":           "Cancelar",
        "ok":               "OK",
        "req_name":         "Por favor ingresa tu nombre.",
        "req_field":        "Campo requerido",
        "req_meta":         "Ingresa una meta de ahorro válida.",
        "req_anio":         "Ingresa un año válido (ej: 2026).",
        "invalid_year":     "Año inválido",
        "req_salary":       "Ingresa tu salario mensual bruto.",
        "p0_title":         "👤  Tu Perfil",
        "p0_sub":           "Cuéntanos quién eres para personalizar tu reporte.",
        "p0_section":       "Información Personal",
        "p0_name":          "Tu nombre completo *",
        "p0_country":       "País de residencia *",
        "p0_note":          "⚠️  VERSIÓN BETA EN DESARROLLO — Disponible para Panamá 🇵🇦 y Colombia 🇨🇴. Próximamente más países. Los cálculos son estimados.",
        "p1_title":         "🎯  Meta de Ahorro",
        "p1_sub":           "Define cuánto quieres ahorrar y para cuándo.",
        "p1_section":       "Tu Objetivo Financiero",
        "p1_meta":          "Meta de ahorro *",
        "p1_month":         "Mes objetivo *",
        "p1_year":          "Año objetivo *",
        "p1_tip":           "💡  Un ahorro mensual constante, aunque sea pequeño, tiene un gran impacto a largo plazo. Sé realista con tu meta y celebra cada mes que la cumples.",
        "p2_title":         "💵  Ingresos  —  {nombre}",
        "p2_sub":           "País: {pais}  |  Deducciones calculadas automáticamente.",
        "p2_section":       "Salario Mensual",
        "p2_gross":         "Salario mensual BRUTO *",
        "p2_extra":         "Ingresos extra este mes",
        "p2_imp_hint":      "🧮  Ingresa tu salario bruto para ver el desglose",
        "p2_imp_title":     "🧮  Desglose estimado de deducciones — {pais}",
        "p2_net_est":       "  Salario Neto Estimado:",
        "p2_note":          "⚠️  El cálculo de impuestos es un estimado. El monto real puede variar. Siempre consulta tu slip de pago oficial.",
        "p2_real":          "Salario REAL recibido según tu slip de pago (si difiere del estimado)",
        "p2_real_tip":      "💡  Si dejas vacío,\nse usa el neto estimado.",
        "p3_title":         "🏠  Gastos del Hogar",
        "p3_sub":           "Servicios básicos y vivienda.",
        "p3_section":       "Gastos Fijos Mensuales",
        "p3_rent":          "Alquiler / Hipoteca",
        "p3_internet":      "Internet",
        "p3_electric":      "Luz / Electricidad",
        "p3_water":         "Agua",
        "p3_mobile":        "Data Móvil / Celular",
        "p4_title":         "🏦  Deudas, Auto y Mascotas",
        "p4_sub":           "Préstamos, gastos de vehículo y cuidado de mascotas.",
        "p4_s1":            "Préstamos y Deudas",
        "p4_loan_p":        "Préstamo Personal",
        "p4_loan_a":        "Préstamo de Auto",
        "p4_debts":         "Otras Deudas",
        "p4_s2":            "Gastos de Auto",
        "p4_gas":           "Gasolina",
        "p4_maint":         "Mantenimiento",
        "p4_s3":            "Gastos de Mascotas",
        "p4_pet_food":      "Comida mascotas",
        "p4_pet_vet":       "Veterinario",
        "p4_pet_other":     "Otros mascotas",
        "p5_title":         "🎬  Ocio y Suscripciones",
        "p5_sub":           "Entretenimiento, comida y plataformas digitales.",
        "p5_s1":            "Gastos Variables",
        "p5_grocery":       "Supermercado / Comida",
        "p5_out":           "Salidas / Entretenimiento",
        "p5_delivery":      "Delivery",
        "p5_s2":            "Suscripciones Digitales",
        "p6_title":         "➕  Gastos Extra",
        "p6_sub":           "Cualquier gasto adicional que no encaje en las categorías anteriores.",
        "p6_section":       "Gastos Adicionales",
        "p6_extra":         "Gasto Extra {n}",
        "p6_desc":          "Descripción",
        "p6_hint":          "✔  Al presionar 'Siguiente' se calcularán todos tus resultados.",
        "p7_title":         "📊  Resultados  —  {nombre}",
        "p7_sub":           "{pais}  •  Meta: {sym}{meta:,.0f} para {mes} {anio}",
        "p7_deficit":       "⚠  Déficit de {sym}{amt:,.0f}/mes  —  Tus gastos superan tus ingresos",
        "p7_ontrack":       "🎉  Ahorro de {sym}{amt:,.0f}/mes  —  ¡Alcanzarás tu meta!",
        "p7_need":          "💡  Ahorro de {sym}{amt:,.0f}/mes  —  Necesitas {sym}{falta:,.0f} más/mes",
        "p7_salary_imp":    "🧾  Salario e Impuestos",
        "p7_total_ded":     "Total deducciones (estimado)",
        "p7_net_est":       "Salario Neto (estimado)",
        "p7_net_real":      "Salario Real (slip)",
        "p7_imp_note":      "⚠️  Estimado. Puede variar. Verifica con tu slip de pago.",
        "p7_income":        "💵  Ingresos",
        "p7_net_base":      "Salario Neto (base)",
        "p7_extra_inc":     "Ingreso Extra",
        "p7_total_inc":     "TOTAL INGRESOS",
        "p7_home":          "🏠  Hogar",
        "p7_rent":          "Alquiler",
        "p7_electric":      "Luz",
        "p7_water":         "Agua",
        "p7_mobile":        "Data Móvil",
        "p7_loans":         "🏦  Préstamos",
        "p7_loan_p":        "Préstamo personal",
        "p7_loan_a":        "Préstamo auto",
        "p7_debts":         "Otras deudas",
        "p7_auto_pets":     "🚗  Auto & Mascotas",
        "p7_gas":           "Gasolina",
        "p7_maint":         "Mantenimiento",
        "p7_pet_food":      "Comida mascotas",
        "p7_pet_vet":       "Veterinario",
        "p7_pet_other":     "Otros mascotas",
        "p7_vars":          "🛒  Variables & Suscripciones",
        "p7_grocery":       "Supermercado",
        "p7_out":           "Salidas",
        "p7_extras_sec":    "➕  Gastos Extra",
        "p7_extra_lbl":     "Extra: {desc}",
        "p7_summary":       "📊  Resumen Total",
        "p7_tot_inc":       "Total Ingresos",
        "p7_tot_exp":       "Total Gastos",
        "p7_saving":        "AHORRO MENSUAL",
        "p7_goal":          "🎯  Análisis de Meta",
        "p7_goal_amt":      "Meta de ahorro",
        "p7_months_left":   "Meses restantes",
        "p7_need_mo":       "Ahorro necesario/mes",
        "p7_curr_mo":       "Tu ahorro actual/mes",
        "p7_projection":    "Proyección total",
        "p7_export":        "📄  Exportar Reporte PDF",
        "p7_new":           "💡  Usa 'Nueva Consulta' para empezar de nuevo.",
        "pdf_saved":        "✅ PDF Generado",
        "pdf_saved_msg":    "Reporte guardado en:\n{ruta}",
        "pdf_save_title":   "Guardar reporte PDF",
        "months":           ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
                             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
        "tax_css":          "CSS (9.75%)",
        "tax_edu":          "Seguro Educativo (1.25%)",
        "tax_isr":          "ISR mensual estimado",
        "tax_pension":      "Pensión (16%)",
        "tax_salud":        "Salud (12.5%)",
        "tax_solidaridad":  "Fondo Solidaridad (1%)",
        "tax_renta":        "Retención en la Fuente (est.)",
        "pdf_title":        "Calculadora de Salario & Metas",
        "pdf_by":           "by Erick Perez",
        "pdf_date":         "Generado el {d}",
        "pdf_salary":       "Salario e Impuestos",
        "pdf_gross":        "Salario Bruto",
        "pdf_ded_est":      "Total Deducciones (estimado)",
        "pdf_net_est":      "Salario Neto Estimado",
        "pdf_net_real":     "Salario Real Recibido (slip)",
        "pdf_note":         "NOTA: Calculo estimado. Verificar con slip de pago oficial.",
        "pdf_income":       "Ingresos Totales",
        "pdf_net_base":     "Salario Neto (base)",
        "pdf_extra_inc":    "Ingreso Extra",
        "pdf_total_inc":    "TOTAL INGRESOS",
        "pdf_home":         "Gastos del Hogar",
        "pdf_rent":         "Alquiler / Hipoteca",
        "pdf_electric":     "Luz / Electricidad",
        "pdf_water":        "Agua",
        "pdf_mobile":       "Data Movil",
        "pdf_loans":        "Prestamos y Deudas",
        "pdf_loan_p":       "Prestamo Personal",
        "pdf_loan_a":       "Prestamo de Auto",
        "pdf_debts":        "Otras Deudas",
        "pdf_auto":         "Auto y Mascotas",
        "pdf_gas":          "Gasolina",
        "pdf_maint":        "Mantenimiento",
        "pdf_pet_food":     "Comida mascotas",
        "pdf_pet_vet":      "Veterinario",
        "pdf_pet_other":    "Otros mascotas",
        "pdf_vars":         "Variables y Suscripciones",
        "pdf_grocery":      "Supermercado",
        "pdf_out":          "Salidas",
        "pdf_extras":       "Gastos Extra",
        "pdf_summary":      "Resumen Final",
        "pdf_tot_inc":      "Total Ingresos",
        "pdf_tot_exp":      "Total Gastos",
        "pdf_saving":       "Ahorro Mensual",
        "pdf_analysis":     "Analisis de Meta",
        "pdf_goal_amt":     "Meta de ahorro",
        "pdf_objective":    "Objetivo: {mes} {anio}",
        "pdf_months_left":  "{n} meses restantes",
        "pdf_need_mo":      "Ahorro necesario/mes",
        "pdf_curr_mo":      "Ahorro actual/mes",
        "pdf_projection":   "Proyeccion total",
        "pdf_ok":           "EXCELENTE: Alcanzaras tu meta antes de {mes} {anio}.",
        "pdf_warn":         "ATENCION: Necesitas {sym}{n:,.0f} mas/mes para tu meta.",
        "pdf_alert":        "ALERTA: Tus gastos superan tus ingresos.",
        "pdf_footer":       "Calculadora de Salario & Metas  •  by Erick Perez  •  {nombre}  •  {pais}",
    },
    "en": {
        "app_title":        "Salary & Goals Calculator  —  by Erick Perez",
        "title_bar":        "  💰  Salary & Goals Calculator  —  by Erick Perez",
        "splash_sub":       "Salary & Goals Calculator",
        "splash_edition":   "v0.2 BETA  •  Panama & Colombia",
        "splash_loading":   ["Starting...", "Loading interface...",
                             "Setting up taxes...",
                             "Preparing calculator...", "Ready!"],
        "back":             "← Back",
        "next":             "Next →",
        "new_query":        "🔄  New Query",
        "step_of":          "Step {s} of {t}",
        "steps":            ["Profile","Goal","Income","Home","Debts","Leisure","Extras","Results"],
        "dark_mode":        "🌙 Dark",
        "light_mode":       "☀️ Light",
        "save_session":     "💾 Save",
        "load_session":     "📂 Load",
        "sessions_title":   "Saved Sessions",
        "save_name_prompt": "Session name:",
        "save_success":     "Session saved as «{name}»",
        "save_error":       "Could not save session.",
        "load_select":      "Select a session to load:",
        "load_none":        "No saved sessions.",
        "load_success":     "Session «{name}» loaded.",
        "delete_session":   "Delete",
        "cancel":           "Cancel",
        "ok":               "OK",
        "req_name":         "Please enter your name.",
        "req_field":        "Required field",
        "req_meta":         "Enter a valid savings goal.",
        "req_anio":         "Enter a valid year (e.g. 2026).",
        "invalid_year":     "Invalid year",
        "req_salary":       "Enter your gross monthly salary.",
        "p0_title":         "👤  Your Profile",
        "p0_sub":           "Tell us about yourself to personalize your report.",
        "p0_section":       "Personal Information",
        "p0_name":          "Full name *",
        "p0_country":       "Country of residence *",
        "p0_note":          "⚠️  BETA VERSION IN DEVELOPMENT — Available for Panama 🇵🇦 and Colombia 🇨🇴. More countries coming soon. All calculations are estimates.",
        "p1_title":         "🎯  Savings Goal",
        "p1_sub":           "Define how much you want to save and by when.",
        "p1_section":       "Your Financial Goal",
        "p1_meta":          "Savings goal *",
        "p1_month":         "Target month *",
        "p1_year":          "Target year *",
        "p1_tip":           "💡  Consistent monthly savings, even small amounts, have a huge long-term impact. Be realistic with your goal.",
        "p2_title":         "💵  Income  —  {nombre}",
        "p2_sub":           "Country: {pais}  |  Deductions calculated automatically.",
        "p2_section":       "Monthly Salary",
        "p2_gross":         "Gross monthly salary *",
        "p2_extra":         "Extra income this month",
        "p2_imp_hint":      "🧮  Enter your gross salary to see the breakdown",
        "p2_imp_title":     "🧮  Estimated deductions — {pais}",
        "p2_net_est":       "  Estimated Net Salary:",
        "p2_note":          "⚠️  Tax calculation is an estimate. Actual amount may vary. Always check your official pay stub.",
        "p2_real":          "ACTUAL salary received per your pay stub (if different from estimate)",
        "p2_real_tip":      "💡  Leave empty to use\nthe estimated net salary.",
        "p3_title":         "🏠  Home Expenses",
        "p3_sub":           "Basic services and housing.",
        "p3_section":       "Fixed Monthly Expenses",
        "p3_rent":          "Rent / Mortgage",
        "p3_internet":      "Internet",
        "p3_electric":      "Electricity",
        "p3_water":         "Water",
        "p3_mobile":        "Mobile Data / Phone",
        "p4_title":         "🏦  Debts, Car & Pets",
        "p4_sub":           "Loans, vehicle expenses and pet care.",
        "p4_s1":            "Loans & Debts",
        "p4_loan_p":        "Personal Loan",
        "p4_loan_a":        "Car Loan",
        "p4_debts":         "Other Debts",
        "p4_s2":            "Car Expenses",
        "p4_gas":           "Gas",
        "p4_maint":         "Maintenance",
        "p4_s3":            "Pet Expenses",
        "p4_pet_food":      "Pet food",
        "p4_pet_vet":       "Veterinarian",
        "p4_pet_other":     "Other pet expenses",
        "p5_title":         "🎬  Leisure & Subscriptions",
        "p5_sub":           "Entertainment, food and digital platforms.",
        "p5_s1":            "Variable Expenses",
        "p5_grocery":       "Grocery / Food",
        "p5_out":           "Outings / Entertainment",
        "p5_delivery":      "Delivery",
        "p5_s2":            "Digital Subscriptions",
        "p6_title":         "➕  Extra Expenses",
        "p6_sub":           "Any additional expense that doesn't fit previous categories.",
        "p6_section":       "Additional Expenses",
        "p6_extra":         "Extra Expense {n}",
        "p6_desc":          "Description",
        "p6_hint":          "✔  Pressing 'Next' will calculate all your results.",
        "p7_title":         "📊  Results  —  {nombre}",
        "p7_sub":           "{pais}  •  Goal: {sym}{meta:,.0f} for {mes} {anio}",
        "p7_deficit":       "⚠  Monthly deficit of {sym}{amt:,.0f}  —  Expenses exceed income",
        "p7_ontrack":       "🎉  Saving {sym}{amt:,.0f}/mo  —  You'll reach your goal!",
        "p7_need":          "💡  Saving {sym}{amt:,.0f}/mo  —  Need {sym}{falta:,.0f} more/mo",
        "p7_salary_imp":    "🧾  Salary & Taxes",
        "p7_total_ded":     "Total deductions (estimated)",
        "p7_net_est":       "Net Salary (estimated)",
        "p7_net_real":      "Actual Salary (pay stub)",
        "p7_imp_note":      "⚠️  Estimated. May vary. Verify with your official pay stub.",
        "p7_income":        "💵  Income",
        "p7_net_base":      "Net Salary (base)",
        "p7_extra_inc":     "Extra Income",
        "p7_total_inc":     "TOTAL INCOME",
        "p7_home":          "🏠  Home",
        "p7_rent":          "Rent",
        "p7_electric":      "Electricity",
        "p7_water":         "Water",
        "p7_mobile":        "Mobile Data",
        "p7_loans":         "🏦  Loans",
        "p7_loan_p":        "Personal loan",
        "p7_loan_a":        "Car loan",
        "p7_debts":         "Other debts",
        "p7_auto_pets":     "🚗  Car & Pets",
        "p7_gas":           "Gas",
        "p7_maint":         "Maintenance",
        "p7_pet_food":      "Pet food",
        "p7_pet_vet":       "Veterinarian",
        "p7_pet_other":     "Other pets",
        "p7_vars":          "🛒  Variable & Subscriptions",
        "p7_grocery":       "Grocery",
        "p7_out":           "Outings",
        "p7_extras_sec":    "➕  Extra Expenses",
        "p7_extra_lbl":     "Extra: {desc}",
        "p7_summary":       "📊  Total Summary",
        "p7_tot_inc":       "Total Income",
        "p7_tot_exp":       "Total Expenses",
        "p7_saving":        "MONTHLY SAVINGS",
        "p7_goal":          "🎯  Goal Analysis",
        "p7_goal_amt":      "Savings goal",
        "p7_months_left":   "Months remaining",
        "p7_need_mo":       "Required savings/mo",
        "p7_curr_mo":       "Your current savings/mo",
        "p7_projection":    "Total projection",
        "p7_export":        "📄  Export PDF Report",
        "p7_new":           "💡  Use 'New Query' to start over.",
        "pdf_saved":        "✅ PDF Generated",
        "pdf_saved_msg":    "Report saved at:\n{ruta}",
        "pdf_save_title":   "Save PDF report",
        "months":           ["January","February","March","April","May","June",
                             "July","August","September","October","November","December"],
        "tax_css":          "CSS (9.75%)",
        "tax_edu":          "Educational Insurance (1.25%)",
        "tax_isr":          "Estimated monthly ISR",
        "tax_pension":      "Pension (16%)",
        "tax_salud":        "Health (12.5%)",
        "tax_solidaridad":  "Solidarity Fund (1%)",
        "tax_renta":        "Income Withholding (est.)",
        "pdf_title":        "Salary & Goals Calculator",
        "pdf_by":           "by Erick Perez",
        "pdf_date":         "Generated on {d}",
        "pdf_salary":       "Salary & Taxes",
        "pdf_gross":        "Gross Salary",
        "pdf_ded_est":      "Total Deductions (estimated)",
        "pdf_net_est":      "Estimated Net Salary",
        "pdf_net_real":     "Actual Salary Received (pay stub)",
        "pdf_note":         "NOTE: Estimated. Verify with your official pay stub.",
        "pdf_income":       "Total Income",
        "pdf_net_base":     "Net Salary (base)",
        "pdf_extra_inc":    "Extra Income",
        "pdf_total_inc":    "TOTAL INCOME",
        "pdf_home":         "Fixed Home Expenses",
        "pdf_rent":         "Rent / Mortgage",
        "pdf_electric":     "Electricity",
        "pdf_water":        "Water",
        "pdf_mobile":       "Mobile Data",
        "pdf_loans":        "Loans & Debts",
        "pdf_loan_p":       "Personal Loan",
        "pdf_loan_a":       "Car Loan",
        "pdf_debts":        "Other Debts",
        "pdf_auto":         "Car & Pets",
        "pdf_gas":          "Gas",
        "pdf_maint":        "Maintenance",
        "pdf_pet_food":     "Pet food",
        "pdf_pet_vet":      "Veterinarian",
        "pdf_pet_other":    "Other pets",
        "pdf_vars":         "Variable & Subscriptions",
        "pdf_grocery":      "Grocery",
        "pdf_out":          "Outings",
        "pdf_extras":       "Extra Expenses",
        "pdf_summary":      "Final Summary",
        "pdf_tot_inc":      "Total Income",
        "pdf_tot_exp":      "Total Expenses",
        "pdf_saving":       "Monthly Savings",
        "pdf_analysis":     "Goal Analysis",
        "pdf_goal_amt":     "Savings goal",
        "pdf_objective":    "Target: {mes} {anio}",
        "pdf_months_left":  "{n} months remaining",
        "pdf_need_mo":      "Required savings/mo",
        "pdf_curr_mo":      "Current savings/mo",
        "pdf_projection":   "Total projection",
        "pdf_ok":           "EXCELLENT: You will reach your goal before {mes} {anio}.",
        "pdf_warn":         "ATTENTION: You need {sym}{n:,.0f} more/mo to reach your goal.",
        "pdf_alert":        "ALERT: Your expenses exceed your income.",
        "pdf_footer":       "Salary & Goals Calculator  •  by Erick Perez  •  {nombre}  •  {pais}",
    },
}

def T(key, **kw):
    txt = LANGS[_LANG].get(key, LANGS["es"].get(key, key))
    return txt.format(**kw) if kw else txt

def get_months():
    return LANGS[_LANG]["months"]

# ══════════════════════════════════════════════════════════
#  THEME — light / dark
# ══════════════════════════════════════════════════════════

THEME_LIGHT = {
    "bg":           "#f3f3f3",
    "surface":      "#ffffff",
    "surface2":     "#f9f9f9",
    "accent":       "#0067c0",
    "accent_h":     "#1a7ed4",
    "text":         "#1a1a1a",
    "text2":        "#5a5a5a",
    "text3":        "#8a8a8a",
    "border":       "#e0e0e0",
    "border2":      "#c8c8c8",
    "success":      "#107c10",
    "danger":       "#d13438",
    "warning":      "#ca5010",
    "gold":         "#8a6914",
    "gold_bg":      "#fef9e7",
    "gold_border":  "#f0c040",
    "title_bar":    "#202020",
    "step_done":    "#107c10",
    "step_act":     "#0067c0",
    "step_pend":    "#c8c8c8",
    "input_bg":     "#ffffff",
    "input_border": "#8a8a8a",
    "input_focus":  "#0067c0",
    "btn_bg":       "#0067c0",
    "btn_fg":       "#ffffff",
    "btn_sec":      "#f3f3f3",
    "btn_sec_fg":   "#1a1a1a",
    "note_bg":      "#fff4ce",
    "note_border":  "#f0b400",
}

THEME_DARK = {
    "bg":           "#1a1a2e",
    "surface":      "#16213e",
    "surface2":     "#0f3460",
    "accent":       "#4fc3f7",
    "accent_h":     "#81d4fa",
    "text":         "#e8eaf6",
    "text2":        "#b0bec5",
    "text3":        "#78909c",
    "border":       "#2d3561",
    "border2":      "#3d4b7a",
    "success":      "#69f0ae",
    "danger":       "#ff5252",
    "warning":      "#ffab40",
    "gold":         "#ffd54f",
    "gold_bg":      "#1a1500",
    "gold_border":  "#ffd54f",
    "title_bar":    "#0a0a1a",
    "step_done":    "#69f0ae",
    "step_act":     "#4fc3f7",
    "step_pend":    "#3d4b7a",
    "input_bg":     "#0f3460",
    "input_border": "#4fc3f7",
    "input_focus":  "#81d4fa",
    "btn_bg":       "#4fc3f7",
    "btn_fg":       "#0a0a1a",
    "btn_sec":      "#2d3561",
    "btn_sec_fg":   "#e8eaf6",
    "note_bg":      "#1a1500",
    "note_border":  "#ffd54f",
}

W11 = dict(THEME_LIGHT)

def _rebuild_theme():
    src = THEME_DARK if _DARK_MODE else THEME_LIGHT
    W11.update(src)

FONT    = "Segoe UI"
F_TITLE = (FONT, 20, "bold")
F_SUBH  = (FONT, 11, "bold")
F_BODY  = (FONT, 10)
F_SMALL = (FONT, 9)
F_INPUT = (FONT, 10)
F_BTN   = (FONT, 10, "bold")
F_LABEL = (FONT, 9)

# ══════════════════════════════════════════════════════════
#  TAX CALCULATORS
# ══════════════════════════════════════════════════════════

def calcular_impuestos_panama(salario_bruto):
    css           = salario_bruto * 0.0975
    seg_educativo = salario_bruto * 0.0125
    base_isr      = salario_bruto - css - seg_educativo
    anual         = base_isr * 12
    if anual <= 11000:
        isr_anual = 0
    elif anual <= 50000:
        isr_anual = (anual - 11000) * 0.15
    else:
        isr_anual = (50000 - 11000) * 0.15 + (anual - 50000) * 0.25
    isr_mes = isr_anual / 12
    total   = css + seg_educativo + isr_mes
    neto    = salario_bruto - total
    return {
        "total_imp":    round(total, 2),
        "salario_neto": round(neto, 2),
        "detalle": [
            (T("tax_css"),  round(css, 2)),
            (T("tax_edu"),  round(seg_educativo, 2)),
            (T("tax_isr"),  round(isr_mes, 2)),
        ]
    }

def calcular_impuestos_colombia(salario_bruto):
    # Deducciones de empleado (sobre salario bruto):
    # Pensión: 4%, Salud: 4%, Fondo Solidaridad: 1% si > 4 SMMLV (~$5,200,000)
    # Retención en la fuente: progresiva según UVT (valor UVT 2024 ≈ $47,065 COP)
    pension  = salario_bruto * 0.04
    salud    = salario_bruto * 0.04
    uvt      = 47065
    ingreso_mensual_uvt = salario_bruto / uvt
    # Tabla simplificada de retención en la fuente mensual
    ingreso_anual_uvt = ingreso_mensual_uvt * 12
    if ingreso_anual_uvt <= 95:
        renta = 0
    elif ingreso_anual_uvt <= 150:
        renta = (ingreso_anual_uvt - 95) * 0.19 * uvt / 12
    elif ingreso_anual_uvt <= 360:
        renta = ((ingreso_anual_uvt - 150) * 0.28 + 10.45) * uvt / 12
    elif ingreso_anual_uvt <= 640:
        renta = ((ingreso_anual_uvt - 360) * 0.33 + 69.25) * uvt / 12
    elif ingreso_anual_uvt <= 945:
        renta = ((ingreso_anual_uvt - 640) * 0.35 + 162.65) * uvt / 12
    elif ingreso_anual_uvt <= 2300:
        renta = ((ingreso_anual_uvt - 945) * 0.37 + 269.40) * uvt / 12
    else:
        renta = ((ingreso_anual_uvt - 2300) * 0.39 + 770.85) * uvt / 12

    total = pension + salud + renta
    neto  = salario_bruto - total
    return {
        "total_imp":    round(total, 2),
        "salario_neto": round(neto, 2),
        "detalle": [
            (T("tax_pension"), round(pension, 2)),
            (T("tax_salud"),   round(salud,   2)),
            (T("tax_renta"),   round(renta,   2)),
        ]
    }

PAISES = {
    "Panamá": {
        "moneda": "USD", "simbolo": "$", "flag": "🇵🇦",
        "calcular": calcular_impuestos_panama,
    },
    "Colombia": {
        "moneda": "COP", "simbolo": "$", "flag": "🇨🇴",
        "calcular": calcular_impuestos_colombia,
    },
}

def get_sym(pais):
    return PAISES.get(pais, {}).get("simbolo", "$")

def fmt(amount, pais):
    """Format a number with currency symbol appropriate to country."""
    sym = get_sym(pais)
    if pais == "Colombia":
        return f"{sym}{amount:,.0f}"
    return f"{sym}{amount:,.2f}"

def calcular_meses(anio_meta, mes_meta):
    hoy  = date.today()
    meta = date(anio_meta, mes_meta, 1)
    if hoy >= meta:
        return 0
    return (meta.year - hoy.year)*12 + (meta.month - hoy.month)

def val(entry):
    try:
        return max(0.0, float(entry.get().strip().replace(",",".")))
    except:
        return 0.0

# ══════════════════════════════════════════════════════════
#  SESSION SAVE / LOAD
# ══════════════════════════════════════════════════════════

def load_sessions():
    try:
        if os.path.exists(SESSIONS_FILE):
            with open(SESSIONS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except:
        pass
    return {}

def save_sessions(sessions):
    try:
        with open(SESSIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(sessions, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False

# ══════════════════════════════════════════════════════════
#  LANGUAGE BOOT SCREEN
# ══════════════════════════════════════════════════════════

class LanguageBootScreen(tk.Tk):
    """First screen shown before the splash — pick language."""
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.configure(bg="#0f172a")
        w, h = 420, 300
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
        self.lift()
        self.attributes("-topmost", True)
        self._chosen = None
        self._build()

    def _build(self):
        tk.Label(self, text="💰", font=(FONT, 42),
                 bg="#0f172a", fg="#f0c040").pack(pady=(30, 5))
        tk.Label(self, text="Salary & Goals Calculator",
                 font=(FONT, 16, "bold"), bg="#0f172a", fg="#ffffff").pack()
        tk.Label(self, text="Calculadora de Salario & Metas",
                 font=(FONT, 11, "italic"), bg="#0f172a", fg="#94a3b8").pack(pady=(2,4))
        tk.Label(self, text="by Erick Perez  •  v0.2 BETA",
                 font=(FONT, 9), bg="#0f172a", fg="#475569").pack(pady=(0, 20))

        tk.Label(self, text="Select Language / Selecciona Idioma",
                 font=(FONT, 10), bg="#0f172a", fg="#64748b").pack(pady=(0, 10))

        btn_frame = tk.Frame(self, bg="#0f172a")
        btn_frame.pack()

        def _pick(lang):
            self._chosen = lang
            self.destroy()

        es_btn = tk.Button(btn_frame, text="🇪🇸  Español", font=(FONT, 13, "bold"),
                           bg="#0067c0", fg="white", relief="flat",
                           padx=28, pady=12, cursor="hand2",
                           command=lambda: _pick("es"))
        es_btn.pack(side="left", padx=10)
        es_btn.bind("<Enter>", lambda e: es_btn.config(bg="#1a7ed4"))
        es_btn.bind("<Leave>", lambda e: es_btn.config(bg="#0067c0"))

        en_btn = tk.Button(btn_frame, text="🇺🇸  English", font=(FONT, 13, "bold"),
                           bg="#334155", fg="white", relief="flat",
                           padx=28, pady=12, cursor="hand2",
                           command=lambda: _pick("en"))
        en_btn.pack(side="left", padx=10)
        en_btn.bind("<Enter>", lambda e: en_btn.config(bg="#4a5568"))
        en_btn.bind("<Leave>", lambda e: en_btn.config(bg="#334155"))

    def get_choice(self):
        self.mainloop()
        return self._chosen or "es"

# ══════════════════════════════════════════════════════════
#  SPLASH SCREEN
# ══════════════════════════════════════════════════════════

class SplashScreen(tk.Toplevel):
    def __init__(self, parent, on_done):
        super().__init__(parent)
        self.on_done = on_done
        self.overrideredirect(True)
        self.configure(bg="#0f172a")
        w, h = 580, 360
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
        self.lift(); self.attributes("-topmost", True)

        self.canvas = tk.Canvas(self, bg="#0f172a", width=w, height=h,
                                highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        import random
        self._particles = []
        for _ in range(28):
            x = random.randint(0, w); y = random.randint(0, h)
            r = random.uniform(1.5, 4.5)
            vx = random.uniform(-0.4, 0.4); vy = random.uniform(-0.3, 0.3)
            col = random.choice(["#0067c0","#1a7ed4","#38bdf8","#7dd3fc"])
            cid = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=col, outline="")
            self._particles.append({"id":cid,"x":x,"y":y,"vx":vx,"vy":vy,"r":r,"w":w,"h":h})

        self.canvas.create_text(w//2, 162, text=T("splash_sub"),
                                font=(FONT, 22, "bold"), fill="#ffffff")
        self.canvas.create_text(w//2, 202, text="by Erick Perez",
                                font=(FONT, 13, "italic"), fill="#94a3b8")
        self.canvas.create_text(w//2, 228, text=T("splash_edition"),
                                font=(FONT, 10), fill="#475569")
        self._coin_id = self.canvas.create_text(w//2, 80, text="💰",
                                                font=(FONT, 48), fill="#f0c040")
        self._bar_bg = self.canvas.create_rectangle(
            w//2-180, 280, w//2+180, 298, fill="#1e293b", outline="#334155")
        self._bar_fg = self.canvas.create_rectangle(
            w//2-180, 280, w//2-180, 298, fill="#0067c0", outline="")
        self._bar_lbl = self.canvas.create_text(
            w//2, 312, text="0%", font=(FONT, 9), fill="#64748b")

        self._bar_w    = 360
        self._bar_x0   = w//2 - 180
        self._total_ms = 2800
        self._step_ms  = 30
        self._elapsed  = 0
        self._animate()

    def _animate(self):
        self._elapsed += self._step_ms
        pct = min(self._elapsed / self._total_ms, 1.0)
        msgs = LANGS[_LANG]["splash_loading"]
        thresholds = [0, 20, 50, 75, 95]
        pct100 = int(pct * 100)
        msg = msgs[0]
        for i, th in enumerate(thresholds):
            if pct100 >= th:
                msg = msgs[i]

        for p in self._particles:
            p["x"] += p["vx"]; p["y"] += p["vy"]
            if p["x"] < 0: p["x"] = p["w"]
            if p["x"] > p["w"]: p["x"] = 0
            if p["y"] < 0: p["y"] = p["h"]
            if p["y"] > p["h"]: p["y"] = 0
            r = p["r"]
            self.canvas.coords(p["id"], p["x"]-r, p["y"]-r, p["x"]+r, p["y"]+r)

        bounce = math.sin(self._elapsed / 200) * 10
        self.canvas.coords(self._coin_id, 580//2, 80 + bounce)
        x1 = self._bar_x0 + int(self._bar_w * pct)
        self.canvas.coords(self._bar_fg, self._bar_x0, 280, x1, 298)
        self.canvas.itemconfig(self._bar_lbl, text=f"{msg}  {pct100}%")

        if pct < 1.0:
            self.after(self._step_ms, self._animate)
        else:
            self.after(300, self._finish)

    def _finish(self):
        self.destroy()
        self.on_done()

# ══════════════════════════════════════════════════════════
#  WIDGETS
# ══════════════════════════════════════════════════════════

class W11Entry(tk.Frame):
    def __init__(self, parent, label="", prefix="$", width=18, **kw):
        super().__init__(parent, bg=W11["surface"])
        if label:
            tk.Label(self, text=label, font=F_LABEL, bg=W11["surface"],
                     fg=W11["text2"], anchor="w").pack(fill="x")
        bf = tk.Frame(self, bg=W11["input_border"])
        bf.pack(fill="x", pady=(1,0))
        inner = tk.Frame(bf, bg=W11["input_bg"])
        inner.pack(fill="x", padx=1, pady=1)
        if prefix:
            tk.Label(inner, text=prefix, font=F_INPUT,
                     bg=W11["input_bg"], fg=W11["text2"], padx=6).pack(side="left")
        self.var   = tk.StringVar()
        self.entry = tk.Entry(inner, textvariable=self.var, font=F_INPUT,
                              bg=W11["input_bg"], fg=W11["text"], relief="flat",
                              width=width, insertbackground=W11["accent"])
        self.entry.pack(side="left", fill="x", expand=True, padx=(0,6), pady=5)
        self._bf = bf
        self.entry.bind("<FocusIn>",  lambda e: self._bf.config(bg=W11["input_focus"]))
        self.entry.bind("<FocusOut>", lambda e: self._bf.config(bg=W11["input_border"]))

    def get(self):    return self.var.get()
    def set(self, v): self.var.set(v)


class W11Combo(tk.Frame):
    def __init__(self, parent, label="", values=[], width=20, **kw):
        super().__init__(parent, bg=W11["surface"])
        if label:
            tk.Label(self, text=label, font=F_LABEL, bg=W11["surface"],
                     fg=W11["text2"], anchor="w").pack(fill="x")
        s = ttk.Style()
        s.configure("W11.TCombobox", fieldbackground=W11["input_bg"],
                    background=W11["input_bg"], foreground=W11["text"],
                    selectbackground=W11["accent"])
        self.cb = ttk.Combobox(self, values=values, state="readonly",
                               font=F_INPUT, width=width, style="W11.TCombobox")
        self.cb.pack(fill="x", pady=(1,0))
        if values: self.cb.set(values[0])

    def get(self):    return self.cb.get()
    def set(self, v): self.cb.set(v)


class W11Button(tk.Button):
    def __init__(self, parent, text="", primary=True, command=None, **kw):
        bg  = W11["btn_bg"]   if primary else W11["btn_sec"]
        fg  = W11["btn_fg"]   if primary else W11["btn_sec_fg"]
        abg = W11["accent_h"] if primary else W11["border2"]
        super().__init__(parent, text=text, font=F_BTN, bg=bg, fg=fg,
                         activebackground=abg, activeforeground=fg,
                         relief="flat", padx=20, pady=8,
                         cursor="hand2", command=command, **kw)
        self._bg = bg; self._abg = abg
        self.bind("<Enter>", lambda e: self.config(bg=abg))
        self.bind("<Leave>", lambda e: self.config(bg=self._bg))


def card(parent, padx=20, pady=16):
    f = tk.Frame(parent, bg=W11["surface"],
                 highlightbackground=W11["border"], highlightthickness=1)
    f.pack(fill="x", padx=padx, pady=pady)
    return f

def section_title(parent, text, icon=""):
    tk.Label(parent, text=f"{icon}  {text}" if icon else text,
             font=F_SUBH, bg=W11["surface"], fg=W11["text"]
             ).pack(anchor="w", padx=14, pady=(12,4))
    tk.Frame(parent, bg=W11["border"], height=1).pack(fill="x", padx=14, pady=(0,8))

def note_box(parent, text, color_bg=None, color_border=None):
    bg  = color_bg     or W11["note_bg"]
    brd = color_border or W11["note_border"]
    f = tk.Frame(parent, bg=bg, highlightbackground=brd, highlightthickness=1)
    f.pack(fill="x", padx=14, pady=(0,10))
    tk.Label(f, text=text, font=F_SMALL, bg=bg, fg=W11["text2"],
             wraplength=680, justify="left").pack(padx=12, pady=8, anchor="w")

# ══════════════════════════════════════════════════════════
#  STEP BAR
# ══════════════════════════════════════════════════════════

class StepBar(tk.Frame):
    def __init__(self, parent, **kw):
        super().__init__(parent, bg=W11["bg"], height=64)
        self._circles = []; self._labels = []
        steps = T("steps")
        for i, label in enumerate(steps):
            col = tk.Frame(self, bg=W11["bg"])
            col.pack(side="left", expand=True)
            circ = tk.Label(col, text=str(i+1), font=(FONT,9,"bold"),
                            bg=W11["step_pend"], fg="white", width=3, relief="flat")
            circ.pack(pady=(8,2))
            lbl = tk.Label(col, text=label, font=F_SMALL,
                           bg=W11["bg"], fg=W11["text3"])
            lbl.pack()
            self._circles.append(circ); self._labels.append(lbl)
            if i < len(steps)-1:
                tk.Frame(self, bg=W11["border2"], height=2, width=20
                         ).pack(side="left", pady=8, anchor="n")
        self.update_step(0)

    def update_step(self, step):
        steps = T("steps")
        self.config(bg=W11["bg"])
        for i, (c, l) in enumerate(zip(self._circles, self._labels)):
            lbl_text = steps[i] if i < len(steps) else str(i+1)
            l.config(text=lbl_text)
            c_parent = c.master; c_parent.config(bg=W11["bg"])
            l.config(bg=W11["bg"])
            if i < step:
                c.config(bg=W11["step_done"]); l.config(fg=W11["step_done"], font=F_SMALL)
            elif i == step:
                c.config(bg=W11["step_act"]);  l.config(fg=W11["step_act"], font=(FONT,9,"bold"))
            else:
                c.config(bg=W11["step_pend"]); l.config(fg=W11["text3"], font=F_SMALL)

# ══════════════════════════════════════════════════════════
#  PDF GENERATOR
# ══════════════════════════════════════════════════════════

def generar_pdf(datos, ruta):
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                        Table, TableStyle, HRFlowable)
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER, TA_RIGHT

        doc = SimpleDocTemplate(ruta, pagesize=letter,
                                leftMargin=0.75*inch, rightMargin=0.75*inch,
                                topMargin=0.75*inch, bottomMargin=0.75*inch)
        styles  = getSampleStyleSheet()
        C_AZUL  = colors.HexColor("#0067c0")
        C_VERDE = colors.HexColor("#107c10")
        C_ROJO  = colors.HexColor("#d13438")
        C_GOLD  = colors.HexColor("#8a6914")
        C_GRIS  = colors.HexColor("#f3f3f3")
        C_BORDE = colors.HexColor("#e0e0e0")
        C_DARK  = colors.HexColor("#1a1a1a")

        tit  = ParagraphStyle("tit", fontSize=22, textColor=C_AZUL,
                              alignment=TA_CENTER, spaceAfter=4, fontName="Helvetica-Bold")
        sub  = ParagraphStyle("sub", fontSize=10, textColor=colors.grey,
                              alignment=TA_CENTER, spaceAfter=14)
        h2   = ParagraphStyle("h2",  fontSize=12, textColor=C_AZUL,
                              spaceBefore=14, spaceAfter=4, fontName="Helvetica-Bold")
        norm = styles["Normal"]
        der  = ParagraphStyle("der", fontSize=10, alignment=TA_RIGHT)

        ts = TableStyle([
            ("ROWBACKGROUNDS",(0,0),(-1,-1),[C_GRIS, colors.white]),
            ("BOX",(0,0),(-1,-1),0.5,C_BORDE),("INNERGRID",(0,0),(-1,-1),0.25,C_BORDE),
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
            ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
        ])

        pais  = datos.get("pais","Panamá")
        sym   = get_sym(pais)
        f_amt = lambda v: f"{sym}{v:,.0f}" if pais=="Colombia" else f"{sym}{v:,.2f}"

        def fila(lbl, monto, col=None, bold=False):
            fn  = "Helvetica-Bold" if bold else "Helvetica"
            col = col or C_DARK
            hx  = col.hexval() if hasattr(col,"hexval") else str(col)
            return [
                Paragraph(f'<font name="{fn}">{lbl}</font>', norm),
                Paragraph(f'<font name="{fn}" color="{hx}">{f_amt(monto)}</font>', der),
            ]

        def tabla(rows):
            t = Table(rows, colWidths=["70%","30%"])
            t.setStyle(ts); return t

        imp      = datos["impuestos"]
        sal_real = datos.get("salario_real", 0)
        sal_base = sal_real if sal_real > 0 else imp["salario_neto"]
        months   = get_months()
        mes_n    = months[datos["mes_num"]-1]
        nombre   = datos.get("nombre","")

        story = []
        story.append(Paragraph(T("pdf_title"), tit))
        story.append(Paragraph(f"{T('pdf_by')}  •  {nombre}  •  {pais}", sub))
        story.append(Paragraph(
            T("pdf_date", d=date.today().strftime('%d/%m/%Y')) +
            f"  •  {T('pdf_goal_amt')}: {f_amt(datos['meta'])} / {mes_n} {datos['anio_meta']}", sub))
        story.append(HRFlowable(width="100%", thickness=2, color=C_AZUL, spaceAfter=10))

        story.append(Paragraph(T("pdf_salary"), h2))
        rows_imp = [fila(T("pdf_gross"), datos["salario"])]
        for nd, md in imp["detalle"]:
            rows_imp.append(fila(f"  - {nd}", md, C_ROJO))
        rows_imp.append(fila(T("pdf_ded_est"), imp["total_imp"], C_ROJO, True))
        if sal_real > 0:
            rows_imp += [fila(T("pdf_net_est"), imp["salario_neto"], C_AZUL),
                         fila(T("pdf_net_real"), sal_real, C_VERDE, True)]
        else:
            rows_imp.append(fila(T("pdf_net_est"), imp["salario_neto"], C_VERDE, True))
        story.append(tabla(rows_imp))

        nota_s = ParagraphStyle("nota", fontSize=8, textColor=colors.HexColor("#8a6914"),
                                backColor=colors.HexColor("#fef9e7"),
                                spaceAfter=8, leftIndent=8, rightIndent=8, leading=12)
        story.append(Paragraph(T("pdf_note"), nota_s))
        story.append(Spacer(1, 8))

        story.append(Paragraph(T("pdf_income"), h2))
        story.append(tabla([
            fila(T("pdf_net_base"),  sal_base),
            fila(T("pdf_extra_inc"), datos.get("ingreso_extra",0)),
            fila(T("pdf_total_inc"), datos["total_ingresos"], C_VERDE, True),
        ]))

        story.append(Paragraph(T("pdf_home"), h2))
        story.append(tabla([
            fila(T("pdf_rent"),     datos.get("alquiler",0)),
            fila("Internet",        datos.get("internet",0)),
            fila(T("pdf_electric"), datos.get("luz",0)),
            fila(T("pdf_water"),    datos.get("agua",0)),
            fila(T("pdf_mobile"),   datos.get("data_movil",0)),
        ]))
        story.append(Paragraph(T("pdf_loans"), h2))
        story.append(tabla([
            fila(T("pdf_loan_p"), datos.get("prestamo_personal",0)),
            fila(T("pdf_loan_a"), datos.get("prestamo_auto",0)),
            fila(T("pdf_debts"),  datos.get("deudas",0)),
        ]))
        story.append(Paragraph(T("pdf_auto"), h2))
        story.append(tabla([
            fila(T("pdf_gas"),       datos.get("gasolina",0)),
            fila(T("pdf_maint"),     datos.get("mantenimiento_auto",0)),
            fila(T("pdf_pet_food"),  datos.get("mascota_comida",0)),
            fila(T("pdf_pet_vet"),   datos.get("mascota_vet",0)),
            fila(T("pdf_pet_other"), datos.get("mascota_otros",0)),
        ]))
        story.append(Paragraph(T("pdf_vars"), h2))
        story.append(tabla([
            fila(T("pdf_grocery"), datos.get("comida",0)),
            fila(T("pdf_out"),     datos.get("salidas",0)),
            fila("Delivery",       datos.get("delivery",0)),
            fila("Apple One",      datos.get("apple_one",0)),
            fila("Netflix",        datos.get("netflix",0)),
            fila("HBO Max",        datos.get("hbo",0)),
            fila("Disney+",        datos.get("disney",0)),
        ]))
        ge = [fila(T("p7_extra_lbl", desc=g["desc"]), g["monto"])
              for g in datos.get("gastos_extra",[]) if g["monto"]>0]
        if ge:
            story.append(Paragraph(T("pdf_extras"), h2))
            story.append(tabla(ge))

        col_ah = C_VERDE if datos["ahorro_mensual"]>=0 else C_ROJO
        story.append(Paragraph(T("pdf_summary"), h2))
        story.append(tabla([
            fila(T("pdf_tot_inc"), datos["total_ingresos"],         C_VERDE, True),
            fila(T("pdf_tot_exp"), datos["total_gastos"],           C_ROJO,  True),
            fila(T("pdf_saving"),  abs(datos["ahorro_mensual"]),    col_ah,  True),
        ]))

        meses_r = datos["meses_restantes"]
        nec_mes = datos["meta"]/meses_r if meses_r>0 else 0
        proyecc = max(datos["ahorro_mensual"],0)*meses_r
        story.append(Paragraph(T("pdf_analysis"), h2))
        story.append(tabla([
            [Paragraph(T("pdf_goal_amt"), norm),
             Paragraph(f'<font color="#107c10"><b>{f_amt(datos["meta"])}</b></font>', der)],
            [Paragraph(T("pdf_objective", mes=mes_n, anio=datos["anio_meta"]), norm),
             Paragraph(f'<b>{T("pdf_months_left",n=meses_r)}</b>', der)],
            [Paragraph(T("pdf_need_mo"), norm),
             Paragraph(f'<font color="#ca5010"><b>{f_amt(nec_mes)}</b></font>', der)],
            [Paragraph(T("pdf_curr_mo"), norm),
             Paragraph(f'<font color="{"#107c10" if datos["ahorro_mensual"]>=0 else "#d13438"}"><b>{f_amt(datos["ahorro_mensual"])}</b></font>', der)],
            [Paragraph(T("pdf_projection"), norm),
             Paragraph(f'<font color="#0067c0"><b>{f_amt(proyecc)}</b></font>', der)],
        ]))

        story.append(Spacer(1,14))
        if datos["ahorro_mensual"]<=0:
            msg=T("pdf_alert"); clr="#d13438"
        elif proyecc>=datos["meta"]:
            msg=T("pdf_ok",mes=mes_n,anio=datos["anio_meta"]); clr="#107c10"
        else:
            msg=T("pdf_warn",sym=sym,n=nec_mes-datos["ahorro_mensual"]); clr="#ca5010"
        story.append(Paragraph(f'<font color="{clr}"><b>{msg}</b></font>',
            ParagraphStyle("concl",fontSize=11,spaceAfter=6,leading=16)))
        story.append(HRFlowable(width="100%",thickness=1,color=C_BORDE))
        story.append(Paragraph(T("pdf_footer",nombre=nombre,pais=pais),
            ParagraphStyle("foot",fontSize=8,textColor=colors.grey,
                           alignment=TA_CENTER,spaceBefore=8)))
        doc.build(story)
        return True
    except Exception as e:
        messagebox.showerror("Error PDF", str(e))
        return False

# ══════════════════════════════════════════════════════════
#  MAIN APP
# ══════════════════════════════════════════════════════════

class CalcApp(tk.Tk):
    def __init__(self):
        global _APP_REF
        super().__init__()
        _APP_REF = self
        self.withdraw()
        self.title(T("app_title"))
        self.configure(bg=W11["bg"])
        self.geometry("900x720")
        self.minsize(800, 600)
        self._step  = 0
        self._datos = {}
        self._fields= {}
        self._chrome_built = False
        SplashScreen(self, self._after_splash)

    def _after_splash(self):
        self.deiconify()
        self._build_chrome()
        self._show_step(0)

    # ── Chrome ───────────────────────────────────────────
    def _build_chrome(self):
        self._tb = tk.Frame(self, bg=W11["title_bar"], height=50)
        self._tb.pack(fill="x"); self._tb.pack_propagate(False)

        self._title_lbl = tk.Label(self._tb, text=T("title_bar"),
                 font=(FONT,11,"bold"), bg=W11["title_bar"], fg="white")
        self._title_lbl.pack(side="left", padx=8)

        # Right-side toolbar
        bar = tk.Frame(self._tb, bg=W11["title_bar"])
        bar.pack(side="right", padx=10)

        # Dark/Light toggle
        self._dark_btn = tk.Button(bar, text=T("dark_mode"), font=(FONT,9),
            bg="#334155", fg="white", relief="flat", padx=8, pady=4,
            cursor="hand2", command=self._toggle_dark)
        self._dark_btn.pack(side="left", padx=3)

        # Save / Load session
        tk.Button(bar, text=T("save_session"), font=(FONT,9),
            bg="#1e3a5f", fg="white", relief="flat", padx=8, pady=4,
            cursor="hand2", command=self._save_session_dialog
            ).pack(side="left", padx=3)

        tk.Button(bar, text=T("load_session"), font=(FONT,9),
            bg="#1e3a5f", fg="white", relief="flat", padx=8, pady=4,
            cursor="hand2", command=self._load_session_dialog
            ).pack(side="left", padx=3)

        # Language
        self._btn_es = tk.Button(bar, text="🇪🇸 ES", font=(FONT,9,"bold"),
            bg="#334155", fg="white", relief="flat", padx=7, pady=4,
            cursor="hand2", command=lambda: self._change_lang("es"))
        self._btn_es.pack(side="left", padx=2)

        self._btn_en = tk.Button(bar, text="🇺🇸 EN", font=(FONT,9,"bold"),
            bg="#334155", fg="white", relief="flat", padx=7, pady=4,
            cursor="hand2", command=lambda: self._change_lang("en"))
        self._btn_en.pack(side="left", padx=2)

        self._update_lang_btns()

        self.stepbar = StepBar(self)
        self.stepbar.pack(fill="x")
        self._sep = tk.Frame(self, bg=W11["border"], height=1)
        self._sep.pack(fill="x")

        self.content = tk.Frame(self, bg=W11["bg"])
        self.content.pack(fill="both", expand=True)

        self._nav = tk.Frame(self, bg=W11["surface"],
                       highlightbackground=W11["border"], highlightthickness=1, height=60)
        self._nav.pack(fill="x", side="bottom"); self._nav.pack_propagate(False)

        self.btn_back = W11Button(self._nav, text=T("back"), primary=False,
                                  command=self._prev_step)
        self.btn_back.pack(side="left", padx=20, pady=10)

        self.lbl_step = tk.Label(self._nav, text=T("step_of", s=1, t=8),
                                 font=F_SMALL, bg=W11["surface"], fg=W11["text2"])
        self.lbl_step.pack(side="left", expand=True)

        self.btn_next = W11Button(self._nav, text=T("next"), primary=True,
                                  command=self._next_step)
        self.btn_next.pack(side="right", padx=20, pady=10)
        self._chrome_built = True

    def _apply_theme_to_chrome(self):
        if not self._chrome_built: return
        self.configure(bg=W11["bg"])
        self._tb.config(bg=W11["title_bar"])
        self._title_lbl.config(bg=W11["title_bar"], fg="white")
        for w in self._tb.winfo_children():
            if isinstance(w, tk.Frame):
                w.config(bg=W11["title_bar"])
                for b in w.winfo_children():
                    if isinstance(b, tk.Button):
                        b.config(bg="#334155" if not b == self._dark_btn else "#334155")
        self._sep.config(bg=W11["border"])
        self.content.config(bg=W11["bg"])
        self._nav.config(bg=W11["surface"], highlightbackground=W11["border"])
        self.lbl_step.config(bg=W11["surface"], fg=W11["text2"])

    def _toggle_dark(self):
        toggle_dark()

    def _update_lang_btns(self):
        if not self._chrome_built: return
        self._btn_es.config(bg="#0067c0" if _LANG=="es" else "#334155")
        self._btn_en.config(bg="#0067c0" if _LANG=="en" else "#334155")

    def _change_lang(self, lang):
        set_lang(lang)
        if not self._chrome_built: return
        self._update_lang_btns()
        self.title(T("app_title"))
        self._title_lbl.config(text=T("title_bar"))
        self._dark_btn.config(text=T("light_mode") if _DARK_MODE else T("dark_mode"))
        self.stepbar.update_step(self._step)
        self._refresh_nav()
        self._clear_content()
        self._dispatch_step(self._step)

    def _refresh_nav(self):
        self.lbl_step.config(text=T("step_of", s=self._step+1, t=8))
        self.btn_back.config(text=T("back"))
        is_last = (self._step == 7)
        if is_last:
            self.btn_next.config(text=T("new_query"))
        else:
            self.btn_next.config(text=T("next"))

    def _clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()

    def _scrollable(self):
        canvas = tk.Canvas(self.content, bg=W11["bg"], highlightthickness=0)
        sb = ttk.Scrollbar(self.content, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        frame = tk.Frame(canvas, bg=W11["bg"])
        wid   = canvas.create_window((0,0), window=frame, anchor="nw")
        frame.bind("<Configure>",  lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(wid, width=e.width))
        canvas.bind_all("<MouseWheel>",
            lambda e: canvas.yview_scroll(-1*(e.delta//120),"units"))
        return frame

    # ── Navigation ───────────────────────────────────────
    def _dispatch_step(self, step):
        builders = [
            self._step_perfil, self._step_meta, self._step_ingresos,
            self._step_hogar,  self._step_deudas_auto, self._step_ocio,
            self._step_extras, self._step_resultado,
        ]
        builders[step]()

    def _show_step(self, step):
        self._step = step
        self._clear_content()
        self.stepbar.update_step(step)
        self.lbl_step.config(text=T("step_of", s=step+1, t=8))
        self.btn_back.config(state="normal" if step > 0 else "disabled",
                             text=T("back"))
        is_last = (step == 7)
        if is_last:
            self.btn_next.config(text=T("new_query"), command=self._reset, state="normal")
            self.btn_next._bg  = W11["btn_sec"]
            self.btn_next._abg = W11["border2"]
            self.btn_next.config(bg=W11["btn_sec"], fg=W11["btn_sec_fg"],
                                 activebackground=W11["border2"])
        else:
            self.btn_next.config(text=T("next"), command=self._next_step, state="normal")
            self.btn_next._bg  = W11["btn_bg"]
            self.btn_next._abg = W11["accent_h"]
            self.btn_next.config(bg=W11["btn_bg"], fg=W11["btn_fg"],
                                 activebackground=W11["accent_h"])
        self._dispatch_step(step)

    def _next_step(self):
        validators = {0: self._validate_perfil, 1: self._validate_meta,
                      2: self._validate_ingresos}
        if self._step in validators:
            if not validators[self._step](): return
        self._save_step(self._step)
        self._show_step(self._step + 1)

    def _prev_step(self):
        self._save_step(self._step)
        self._show_step(self._step - 1)

    def _save_step(self, step):
        f = self._fields
        if step == 0:
            self._datos["nombre"] = f.get("nombre","").get() if "nombre" in f else ""
            self._datos["pais"]   = f.get("pais","").get()   if "pais"   in f else "Panamá"
        elif step == 1:
            months = get_months()
            try:
                self._datos["meta"]      = max(0.0, float(f["meta"].get().replace(",",".")))
                self._datos["mes_num"]   = months.index(f["mes"].get()) + 1
                self._datos["anio_meta"] = int(f["anio"].get())
            except: pass
        elif step == 2:
            self._datos["salario"]       = val(f["salario"])
            self._datos["salario_real"]  = val(f["salario_real"]) if "salario_real" in f else 0
            self._datos["ingreso_extra"] = val(f["ingreso_extra"])
        elif step == 3:
            for k in ["alquiler","internet","luz","agua","data_movil"]:
                self._datos[k] = val(f[k])
        elif step == 4:
            for k in ["prestamo_personal","prestamo_auto","deudas",
                      "gasolina","mantenimiento_auto",
                      "mascota_comida","mascota_vet","mascota_otros"]:
                self._datos[k] = val(f[k])
        elif step == 5:
            for k in ["comida","salidas","delivery","apple_one","netflix","hbo","disney"]:
                self._datos[k] = val(f[k])
        elif step == 6:
            extras = []
            for i in range(3):
                m = val(f[f"extra_m_{i}"])
                d = f[f"extra_d_{i}"].get().strip() or T("p6_extra", n=i+1)
                extras.append({"monto": m, "desc": d})
            self._datos["gastos_extra"] = extras

    # ── Validators ───────────────────────────────────────
    def _validate_perfil(self):
        if not self._fields.get("nombre") or not self._fields["nombre"].get().strip():
            messagebox.showwarning(T("req_field"), T("req_name")); return False
        return True

    def _validate_meta(self):
        try:
            m = float(self._fields["meta"].get().replace(",",".")); assert m > 0
        except:
            messagebox.showwarning(T("req_field"), T("req_meta")); return False
        try:
            int(self._fields["anio"].get())
        except:
            messagebox.showwarning(T("invalid_year"), T("req_anio")); return False
        return True

    def _validate_ingresos(self):
        try:
            s = float(self._fields["salario"].get().replace(",",".")); assert s > 0
        except:
            messagebox.showwarning(T("req_field"), T("req_salary")); return False
        return True

    # ── Session management ───────────────────────────────
    def _save_session_dialog(self):
        self._save_step(self._step)
        popup = tk.Toplevel(self)
        popup.title(T("save_session"))
        popup.configure(bg=W11["surface"])
        popup.geometry("360x160")
        popup.transient(self); popup.grab_set()
        sw, sh = popup.winfo_screenwidth(), popup.winfo_screenheight()
        popup.geometry(f"360x160+{(sw-360)//2}+{(sh-160)//2}")

        tk.Label(popup, text=T("save_name_prompt"), font=F_BODY,
                 bg=W11["surface"], fg=W11["text"]).pack(padx=20, pady=(20,4), anchor="w")
        name_var = tk.StringVar(value=self._datos.get("nombre","Mi Sesión"))
        entry = tk.Entry(popup, textvariable=name_var, font=F_INPUT,
                         bg=W11["input_bg"], fg=W11["text"], relief="flat",
                         insertbackground=W11["accent"])
        entry.pack(padx=20, fill="x", pady=4)
        entry.select_range(0,"end"); entry.focus()

        def do_save():
            name = name_var.get().strip()
            if not name: return
            sessions = load_sessions()
            sessions[name] = {"data": self._datos, "lang": _LANG,
                              "dark": _DARK_MODE, "step": self._step,
                              "saved_at": date.today().isoformat()}
            if save_sessions(sessions):
                popup.destroy()
                messagebox.showinfo("✅", T("save_success", name=name))
            else:
                messagebox.showerror("Error", T("save_error"))

        btn_f = tk.Frame(popup, bg=W11["surface"])
        btn_f.pack(fill="x", padx=20, pady=12)
        W11Button(btn_f, text=T("ok"), primary=True, command=do_save).pack(side="right", padx=4)
        W11Button(btn_f, text=T("cancel"), primary=False, command=popup.destroy).pack(side="right", padx=4)

    def _load_session_dialog(self):
        sessions = load_sessions()
        popup = tk.Toplevel(self)
        popup.title(T("load_session"))
        popup.configure(bg=W11["surface"])
        popup.geometry("440x360")
        popup.transient(self); popup.grab_set()
        sw, sh = popup.winfo_screenwidth(), popup.winfo_screenheight()
        popup.geometry(f"440x360+{(sw-440)//2}+{(sh-360)//2}")

        tk.Label(popup, text=T("load_select") if sessions else T("load_none"),
                 font=F_BODY, bg=W11["surface"], fg=W11["text"]
                 ).pack(padx=20, pady=(16,8), anchor="w")

        frame = tk.Frame(popup, bg=W11["surface"])
        frame.pack(fill="both", expand=True, padx=20)

        if not sessions:
            W11Button(popup, text=T("cancel"), primary=False,
                      command=popup.destroy).pack(pady=16)
            return

        selected = tk.StringVar(value=list(sessions.keys())[0])

        sb = ttk.Scrollbar(frame, orient="vertical")
        lb = tk.Listbox(frame, font=F_BODY, bg=W11["input_bg"], fg=W11["text"],
                        selectbackground=W11["accent"], selectforeground="white",
                        relief="flat", bd=1, highlightthickness=0,
                        yscrollcommand=sb.set)
        sb.config(command=lb.yview)
        lb.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        for name, meta in sessions.items():
            saved = meta.get("saved_at","")
            lb.insert("end", f"  {name}  ({saved})")

        def do_load():
            sel = lb.curselection()
            if not sel: return
            name = list(sessions.keys())[sel[0]]
            s = sessions[name]
            self._datos = dict(s.get("data", {}))
            popup.destroy()
            messagebox.showinfo("✅", T("load_success", name=name))
            self._show_step(0)

        def do_delete():
            sel = lb.curselection()
            if not sel: return
            name = list(sessions.keys())[sel[0]]
            sessions.pop(name, None)
            save_sessions(sessions)
            lb.delete(sel[0])

        lb.selection_set(0)
        btn_f = tk.Frame(popup, bg=W11["surface"])
        btn_f.pack(fill="x", padx=20, pady=12)
        W11Button(btn_f, text=T("ok"), primary=True, command=do_load).pack(side="right", padx=4)
        W11Button(btn_f, text=T("delete_session"), primary=False,
                  command=do_delete).pack(side="right", padx=4)
        W11Button(btn_f, text=T("cancel"), primary=False,
                  command=popup.destroy).pack(side="right", padx=4)

    # ── Page title ───────────────────────────────────────
    def _page_title(self, parent, title, subtitle=""):
        hdr = tk.Frame(parent, bg=W11["bg"])
        hdr.pack(fill="x", padx=28, pady=(20,4))
        tk.Label(hdr, text=title, font=F_TITLE,
                 bg=W11["bg"], fg=W11["text"]).pack(anchor="w")
        if subtitle:
            tk.Label(hdr, text=subtitle, font=F_BODY,
                     bg=W11["bg"], fg=W11["text2"]).pack(anchor="w", pady=(2,0))
        tk.Frame(parent, bg=W11["border"], height=1).pack(fill="x", padx=28, pady=(8,16))

    # ════════════════════════════════════════════════════
    #  STEP 0 — PROFILE
    # ════════════════════════════════════════════════════
    def _step_perfil(self):
        self._fields = {}
        f = self._scrollable()
        self._page_title(f, T("p0_title"), T("p0_sub"))
        c = card(f)
        section_title(c, T("p0_section"), "🪪")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=14, pady=(0,14))
        g.columnconfigure(0, weight=1); g.columnconfigure(1, weight=1)

        nom = W11Entry(g, label=T("p0_name"), prefix="")
        nom.grid(row=0, column=0, sticky="ew", padx=(0,10), pady=4)
        nom.set(self._datos.get("nombre",""))
        self._fields["nombre"] = nom

        pais_list = [f"{PAISES[p]['flag']} {p}" for p in PAISES]
        pais_w = W11Combo(g, label=T("p0_country"), values=pais_list, width=22)
        saved_pais = self._datos.get("pais","Panamá")
        # Find matching option
        match = next((o for o in pais_list if saved_pais in o), pais_list[0])
        pais_w.set(match)
        pais_w.grid(row=0, column=1, sticky="ew", pady=4)
        self._fields["pais"] = pais_w

        note_box(c, T("p0_note"), W11["note_bg"], W11["note_border"])

    # ════════════════════════════════════════════════════
    #  STEP 1 — GOAL
    # ════════════════════════════════════════════════════
    def _step_meta(self):
        f = self._scrollable()
        self._page_title(f, T("p1_title"), T("p1_sub"))
        pais = self._datos.get("pais","Panamá")
        sym  = get_sym(pais)
        c = card(f)
        section_title(c, T("p1_section"), "📅")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=14, pady=(0,14))
        g.columnconfigure(0,weight=2); g.columnconfigure(1,weight=1); g.columnconfigure(2,weight=1)

        meta_w = W11Entry(g, label=T("p1_meta"), prefix=sym)
        meta_w.grid(row=0, column=0, sticky="ew", padx=(0,10), pady=4)
        meta_w.set(str(self._datos.get("meta","")))
        self._fields["meta"] = meta_w

        months = get_months()
        mes_w = W11Combo(g, label=T("p1_month"), values=months, width=14)
        mes_w.set(months[self._datos.get("mes_num",11)-1])
        mes_w.grid(row=0, column=1, sticky="ew", padx=(0,10), pady=4)
        self._fields["mes"] = mes_w

        anio_w = W11Entry(g, label=T("p1_year"), prefix="")
        anio_w.grid(row=0, column=2, sticky="ew", pady=4)
        anio_w.set(str(self._datos.get("anio_meta","2026")))
        self._fields["anio"] = anio_w

        tip = card(f, pady=0); tip.config(bg=W11["surface2"])
        tk.Label(tip, text=T("p1_tip"), font=F_SMALL, bg=W11["surface2"],
                 fg=W11["text2"], wraplength=720, justify="left"
                 ).pack(padx=16, pady=14, anchor="w")

    # ════════════════════════════════════════════════════
    #  STEP 2 — INCOME
    # ════════════════════════════════════════════════════
    def _step_ingresos(self):
        f = self._scrollable()
        pais   = self._datos.get("pais","Panamá")
        nombre = self._datos.get("nombre","")
        sym    = get_sym(pais)
        cfg    = PAISES.get(pais, PAISES["Panamá"])
        moneda = cfg["moneda"]
        self._page_title(f, T("p2_title", nombre=nombre),
                            T("p2_sub", pais=pais))
        c = card(f)
        section_title(c, T("p2_section"), "🧾")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=14, pady=(0,4))
        g.columnconfigure(0, weight=1); g.columnconfigure(1, weight=1)

        sal_w = W11Entry(g, label=f"{T('p2_gross')} ({moneda})", prefix=sym)
        sal_w.grid(row=0, column=0, sticky="ew", padx=(0,10), pady=4)
        sal_w.set(str(self._datos.get("salario","")))
        self._fields["salario"] = sal_w

        ext_w = W11Entry(g, label=f"{T('p2_extra')} ({moneda})", prefix=sym)
        ext_w.grid(row=0, column=1, sticky="ew", pady=4)
        ext_w.set(str(self._datos.get("ingreso_extra","")))
        self._fields["ingreso_extra"] = ext_w

        self.imp_frame = tk.Frame(c, bg=W11["surface2"],
                                  highlightbackground=W11["border"], highlightthickness=1)
        self.imp_frame.pack(fill="x", padx=14, pady=(4,4))
        self._imp_title = tk.Label(self.imp_frame, text=T("p2_imp_hint"),
                                   font=F_SMALL, bg=W11["surface2"], fg=W11["text2"])
        self._imp_title.pack(padx=12, pady=8, anchor="w")
        self._imp_rows_frame = tk.Frame(self.imp_frame, bg=W11["surface2"])
        self._imp_rows_frame.pack(fill="x", padx=12, pady=(0,8))
        sal_w.entry.bind("<KeyRelease>", lambda e: self._preview_imp())
        self._preview_imp()

        note_box(c, T("p2_note"), W11["note_bg"], W11["note_border"])

        g2 = tk.Frame(c, bg=W11["surface"])
        g2.pack(fill="x", padx=14, pady=(4,14))
        g2.columnconfigure(0, weight=1); g2.columnconfigure(1, weight=1)

        real_w = W11Entry(g2, label=f"{T('p2_real')} ({moneda})", prefix=sym)
        real_w.grid(row=0, column=0, sticky="ew", padx=(0,10), pady=4)
        real_w.set(str(self._datos.get("salario_real","")))
        self._fields["salario_real"] = real_w

        tk.Label(g2, text=T("p2_real_tip"), font=F_SMALL,
                 bg=W11["surface"], fg=W11["text3"], justify="left"
                 ).grid(row=0, column=1, sticky="w", pady=4)

    def _preview_imp(self):
        for w in self._imp_rows_frame.winfo_children():
            w.destroy()
        try:
            s = float(self._fields["salario"].get().replace(",",".")); assert s > 0
        except:
            return
        pais = self._datos.get("pais","Panamá")
        cfg  = PAISES.get(pais, PAISES["Panamá"])
        sym  = cfg["simbolo"]
        f_v  = (lambda v: f"{sym}{v:,.0f}") if pais=="Colombia" else (lambda v: f"{sym}{v:,.2f}")
        imp  = cfg["calcular"](s)
        self._imp_title.config(text=T("p2_imp_title", pais=pais),
                               fg=W11["text"], font=(FONT,9,"bold"))
        for nd, md in imp["detalle"]:
            row = tk.Frame(self._imp_rows_frame, bg=W11["surface2"])
            row.pack(fill="x", pady=1)
            tk.Label(row, text=f"  {nd}", font=F_SMALL,
                     bg=W11["surface2"], fg=W11["text2"]).pack(side="left")
            tk.Label(row, text=f"-{f_v(md)}", font=(FONT,9,"bold"),
                     bg=W11["surface2"], fg=W11["danger"]).pack(side="right")
        tk.Frame(self._imp_rows_frame, bg=W11["border"], height=1).pack(fill="x", pady=4)
        row_n = tk.Frame(self._imp_rows_frame, bg=W11["surface2"])
        row_n.pack(fill="x")
        tk.Label(row_n, text=T("p2_net_est"), font=(FONT,10,"bold"),
                 bg=W11["surface2"], fg=W11["text"]).pack(side="left")
        tk.Label(row_n, text=f_v(imp["salario_neto"]), font=(FONT,12,"bold"),
                 bg=W11["surface2"], fg=W11["success"]).pack(side="right")

    # ════════════════════════════════════════════════════
    #  STEP 3 — HOME
    # ════════════════════════════════════════════════════
    def _step_hogar(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p3_title"), T("p3_sub"))
        c = card(f)
        section_title(c, T("p3_section"), "📋")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=14, pady=(0,14))
        g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
        for i,(k,lk) in enumerate([("alquiler","p3_rent"),("internet","p3_internet"),
                                    ("luz","p3_electric"),("agua","p3_water"),
                                    ("data_movil","p3_mobile")]):
            w = W11Entry(g, label=f"{T(lk)}", prefix=sym)
            w.grid(row=i//2, column=i%2, sticky="ew",
                   padx=(0,10) if i%2==0 else 0, pady=4)
            w.set(str(self._datos.get(k,""))); self._fields[k] = w

    # ════════════════════════════════════════════════════
    #  STEP 4 — DEBTS / CAR / PETS
    # ════════════════════════════════════════════════════
    def _step_deudas_auto(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p4_title"), T("p4_sub"))
        for sec, icon, campos in [
            (T("p4_s1"), "💳", [("prestamo_personal","p4_loan_p"),
                                ("prestamo_auto","p4_loan_a"),("deudas","p4_debts")]),
            (T("p4_s2"), "🚗", [("gasolina","p4_gas"),("mantenimiento_auto","p4_maint")]),
            (T("p4_s3"), "🐾", [("mascota_comida","p4_pet_food"),
                                ("mascota_vet","p4_pet_vet"),("mascota_otros","p4_pet_other")]),
        ]:
            c = card(f, pady=8)
            section_title(c, sec, icon)
            g = tk.Frame(c, bg=W11["surface"])
            g.pack(fill="x", padx=14, pady=(0,10))
            g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
            for i,(k,lk) in enumerate(campos):
                w = W11Entry(g, label=T(lk), prefix=sym)
                w.grid(row=i//2, column=i%2, sticky="ew",
                       padx=(0,10) if i%2==0 else 0, pady=4)
                w.set(str(self._datos.get(k,""))); self._fields[k] = w

    # ════════════════════════════════════════════════════
    #  STEP 5 — LEISURE
    # ════════════════════════════════════════════════════
    def _step_ocio(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p5_title"), T("p5_sub"))
        for sec, icon, campos in [
            (T("p5_s1"), "🛒", [("comida","p5_grocery"),("salidas","p5_out"),
                                ("delivery","p5_delivery")]),
            (T("p5_s2"), "📱", [("apple_one","Apple One"),("netflix","Netflix"),
                                ("hbo","HBO Max"),("disney","Disney+")]),
        ]:
            c = card(f, pady=8)
            section_title(c, sec, icon)
            g = tk.Frame(c, bg=W11["surface"])
            g.pack(fill="x", padx=14, pady=(0,10))
            g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
            for i,(k,lk) in enumerate(campos):
                lbl = T(lk) if lk in LANGS["es"] else lk
                w = W11Entry(g, label=lbl, prefix=sym)
                w.grid(row=i//2, column=i%2, sticky="ew",
                       padx=(0,10) if i%2==0 else 0, pady=4)
                w.set(str(self._datos.get(k,""))); self._fields[k] = w

    # ════════════════════════════════════════════════════
    #  STEP 6 — EXTRAS
    # ════════════════════════════════════════════════════
    def _step_extras(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p6_title"), T("p6_sub"))
        c = card(f)
        section_title(c, T("p6_section"), "📝")
        extras = self._datos.get("gastos_extra",
                                 [{"monto":0,"desc":""},{"monto":0,"desc":""},{"monto":0,"desc":""}])
        for i in range(3):
            row = tk.Frame(c, bg=W11["surface"])
            row.pack(fill="x", padx=14, pady=4)
            row.columnconfigure(0,weight=1); row.columnconfigure(1,weight=2)
            mw = W11Entry(row, label=T("p6_extra", n=i+1), prefix=sym)
            mw.grid(row=0, column=0, sticky="ew", padx=(0,12))
            mw.set(str(extras[i]["monto"]) if extras[i]["monto"] else "")
            self._fields[f"extra_m_{i}"] = mw
            dw = W11Entry(row, label=T("p6_desc"), prefix="")
            dw.grid(row=0, column=1, sticky="ew")
            dw.set(extras[i]["desc"]); self._fields[f"extra_d_{i}"] = dw

        tk.Frame(c, bg=W11["border"], height=1).pack(fill="x", padx=14, pady=12)
        tk.Label(c, text=T("p6_hint"), font=F_SMALL, bg=W11["surface"],
                 fg=W11["text2"]).pack(padx=14, pady=(0,14), anchor="w")

    # ════════════════════════════════════════════════════
    #  STEP 7 — RESULTS
    # ════════════════════════════════════════════════════
    def _step_resultado(self):
        self._save_step(6)
        d    = self._datos
        pais = d.get("pais","Panamá")
        cfg  = PAISES.get(pais, PAISES["Panamá"])
        sym  = cfg["simbolo"]
        imp  = cfg["calcular"](d.get("salario",0))
        d["impuestos"] = imp

        sal_real = d.get("salario_real", 0)
        sal_base = sal_real if sal_real > 0 else imp["salario_neto"]
        d["salario_neto"]   = sal_base
        d["total_ingresos"] = sal_base + d.get("ingreso_extra", 0)

        total_g = sum(d.get(k,0) for k in [
            "alquiler","internet","luz","agua","data_movil",
            "prestamo_personal","prestamo_auto","deudas",
            "gasolina","mantenimiento_auto",
            "mascota_comida","mascota_vet","mascota_otros",
            "comida","salidas","delivery",
            "apple_one","netflix","hbo","disney",
        ]) + sum(g["monto"] for g in d.get("gastos_extra",[]))
        d["total_gastos"]   = total_g
        d["ahorro_mensual"] = d["total_ingresos"] - total_g

        meses_r = calcular_meses(d.get("anio_meta",2026), d.get("mes_num",11))
        d["meses_restantes"] = meses_r
        meta    = d.get("meta",0)
        nec_mes = meta / meses_r if meses_r > 0 else 0
        proyecc = max(d["ahorro_mensual"],0) * meses_r
        ahorro  = d["ahorro_mensual"]
        months  = get_months()
        mes_n   = months[d.get("mes_num",11)-1]
        f_v     = (lambda v: f"{sym}{v:,.0f}") if pais=="Colombia" else (lambda v: f"{sym}{v:,.2f}")

        f = self._scrollable()
        self._page_title(f,
            T("p7_title", nombre=d.get("nombre","")),
            T("p7_sub", pais=pais, sym=sym, meta=meta, mes=mes_n, anio=d.get("anio_meta",2026)))

        # Banner
        col_b = W11["success"] if ahorro >= 0 else W11["danger"]
        banner = tk.Frame(f, bg=col_b)
        banner.pack(fill="x", padx=28, pady=(0,10))
        if ahorro <= 0:
            bmsg = T("p7_deficit", sym=sym, amt=abs(ahorro))
        elif proyecc >= meta:
            bmsg = T("p7_ontrack", sym=sym, amt=ahorro, mes=mes_n, anio=d.get("anio_meta",2026))
        else:
            bmsg = T("p7_need", sym=sym, amt=ahorro, falta=nec_mes-ahorro)
        tk.Label(banner, text=bmsg, font=F_SUBH, bg=col_b, fg="white",
                 wraplength=760, justify="left", padx=16, pady=12).pack(anchor="w")

        T_=W11["text"]; T2=W11["text2"]; SU=W11["success"]; DA=W11["danger"]
        WA=W11["warning"]; AC=W11["accent"]

        def res_card(parent, title, rows):
            c = card(parent, pady=6)
            section_title(c, title)
            for lbl, amt, col in rows:
                if amt == 0: continue
                row = tk.Frame(c, bg=W11["surface"])
                row.pack(fill="x", padx=14, pady=1)
                tk.Label(row, text=lbl, font=F_BODY,
                         bg=W11["surface"], fg=T2).pack(side="left")
                tk.Label(row, text=f_v(amt), font=(FONT,10,"bold"),
                         bg=W11["surface"], fg=col).pack(side="right")
            tk.Frame(c, bg=W11["border"], height=1).pack(fill="x", padx=14, pady=(6,4))

        # Salary & taxes
        imp_rows = [(n, m, DA) for n,m in imp["detalle"]]
        imp_rows += [(T("p7_total_ded"), imp["total_imp"], DA)]
        if sal_real > 0:
            imp_rows += [(T("p7_net_est"), imp["salario_neto"], AC),
                         (T("p7_net_real"), sal_real, SU)]
        else:
            imp_rows += [(T("p7_net_est"), imp["salario_neto"], SU)]
        res_card(f, T("p7_salary_imp"), imp_rows)

        note_c = card(f, pady=4)
        note_c.config(bg=W11["note_bg"], highlightbackground=W11["note_border"])
        tk.Label(note_c, text=T("p7_imp_note"), font=F_SMALL,
                 bg=W11["note_bg"], fg=W11["gold"],
                 wraplength=720, justify="left").pack(padx=12, pady=8, anchor="w")

        res_card(f, T("p7_income"), [
            (T("p7_net_base"),  sal_base,                 T_),
            (T("p7_extra_inc"), d.get("ingreso_extra",0), AC),
            (T("p7_total_inc"), d["total_ingresos"],      SU),
        ])
        res_card(f, T("p7_home"), [
            (T("p7_rent"),     d.get("alquiler",0),   T2),
            ("Internet",       d.get("internet",0),   T2),
            (T("p7_electric"), d.get("luz",0),        T2),
            (T("p7_water"),    d.get("agua",0),       T2),
            (T("p7_mobile"),   d.get("data_movil",0), T2),
        ])
        res_card(f, T("p7_loans"), [
            (T("p7_loan_p"), d.get("prestamo_personal",0), T2),
            (T("p7_loan_a"), d.get("prestamo_auto",0),     T2),
            (T("p7_debts"),  d.get("deudas",0),            T2),
        ])
        res_card(f, T("p7_auto_pets"), [
            (T("p7_gas"),       d.get("gasolina",0),           T2),
            (T("p7_maint"),     d.get("mantenimiento_auto",0), T2),
            (T("p7_pet_food"),  d.get("mascota_comida",0),     T2),
            (T("p7_pet_vet"),   d.get("mascota_vet",0),        T2),
            (T("p7_pet_other"), d.get("mascota_otros",0),      T2),
        ])
        res_card(f, T("p7_vars"), [
            (T("p7_grocery"), d.get("comida",0),    T2),
            (T("p7_out"),     d.get("salidas",0),   T2),
            ("Delivery",      d.get("delivery",0),  T2),
            ("Apple One",     d.get("apple_one",0), T2),
            ("Netflix",       d.get("netflix",0),   T2),
            ("HBO Max",       d.get("hbo",0),       T2),
            ("Disney+",       d.get("disney",0),    T2),
        ])
        ge = [(T("p7_extra_lbl", desc=g["desc"]), g["monto"], T2)
              for g in d.get("gastos_extra",[]) if g["monto"]>0]
        if ge: res_card(f, T("p7_extras_sec"), ge)

        res_card(f, T("p7_summary"), [
            (T("p7_tot_inc"), d["total_ingresos"], SU),
            (T("p7_tot_exp"), d["total_gastos"],   DA),
            (T("p7_saving"),  abs(ahorro), SU if ahorro>=0 else DA),
        ])

        meta_c = card(f, pady=6)
        section_title(meta_c, T("p7_goal"))
        for lbl, val_s, col in [
            (T("p7_goal_amt"),   f_v(meta),    SU),
            (T("p7_months_left"),str(meses_r), T_),
            (T("p7_need_mo"),    f_v(nec_mes), WA),
            (T("p7_curr_mo"),    f_v(ahorro),  SU if ahorro>=0 else DA),
            (T("p7_projection"), f_v(proyecc), AC),
        ]:
            row = tk.Frame(meta_c, bg=W11["surface"])
            row.pack(fill="x", padx=14, pady=2)
            tk.Label(row, text=lbl, font=F_BODY,
                     bg=W11["surface"], fg=T2).pack(side="left")
            tk.Label(row, text=val_s, font=(FONT,10,"bold"),
                     bg=W11["surface"], fg=col).pack(side="right")
        tk.Frame(meta_c, bg=W11["border"], height=1).pack(fill="x", padx=14, pady=(8,4))

        btn_row = tk.Frame(meta_c, bg=W11["surface"])
        btn_row.pack(fill="x", padx=14, pady=(4,14))

        def exportar():
            ruta = filedialog.asksaveasfilename(
                defaultextension=".pdf", filetypes=[("PDF","*.pdf")],
                initialfile=f"report_{d.get('nombre','').replace(' ','_')}.pdf",
                title=T("pdf_save_title"))
            if ruta:
                if generar_pdf(d, ruta):
                    messagebox.showinfo(T("pdf_saved"), T("pdf_saved_msg", ruta=ruta))

        W11Button(btn_row, text=T("p7_export"), primary=True,
                  command=exportar).pack(side="left", padx=(0,10))
        tk.Label(meta_c, text=T("p7_new"), font=F_SMALL,
                 bg=W11["surface"], fg=W11["text3"]
                 ).pack(padx=14, pady=(0,10), anchor="w")

    def _reset(self):
        self._datos  = {}
        self._fields = {}
        self._show_step(0)

# ══════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        # 1) Language boot screen
        boot = LanguageBootScreen()
        chosen_lang = boot.get_choice()
        set_lang(chosen_lang)

        # 2) Main app + splash
        app = CalcApp()
        app.mainloop()
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("\nError. Press Enter / Presiona Enter para cerrar...")
