# ============================================================
#  CALCULADORA DE SALARIO & METAS  —  Windows 11 Style GUI
#  by Erick Perez  |  v0.1 Panama Tax Only  |  BETA
#  Requiere: pip install reportlab
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import date
import os, sys, math

# ══════════════════════════════════════════════════════════
#  IDIOMAS — Todas las cadenas de texto
# ══════════════════════════════════════════════════════════

LANGS = {
    "es": {
        # General
        "app_title":        "Calculadora de Salario & Metas  —  by Erick Perez",
        "title_bar":        "  💰  Calculadora de Salario & Metas  —  by Erick Perez",
        "splash_sub":       "Calculadora de Salario & Metas",
        "splash_edition":   "v0.1 Panama Tax Only  •  BETA",
        "splash_loading":   ["Iniciando...", "Cargando interfaz...",
                             "Configurando impuestos Panamá...",
                             "Preparando calculadora...", "¡Listo!"],
        # Navegación
        "back":             "← Atrás",
        "next":             "Siguiente →",
        "new_query":        "🔄  Nueva Consulta",
        "step_of":          "Paso {s} de {t}",
        # Nombres de pasos
        "steps":            ["Perfil","Meta","Ingresos","Hogar",
                             "Deudas","Ocio","Extras","Resultado"],
        # Validaciones
        "req_name":         "Por favor ingresa tu nombre.",
        "req_field":        "Campo requerido",
        "req_meta":         "Ingresa una meta de ahorro válida.",
        "req_anio":         "Ingresa un año válido (ej: 2026).",
        "invalid_year":     "Año inválido",
        "req_salary":       "Ingresa tu salario mensual bruto.",
        # Paso 0 — Perfil
        "p0_title":         "👤  Tu Perfil",
        "p0_sub":           "Cuéntanos quién eres para personalizar tu reporte.",
        "p0_section":       "Información Personal",
        "p0_name":          "Tu nombre completo *",
        "p0_country":       "País de residencia *",
        "p0_note":          "⚠️  VERSIÓN BETA EN DESARROLLO — Actualmente solo disponible para Panamá (CSS 9.75% + Seg. Educativo 1.25% + ISR progresivo). Próximamente se agregarán más países. Los cálculos son estimados.",
        # Paso 1 — Meta
        "p1_title":         "🎯  Meta de Ahorro",
        "p1_sub":           "Define cuánto quieres ahorrar y para cuándo.",
        "p1_section":       "Tu Objetivo Financiero",
        "p1_meta":          "Meta de ahorro ($) *",
        "p1_month":         "Mes objetivo *",
        "p1_year":          "Año objetivo *",
        "p1_tip":           "💡  Un ahorro mensual constante, aunque sea pequeño, tiene un gran impacto a largo plazo. Sé realista con tu meta y celebra cada mes que la cumples.",
        # Paso 2 — Ingresos
        "p2_title":         "💵  Ingresos  —  {nombre}",
        "p2_sub":           "País: {pais}  |  Deducciones calculadas automáticamente.",
        "p2_section":       "Salario Mensual",
        "p2_gross":         "Salario mensual BRUTO ($) *",
        "p2_extra":         "Ingresos extra este mes ($)",
        "p2_imp_hint":      "🧮  Ingresa tu salario bruto para ver el desglose",
        "p2_imp_title":     "🧮  Desglose estimado de deducciones — {pais}",
        "p2_net_est":       "  Salario Neto Estimado:",
        "p2_note":          "⚠️  AVISO IMPORTANTE: El cálculo de impuestos mostrado arriba es un estimado basado en las tasas oficiales de Panamá. El monto real puede variar según deducciones adicionales, bonificaciones, ajustes de CSS o cambios de ley. Siempre consulta tu slip de pago oficial para conocer el monto real recibido.",
        "p2_real":          "Salario REAL recibido según tu slip de pago ($)  (si difiere del estimado arriba)",
        "p2_real_tip":      "💡  Si dejas este campo vacío,\nse usará el salario neto estimado.",
        # Paso 3 — Hogar
        "p3_title":         "🏠  Gastos del Hogar",
        "p3_sub":           "Servicios básicos y vivienda.",
        "p3_section":       "Gastos Fijos Mensuales",
        "p3_rent":          "Alquiler / Hipoteca ($)",
        "p3_internet":      "Internet ($)",
        "p3_electric":      "Luz / Electricidad ($)",
        "p3_water":         "Agua ($)",
        "p3_mobile":        "Data Móvil / Celular ($)",
        # Paso 4 — Deudas/Auto/Mascotas
        "p4_title":         "🏦  Deudas, Auto y Mascotas",
        "p4_sub":           "Préstamos, gastos de vehículo y cuidado de mascotas.",
        "p4_s1":            "Préstamos y Deudas",
        "p4_loan_p":        "Préstamo Personal ($)",
        "p4_loan_a":        "Préstamo de Auto ($)",
        "p4_debts":         "Otras Deudas ($)",
        "p4_s2":            "Gastos de Auto",
        "p4_gas":           "Gasolina ($)",
        "p4_maint":         "Mantenimiento ($)",
        "p4_s3":            "Gastos de Mascotas",
        "p4_pet_food":      "Comida mascotas ($)",
        "p4_pet_vet":       "Veterinario ($)",
        "p4_pet_other":     "Otros mascotas ($)",
        # Paso 5 — Ocio
        "p5_title":         "🎬  Ocio y Suscripciones",
        "p5_sub":           "Entretenimiento, comida y plataformas digitales.",
        "p5_s1":            "Gastos Variables",
        "p5_grocery":       "Supermercado / Comida ($)",
        "p5_out":           "Salidas / Entretenimiento ($)",
        "p5_delivery":      "Delivery ($)",
        "p5_s2":            "Suscripciones Digitales",
        # Paso 6 — Extras
        "p6_title":         "➕  Gastos Extra",
        "p6_sub":           "Cualquier gasto adicional que no encaje en las categorías anteriores.",
        "p6_section":       "Gastos Adicionales",
        "p6_extra":         "Gasto Extra {n} ($)",
        "p6_desc":          "Descripción",
        "p6_hint":          "✔  Al presionar 'Siguiente' se calcularán todos tus resultados.",
        # Paso 7 — Resultado
        "p7_title":         "📊  Resultados  —  {nombre}",
        "p7_sub":           "{pais}  •  Meta: ${meta:,.2f} para {mes} {anio}",
        "p7_deficit":       "⚠  Déficit de ${amt:,.2f}/mes  —  Tus gastos superan tus ingresos",
        "p7_ontrack":       "🎉  Ahorro de ${amt:,.2f}/mes  —  ¡Alcanzarás tu meta antes de {mes} {anio}!",
        "p7_need":          "💡  Ahorro de ${amt:,.2f}/mes  —  Necesitas ${falta:,.2f} más/mes para tu meta",
        "p7_salary_imp":    "🧾  Salario e Impuestos",
        "p7_total_ded":     "Total deducciones (estimado)",
        "p7_net_est":       "Salario Neto (estimado)",
        "p7_net_real":      "Salario Real (slip)",
        "p7_imp_note":      "⚠️  El cálculo de impuestos es estimado. Puede variar según deducciones adicionales, bonificaciones o ajustes de la CSS. Siempre verifica con tu slip de pago oficial.",
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
        "p7_new":           "💡  Usa el botón 'Nueva Consulta' en la barra inferior para comenzar de nuevo.",
        "pdf_saved":        "✅ PDF Generado",
        "pdf_saved_msg":    "Reporte guardado en:\n{ruta}",
        "pdf_save_title":   "Guardar reporte PDF",
        # Meses
        "months":           ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
                             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
        # Impuestos
        "tax_css":          "CSS (9.75%)",
        "tax_edu":          "Seguro Educativo (1.25%)",
        "tax_isr":          "ISR mensual estimado",
        # PDF
        "pdf_title":        "Calculadora de Salario & Metas",
        "pdf_by":           "by Erick Perez",
        "pdf_date":         "Generado el {d}",
        "pdf_goal_for":     "Meta: ${m:,.2f} para {mes} {anio}",
        "pdf_salary":       "Salario e Impuestos",
        "pdf_gross":        "Salario Bruto",
        "pdf_ded_est":      "Total Deducciones (estimado)",
        "pdf_net_est":      "Salario Neto Estimado",
        "pdf_net_real":     "Salario Real Recibido (slip)",
        "pdf_note":         "NOTA: El calculo de impuestos es estimado y puede variar. Verifica con tu slip de pago oficial.",
        "pdf_income":       "Ingresos Totales",
        "pdf_net_base":     "Salario Neto (base calculo)",
        "pdf_extra_inc":    "Ingreso Extra",
        "pdf_total_inc":    "TOTAL INGRESOS",
        "pdf_home":         "Gastos Fijos del Hogar",
        "pdf_rent":         "Alquiler / Hipoteca",
        "pdf_electric":     "Luz / Electricidad",
        "pdf_water":        "Agua",
        "pdf_mobile":       "Data Movil / Celular",
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
        "pdf_grocery":      "Supermercado / Comida",
        "pdf_out":          "Salidas / Entretenimiento",
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
        "pdf_warn":         "ATENCION: Necesitas ${n:,.2f} mas/mes para tu meta.",
        "pdf_alert":        "ALERTA: Tus gastos superan tus ingresos.",
        "pdf_footer":       "Calculadora de Salario & Metas  •  by Erick Perez  •  {nombre}  •  {pais}",
    },
    "en": {
        # General
        "app_title":        "Salary & Goals Calculator  —  by Erick Perez",
        "title_bar":        "  💰  Salary & Goals Calculator  —  by Erick Perez",
        "splash_sub":       "Salary & Goals Calculator",
        "splash_edition":   "v0.1 Panama Tax Only  •  BETA",
        "splash_loading":   ["Starting...", "Loading interface...",
                             "Setting up Panama taxes...",
                             "Preparing calculator...", "Ready!"],
        # Navegación
        "back":             "← Back",
        "next":             "Next →",
        "new_query":        "🔄  New Query",
        "step_of":          "Step {s} of {t}",
        # Nombres de pasos
        "steps":            ["Profile","Goal","Income","Home",
                             "Debts","Leisure","Extras","Results"],
        # Validaciones
        "req_name":         "Please enter your name.",
        "req_field":        "Required field",
        "req_meta":         "Enter a valid savings goal.",
        "req_anio":         "Enter a valid year (e.g. 2026).",
        "invalid_year":     "Invalid year",
        "req_salary":       "Enter your gross monthly salary.",
        # Paso 0 — Perfil
        "p0_title":         "👤  Your Profile",
        "p0_sub":           "Tell us about yourself to personalize your report.",
        "p0_section":       "Personal Information",
        "p0_name":          "Full name *",
        "p0_country":       "Country of residence *",
        "p0_note":          "⚠️  BETA VERSION IN DEVELOPMENT — Currently only available for Panama (CSS 9.75% + Educational Insurance 1.25% + Progressive ISR). More countries coming soon. All calculations are estimates.",
        # Paso 1 — Meta
        "p1_title":         "🎯  Savings Goal",
        "p1_sub":           "Define how much you want to save and by when.",
        "p1_section":       "Your Financial Goal",
        "p1_meta":          "Savings goal ($) *",
        "p1_month":         "Target month *",
        "p1_year":          "Target year *",
        "p1_tip":           "💡  Consistent monthly savings, even small amounts, have a huge long-term impact. Be realistic with your goal and celebrate every month you achieve it.",
        # Paso 2 — Ingresos
        "p2_title":         "💵  Income  —  {nombre}",
        "p2_sub":           "Country: {pais}  |  Deductions calculated automatically.",
        "p2_section":       "Monthly Salary",
        "p2_gross":         "Gross monthly salary ($) *",
        "p2_extra":         "Extra income this month ($)",
        "p2_imp_hint":      "🧮  Enter your gross salary to see the breakdown",
        "p2_imp_title":     "🧮  Estimated deductions breakdown — {pais}",
        "p2_net_est":       "  Estimated Net Salary:",
        "p2_note":          "⚠️  IMPORTANT NOTICE: The tax calculation shown above is an estimate based on Panama's official rates. The actual amount may vary due to additional deductions, bonuses, CSS adjustments, or law changes. Always check your official pay stub for the actual amount received.",
        "p2_real":          "ACTUAL salary received per your pay stub ($)  (if different from estimate above)",
        "p2_real_tip":      "💡  If left empty,\nthe estimated net salary will be used.",
        # Paso 3 — Hogar
        "p3_title":         "🏠  Home Expenses",
        "p3_sub":           "Basic services and housing.",
        "p3_section":       "Fixed Monthly Expenses",
        "p3_rent":          "Rent / Mortgage ($)",
        "p3_internet":      "Internet ($)",
        "p3_electric":      "Electricity ($)",
        "p3_water":         "Water ($)",
        "p3_mobile":        "Mobile Data / Phone ($)",
        # Paso 4 — Deudas/Auto/Mascotas
        "p4_title":         "🏦  Debts, Car & Pets",
        "p4_sub":           "Loans, vehicle expenses and pet care.",
        "p4_s1":            "Loans & Debts",
        "p4_loan_p":        "Personal Loan ($)",
        "p4_loan_a":        "Car Loan ($)",
        "p4_debts":         "Other Debts ($)",
        "p4_s2":            "Car Expenses",
        "p4_gas":           "Gas ($)",
        "p4_maint":         "Maintenance ($)",
        "p4_s3":            "Pet Expenses",
        "p4_pet_food":      "Pet food ($)",
        "p4_pet_vet":       "Veterinarian ($)",
        "p4_pet_other":     "Other pet expenses ($)",
        # Paso 5 — Ocio
        "p5_title":         "🎬  Leisure & Subscriptions",
        "p5_sub":           "Entertainment, food and digital platforms.",
        "p5_s1":            "Variable Expenses",
        "p5_grocery":       "Grocery / Food ($)",
        "p5_out":           "Outings / Entertainment ($)",
        "p5_delivery":      "Delivery ($)",
        "p5_s2":            "Digital Subscriptions",
        # Paso 6 — Extras
        "p6_title":         "➕  Extra Expenses",
        "p6_sub":           "Any additional expense that doesn't fit previous categories.",
        "p6_section":       "Additional Expenses",
        "p6_extra":         "Extra Expense {n} ($)",
        "p6_desc":          "Description",
        "p6_hint":          "✔  Pressing 'Next' will calculate all your results.",
        # Paso 7 — Resultado
        "p7_title":         "📊  Results  —  {nombre}",
        "p7_sub":           "{pais}  •  Goal: ${meta:,.2f} for {mes} {anio}",
        "p7_deficit":       "⚠  Monthly deficit of ${amt:,.2f}  —  Your expenses exceed your income",
        "p7_ontrack":       "🎉  Saving ${amt:,.2f}/mo  —  You'll reach your goal before {mes} {anio}!",
        "p7_need":          "💡  Saving ${amt:,.2f}/mo  —  You need ${falta:,.2f} more/mo for your goal",
        "p7_salary_imp":    "🧾  Salary & Taxes",
        "p7_total_ded":     "Total deductions (estimated)",
        "p7_net_est":       "Net Salary (estimated)",
        "p7_net_real":      "Actual Salary (pay stub)",
        "p7_imp_note":      "⚠️  The tax calculation is an estimate. It may vary due to additional deductions, bonuses or CSS adjustments. Always verify with your official pay stub.",
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
        "p7_new":           "💡  Use the 'New Query' button in the bottom bar to start over.",
        "pdf_saved":        "✅ PDF Generated",
        "pdf_saved_msg":    "Report saved at:\n{ruta}",
        "pdf_save_title":   "Save PDF report",
        # Meses
        "months":           ["January","February","March","April","May","June",
                             "July","August","September","October","November","December"],
        # Impuestos
        "tax_css":          "CSS (9.75%)",
        "tax_edu":          "Educational Insurance (1.25%)",
        "tax_isr":          "Estimated monthly ISR",
        # PDF
        "pdf_title":        "Salary & Goals Calculator",
        "pdf_by":           "by Erick Perez",
        "pdf_date":         "Generated on {d}",
        "pdf_goal_for":     "Goal: ${m:,.2f} for {mes} {anio}",
        "pdf_salary":       "Salary & Taxes",
        "pdf_gross":        "Gross Salary",
        "pdf_ded_est":      "Total Deductions (estimated)",
        "pdf_net_est":      "Estimated Net Salary",
        "pdf_net_real":     "Actual Salary Received (pay stub)",
        "pdf_note":         "NOTE: Tax calculation is estimated and may vary. Verify with your official pay stub.",
        "pdf_income":       "Total Income",
        "pdf_net_base":     "Net Salary (base calculation)",
        "pdf_extra_inc":    "Extra Income",
        "pdf_total_inc":    "TOTAL INCOME",
        "pdf_home":         "Fixed Home Expenses",
        "pdf_rent":         "Rent / Mortgage",
        "pdf_electric":     "Electricity",
        "pdf_water":        "Water",
        "pdf_mobile":       "Mobile Data / Phone",
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
        "pdf_vars":         "Variable Expenses & Subscriptions",
        "pdf_grocery":      "Grocery / Food",
        "pdf_out":          "Outings / Entertainment",
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
        "pdf_warn":         "ATTENTION: You need ${n:,.2f} more/mo to reach your goal.",
        "pdf_alert":        "ALERT: Your expenses exceed your income.",
        "pdf_footer":       "Salary & Goals Calculator  •  by Erick Perez  •  {nombre}  •  {pais}",
    },
}

# Idioma activo global
_LANG = "es"

def T(key, **kw):
    """Devuelve la cadena traducida al idioma activo."""
    txt = LANGS[_LANG].get(key, LANGS["es"].get(key, key))
    return txt.format(**kw) if kw else txt

def set_lang(lang):
    global _LANG
    _LANG = lang

def get_months():
    return LANGS[_LANG]["months"]

# ══════════════════════════════════════════════════════════
#  TEMA WINDOWS 11
# ══════════════════════════════════════════════════════════
W11 = {
    "bg":           "#f3f3f3",
    "surface":      "#ffffff",
    "surface2":     "#f9f9f9",
    "accent":       "#0067c0",
    "accent_h":     "#1a7ed4",
    "accent_dk":    "#004f9e",
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

FONT    = "Segoe UI"
F_TITLE = (FONT, 20, "bold")
F_SUBH  = (FONT, 11, "bold")
F_BODY  = (FONT, 10)
F_SMALL = (FONT, 9)
F_INPUT = (FONT, 10)
F_BTN   = (FONT, 10, "bold")
F_LABEL = (FONT, 9)

# ══════════════════════════════════════════════════════════
#  IMPUESTOS — PANAMÁ
# ══════════════════════════════════════════════════════════

def calcular_impuestos_panama(salario_bruto):
    css           = salario_bruto * 0.0975
    seg_educativo = salario_bruto * 0.0125
    base_isr_mes  = salario_bruto - css - seg_educativo
    anual         = base_isr_mes * 12
    if anual <= 11000:
        isr_anual = 0
    elif anual <= 50000:
        isr_anual = (anual - 11000) * 0.15
    else:
        isr_anual = (50000 - 11000) * 0.15 + (anual - 50000) * 0.25
    isr_mes   = isr_anual / 12
    total     = css + seg_educativo + isr_mes
    neto      = salario_bruto - total
    return {
        "css":           round(css, 2),
        "seg_educativo": round(seg_educativo, 2),
        "isr":           round(isr_mes, 2),
        "total_imp":     round(total, 2),
        "salario_neto":  round(neto, 2),
        "detalle": [
            (T("tax_css"),  round(css, 2)),
            (T("tax_edu"),  round(seg_educativo, 2)),
            (T("tax_isr"),  round(isr_mes, 2)),
        ]
    }

PAISES = {
    "Panamá": {"moneda": "USD", "simbolo": "$", "calcular": calcular_impuestos_panama},
}

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
            cid = self.canvas.create_oval(x-r,y-r,x+r,y+r, fill=col, outline="")
            self._particles.append({"id":cid,"x":x,"y":y,"vx":vx,"vy":vy,"r":r,"w":w,"h":h})

        self._coin_id = self.canvas.create_text(w//2, 80, text="💰",
                                                font=(FONT, 48), fill="#f0c040")
        self._title_id = self.canvas.create_text(w//2, 162,
            text=T("splash_sub"), font=(FONT,22,"bold"), fill="#ffffff")
        self._sub_id = self.canvas.create_text(w//2, 202,
            text="by Erick Perez", font=(FONT,13,"italic"), fill="#94a3b8")
        self._ver_id = self.canvas.create_text(w//2, 230,
            text=T("splash_edition"), font=(FONT,10), fill="#475569")

        self._bar_bg = self.canvas.create_rectangle(
            w//2-180, 280, w//2+180, 298, fill="#1e293b", outline="#334155")
        self._bar_fg = self.canvas.create_rectangle(
            w//2-180, 280, w//2-180, 298, fill="#0067c0", outline="")
        self._bar_lbl = self.canvas.create_text(
            w//2, 312, text="0%", font=(FONT,9), fill="#64748b")

        self._bar_w    = 360
        self._bar_x0   = w//2 - 180
        self._total_ms = 3200
        self._step_ms  = 30
        self._elapsed  = 0
        self._animate()

    def _animate(self):
        self._elapsed += self._step_ms
        pct = min(self._elapsed / self._total_ms, 1.0)
        msgs = LANGS[_LANG]["splash_loading"]
        pct100 = int(pct * 100)
        thresholds = [0, 20, 50, 75, 95]
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
        style = ttk.Style()
        style.configure("W11.TCombobox", fieldbackground=W11["input_bg"],
                        background=W11["input_bg"], foreground=W11["text"],
                        selectbackground=W11["accent"], borderwidth=1)
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
#  BARRA DE PASOS
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
        for i, (c, l) in enumerate(zip(self._circles, self._labels)):
            lbl_text = steps[i] if i < len(steps) else str(i+1)
            if i < step:
                c.config(bg=W11["step_done"]); l.config(text=lbl_text, fg=W11["step_done"], font=F_SMALL)
            elif i == step:
                c.config(bg=W11["step_act"]);  l.config(text=lbl_text, fg=W11["step_act"], font=(FONT,9,"bold"))
            else:
                c.config(bg=W11["step_pend"]); l.config(text=lbl_text, fg=W11["text3"], font=F_SMALL)

# ══════════════════════════════════════════════════════════
#  PDF
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
        C_WARN  = colors.HexColor("#ca5010")
        C_GRIS  = colors.HexColor("#f3f3f3")
        C_BORDE = colors.HexColor("#e0e0e0")
        C_DARK  = colors.HexColor("#1a1a1a")

        tit  = ParagraphStyle("tit",  fontSize=22, textColor=C_AZUL,
                              alignment=TA_CENTER, spaceAfter=4, fontName="Helvetica-Bold")
        sub  = ParagraphStyle("sub",  fontSize=10, textColor=colors.grey,
                              alignment=TA_CENTER, spaceAfter=14)
        h2   = ParagraphStyle("h2",   fontSize=12, textColor=C_AZUL,
                              spaceBefore=14, spaceAfter=4, fontName="Helvetica-Bold")
        norm = styles["Normal"]
        der  = ParagraphStyle("der",  fontSize=10, alignment=TA_RIGHT)

        ts = TableStyle([
            ("ROWBACKGROUNDS",(0,0),(-1,-1),[C_GRIS, colors.white]),
            ("BOX",(0,0),(-1,-1),0.5,C_BORDE),("INNERGRID",(0,0),(-1,-1),0.25,C_BORDE),
            ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
            ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),8),
        ])

        def fila(lbl, monto, col=None, bold=False):
            fn = "Helvetica-Bold" if bold else "Helvetica"
            col = col or C_DARK
            hx  = col.hexval() if hasattr(col,"hexval") else str(col)
            return [
                Paragraph(f'<font name="{fn}">{lbl}</font>', norm),
                Paragraph(f'<font name="{fn}" color="{hx}">${monto:,.2f}</font>', der),
            ]

        def tabla(rows):
            t = Table(rows, colWidths=["70%","30%"])
            t.setStyle(ts)
            return t

        imp    = datos["impuestos"]
        sal_real = datos.get("salario_real", 0)
        sal_base = sal_real if sal_real > 0 else imp["salario_neto"]
        months = get_months()
        mes_n  = months[datos["mes_num"]-1]
        nombre = datos.get("nombre","")
        pais   = datos.get("pais","Panama")

        story = []
        story.append(Paragraph(T("pdf_title"), tit))
        story.append(Paragraph(f"{T('pdf_by')}  •  {nombre}  •  {pais}", sub))
        story.append(Paragraph(
            T("pdf_date", d=date.today().strftime('%d/%m/%Y')) +
            f"  •  " + T("pdf_goal_for", m=datos['meta'], mes=mes_n, anio=datos['anio_meta']), sub))
        story.append(HRFlowable(width="100%", thickness=2, color=C_AZUL, spaceAfter=10))

        # Salario
        story.append(Paragraph(T("pdf_salary"), h2))
        rows_imp = [fila(T("pdf_gross"), datos["salario"])]
        for nd, md in imp["detalle"]:
            rows_imp.append(fila(f"  - {nd}", md, C_ROJO))
        rows_imp.append(fila(T("pdf_ded_est"), imp["total_imp"], C_ROJO, True))
        if sal_real > 0:
            rows_imp.append(fila(T("pdf_net_est"), imp["salario_neto"], C_AZUL))
            rows_imp.append(fila(T("pdf_net_real"), sal_real, C_VERDE, True))
        else:
            rows_imp.append(fila(T("pdf_net_est"), imp["salario_neto"], C_VERDE, True))
        story.append(tabla(rows_imp))

        nota_style = ParagraphStyle("nota", fontSize=8,
            textColor=colors.HexColor("#8a6914"),
            backColor=colors.HexColor("#fef9e7"),
            spaceAfter=8, leftIndent=8, rightIndent=8, leading=12)
        story.append(Paragraph(T("pdf_note"), nota_style))
        story.append(Spacer(1, 8))

        # Ingresos
        story.append(Paragraph(T("pdf_income"), h2))
        rows_ing = [
            fila(T("pdf_net_base"),   sal_base),
            fila(T("pdf_extra_inc"),  datos.get("ingreso_extra",0)),
            fila(T("pdf_total_inc"),  datos["total_ingresos"], C_VERDE, True),
        ]
        story.append(tabla(rows_ing))

        # Hogar
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
            fila(T("pdf_loan_p"),  datos.get("prestamo_personal",0)),
            fila(T("pdf_loan_a"),  datos.get("prestamo_auto",0)),
            fila(T("pdf_debts"),   datos.get("deudas",0)),
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
        ge = [fila(f"{T('p7_extra_lbl', desc=g['desc'])}", g['monto'])
              for g in datos.get("gastos_extra",[]) if g["monto"]>0]
        if ge:
            story.append(Paragraph(T("pdf_extras"), h2))
            story.append(tabla(ge))

        # Resumen
        col_ah = C_VERDE if datos["ahorro_mensual"]>=0 else C_ROJO
        story.append(Paragraph(T("pdf_summary"), h2))
        story.append(tabla([
            fila(T("pdf_tot_inc"), datos["total_ingresos"],         C_VERDE, True),
            fila(T("pdf_tot_exp"), datos["total_gastos"],           C_ROJO,  True),
            fila(T("pdf_saving"),  abs(datos["ahorro_mensual"]),    col_ah,  True),
        ]))

        # Meta
        meses_r = datos["meses_restantes"]
        nec_mes = datos["meta"]/meses_r if meses_r>0 else 0
        proyecc = max(datos["ahorro_mensual"],0)*meses_r
        story.append(Paragraph(T("pdf_analysis"), h2))
        story.append(tabla([
            [Paragraph(T("pdf_goal_amt"), norm),
             Paragraph(f'<font color="#107c10"><b>${datos["meta"]:,.2f}</b></font>', der)],
            [Paragraph(T("pdf_objective", mes=mes_n, anio=datos['anio_meta']), norm),
             Paragraph(f'<b>{T("pdf_months_left", n=meses_r)}</b>', der)],
            [Paragraph(T("pdf_need_mo"), norm),
             Paragraph(f'<font color="#ca5010"><b>${nec_mes:,.2f}</b></font>', der)],
            [Paragraph(T("pdf_curr_mo"), norm),
             Paragraph(f'<font color="{"#107c10" if datos["ahorro_mensual"]>=0 else "#d13438"}"><b>${datos["ahorro_mensual"]:,.2f}</b></font>', der)],
            [Paragraph(T("pdf_projection"), norm),
             Paragraph(f'<font color="#0067c0"><b>${proyecc:,.2f}</b></font>', der)],
        ]))

        story.append(Spacer(1,14))
        if datos["ahorro_mensual"]<=0:
            msg=T("pdf_alert"); col="#d13438"
        elif proyecc>=datos["meta"]:
            msg=T("pdf_ok", mes=mes_n, anio=datos['anio_meta']); col="#107c10"
        else:
            msg=T("pdf_warn", n=nec_mes-datos['ahorro_mensual']); col="#ca5010"
        story.append(Paragraph(f'<font color="{col}"><b>{msg}</b></font>',
            ParagraphStyle("concl",fontSize=11,spaceAfter=6,leading=16)))
        story.append(HRFlowable(width="100%",thickness=1,color=C_BORDE))
        story.append(Paragraph(T("pdf_footer", nombre=nombre, pais=pais),
            ParagraphStyle("foot",fontSize=8,textColor=colors.grey,
                           alignment=TA_CENTER,spaceBefore=8)))
        doc.build(story)
        return True
    except Exception as e:
        messagebox.showerror("Error PDF", f"Could not generate PDF:\n{e}")
        return False

# ══════════════════════════════════════════════════════════
#  APP PRINCIPAL
# ══════════════════════════════════════════════════════════

class CalcApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.title(T("app_title"))
        self.configure(bg=W11["bg"])
        self.geometry("880x700")
        self.minsize(780, 580)
        self._step  = 0
        self._datos = {}
        self._fields= {}
        SplashScreen(self, self._after_splash)

    def _after_splash(self):
        self.deiconify()
        self._build_chrome()
        self._show_step(0)

    # ── Chrome ───────────────────────────────────────────
    def _build_chrome(self):
        tb = tk.Frame(self, bg=W11["title_bar"], height=48)
        tb.pack(fill="x"); tb.pack_propagate(False)

        self._title_lbl = tk.Label(tb, text=T("title_bar"),
                 font=(FONT,12,"bold"), bg=W11["title_bar"], fg="white")
        self._title_lbl.pack(side="left", padx=8)

        # Selector de idioma — botones de bandera
        lang_f = tk.Frame(tb, bg=W11["title_bar"])
        lang_f.pack(side="right", padx=12)

        self._btn_es = tk.Button(lang_f, text="🇪🇸 ES", font=(FONT,9,"bold"),
            bg="#334155", fg="white", relief="flat", padx=8, pady=4,
            cursor="hand2", command=lambda: self._change_lang("es"))
        self._btn_es.pack(side="left", padx=2)

        self._btn_en = tk.Button(lang_f, text="🇺🇸 EN", font=(FONT,9,"bold"),
            bg="#1e3a5f", fg="white", relief="flat", padx=8, pady=4,
            cursor="hand2", command=lambda: self._change_lang("en"))
        self._btn_en.pack(side="left", padx=2)

        self._update_lang_btns()

        self.stepbar = StepBar(self)
        self.stepbar.pack(fill="x")
        tk.Frame(self, bg=W11["border"], height=1).pack(fill="x")

        self.content = tk.Frame(self, bg=W11["bg"])
        self.content.pack(fill="both", expand=True)

        nav = tk.Frame(self, bg=W11["surface"],
                       highlightbackground=W11["border"], highlightthickness=1, height=60)
        nav.pack(fill="x", side="bottom"); nav.pack_propagate(False)

        self.btn_back = W11Button(nav, text=T("back"), primary=False,
                                  command=self._prev_step)
        self.btn_back.pack(side="left", padx=20, pady=10)

        self.lbl_step = tk.Label(nav, text=T("step_of", s=1, t=8),
                                 font=F_SMALL, bg=W11["surface"], fg=W11["text2"])
        self.lbl_step.pack(side="left", expand=True)

        self.btn_next = W11Button(nav, text=T("next"), primary=True,
                                  command=self._next_step)
        self.btn_next.pack(side="right", padx=20, pady=10)

    def _update_lang_btns(self):
        self._btn_es.config(bg="#0067c0" if _LANG=="es" else "#334155")
        self._btn_en.config(bg="#0067c0" if _LANG=="en" else "#334155")

    def _change_lang(self, lang):
        set_lang(lang)
        self._update_lang_btns()
        self.title(T("app_title"))
        self._title_lbl.config(text=T("title_bar"))
        # Refresh stepbar labels
        self.stepbar.update_step(self._step)
        # Refresh nav buttons
        total = 8
        self.lbl_step.config(text=T("step_of", s=self._step+1, t=total))
        is_last = (self._step == total - 1)
        if is_last:
            self.btn_next.config(text=T("new_query"))
        else:
            self.btn_next.config(text=T("next"))
        self.btn_back.config(text=T("back"))
        # Rebuild current step content
        self._clear_content()
        builders = [
            self._step_perfil, self._step_meta, self._step_ingresos,
            self._step_hogar,  self._step_deudas_auto, self._step_ocio,
            self._step_extras, self._step_resultado,
        ]
        builders[self._step]()

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

    # ── Navegación ───────────────────────────────────────
    def _show_step(self, step):
        self._step = step
        self._clear_content()
        self.stepbar.update_step(step)
        total = 8
        self.lbl_step.config(text=T("step_of", s=step+1, t=total))
        self.btn_back.config(state="normal" if step > 0 else "disabled",
                             text=T("back"))
        is_last = (step == total - 1)
        if is_last:
            self.btn_next.config(text=T("new_query"), command=self._reset,
                                 state="normal")
            self.btn_next._bg  = W11["btn_sec"]
            self.btn_next._abg = W11["border2"]
            self.btn_next.config(bg=W11["btn_sec"], fg=W11["btn_sec_fg"],
                                 activebackground=W11["border2"])
        else:
            self.btn_next.config(text=T("next"), command=self._next_step,
                                 state="normal")
            self.btn_next._bg  = W11["btn_bg"]
            self.btn_next._abg = W11["accent_h"]
            self.btn_next.config(bg=W11["btn_bg"], fg=W11["btn_fg"],
                                 activebackground=W11["accent_h"])
        builders = [
            self._step_perfil, self._step_meta, self._step_ingresos,
            self._step_hogar,  self._step_deudas_auto, self._step_ocio,
            self._step_extras, self._step_resultado,
        ]
        builders[step]()

    def _next_step(self):
        validators = {
            0: self._validate_perfil,
            1: self._validate_meta,
            2: self._validate_ingresos,
        }
        if self._step in validators:
            if not validators[self._step]():
                return
        self._save_step(self._step)
        self._show_step(self._step + 1)

    def _prev_step(self):
        self._save_step(self._step)
        self._show_step(self._step - 1)

    def _save_step(self, step):
        f = self._fields
        if step == 0:
            self._datos["nombre"] = f["nombre"].get() if "nombre" in f else ""
            self._datos["pais"]   = f["pais"].get()   if "pais"   in f else "Panamá"
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
            self._datos["decimo"]        = 0
        elif step == 3:
            for k in ["alquiler","internet","luz","agua","data_movil"]:
                self._datos[k] = val(f[k])
        elif step == 4:
            for k in ["prestamo_personal","prestamo_auto","deudas",
                      "gasolina","mantenimiento_auto",
                      "mascota_comida","mascota_vet","mascota_otros"]:
                self._datos[k] = val(f[k])
        elif step == 5:
            for k in ["comida","salidas","delivery",
                      "apple_one","netflix","hbo","disney"]:
                self._datos[k] = val(f[k])
        elif step == 6:
            extras = []
            for i in range(3):
                m = val(f[f"extra_m_{i}"])
                default = T("p6_extra", n=i+1).replace(" ($)","")
                d = f[f"extra_d_{i}"].get().strip() or default
                extras.append({"monto": m, "desc": d})
            self._datos["gastos_extra"] = extras

    # ── Validadores ─────────────────────────────────────
    def _validate_perfil(self):
        if not self._fields.get("nombre") or not self._fields["nombre"].get().strip():
            messagebox.showwarning(T("req_field"), T("req_name"))
            return False
        return True

    def _validate_meta(self):
        months = get_months()
        try:
            m = float(self._fields["meta"].get().replace(",","."))
            if m <= 0: raise ValueError
        except:
            messagebox.showwarning(T("req_field"), T("req_meta"))
            return False
        try:
            int(self._fields["anio"].get())
        except:
            messagebox.showwarning(T("invalid_year"), T("req_anio"))
            return False
        return True

    def _validate_ingresos(self):
        try:
            s = float(self._fields["salario"].get().replace(",","."))
            if s <= 0: raise ValueError
        except:
            messagebox.showwarning(T("req_field"), T("req_salary"))
            return False
        return True

    # ── Título ───────────────────────────────────────────
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
    #  PASO 0 — PERFIL
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

        pais = W11Combo(g, label=T("p0_country"),
                        values=list(PAISES.keys()), width=22)
        pais.set(self._datos.get("pais","Panamá"))
        pais.grid(row=0, column=1, sticky="ew", pady=4)
        self._fields["pais"] = pais

        note_box(c, T("p0_note"), W11["surface2"], W11["border"])

    # ════════════════════════════════════════════════════
    #  PASO 1 — META
    # ════════════════════════════════════════════════════
    def _step_meta(self):
        f = self._scrollable()
        self._page_title(f, T("p1_title"), T("p1_sub"))
        c = card(f)
        section_title(c, T("p1_section"), "📅")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=14, pady=(0,14))
        g.columnconfigure(0,weight=2); g.columnconfigure(1,weight=1); g.columnconfigure(2,weight=1)

        meta_w = W11Entry(g, label=T("p1_meta"), prefix="$")
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
    #  PASO 2 — INGRESOS
    # ════════════════════════════════════════════════════
    def _step_ingresos(self):
        f = self._scrollable()
        pais   = self._datos.get("pais","Panamá")
        nombre = self._datos.get("nombre","")
        self._page_title(f, T("p2_title", nombre=nombre),
                            T("p2_sub", pais=pais))
        c = card(f)
        section_title(c, T("p2_section"), "🧾")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=14, pady=(0,4))
        g.columnconfigure(0, weight=1); g.columnconfigure(1, weight=1)

        sal_w = W11Entry(g, label=T("p2_gross"), prefix="$")
        sal_w.grid(row=0, column=0, sticky="ew", padx=(0,10), pady=4)
        sal_w.set(str(self._datos.get("salario","")))
        self._fields["salario"] = sal_w

        ext_w = W11Entry(g, label=T("p2_extra"), prefix="$")
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

        real_w = W11Entry(g2, label=T("p2_real"), prefix="$")
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
            s = float(self._fields["salario"].get().replace(",","."))
            if s <= 0: raise ValueError
        except:
            return
        pais = self._datos.get("pais","Panamá")
        imp  = PAISES[pais]["calcular"](s)
        self._imp_title.config(text=T("p2_imp_title", pais=pais),
                               fg=W11["text"], font=(FONT,9,"bold"))
        for nd, md in imp["detalle"]:
            row = tk.Frame(self._imp_rows_frame, bg=W11["surface2"])
            row.pack(fill="x", pady=1)
            tk.Label(row, text=f"  {nd}", font=F_SMALL,
                     bg=W11["surface2"], fg=W11["text2"]).pack(side="left")
            tk.Label(row, text=f"-${md:,.2f}", font=(FONT,9,"bold"),
                     bg=W11["surface2"], fg=W11["danger"]).pack(side="right")
        tk.Frame(self._imp_rows_frame, bg=W11["border"], height=1).pack(fill="x", pady=4)
        row_n = tk.Frame(self._imp_rows_frame, bg=W11["surface2"])
        row_n.pack(fill="x")
        tk.Label(row_n, text=T("p2_net_est"), font=(FONT,10,"bold"),
                 bg=W11["surface2"], fg=W11["text"]).pack(side="left")
        tk.Label(row_n, text=f"${imp['salario_neto']:,.2f}", font=(FONT,12,"bold"),
                 bg=W11["surface2"], fg=W11["success"]).pack(side="right")

    # ════════════════════════════════════════════════════
    #  PASO 3 — HOGAR
    # ════════════════════════════════════════════════════
    def _step_hogar(self):
        f = self._scrollable()
        self._page_title(f, T("p3_title"), T("p3_sub"))
        c = card(f)
        section_title(c, T("p3_section"), "📋")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=14, pady=(0,14))
        g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
        for i,(k,lk) in enumerate([
            ("alquiler",   "p3_rent"),
            ("internet",   "p3_internet"),
            ("luz",        "p3_electric"),
            ("agua",       "p3_water"),
            ("data_movil", "p3_mobile"),
        ]):
            w = W11Entry(g, label=T(lk), prefix="$")
            w.grid(row=i//2, column=i%2, sticky="ew",
                   padx=(0,10) if i%2==0 else 0, pady=4)
            w.set(str(self._datos.get(k,"")))
            self._fields[k] = w

    # ════════════════════════════════════════════════════
    #  PASO 4 — DEUDAS / AUTO / MASCOTAS
    # ════════════════════════════════════════════════════
    def _step_deudas_auto(self):
        f = self._scrollable()
        self._page_title(f, T("p4_title"), T("p4_sub"))
        for sec, icon, campos in [
            (T("p4_s1"), "💳", [
                ("prestamo_personal","p4_loan_p"),
                ("prestamo_auto",    "p4_loan_a"),
                ("deudas",           "p4_debts"),
            ]),
            (T("p4_s2"), "🚗", [
                ("gasolina",           "p4_gas"),
                ("mantenimiento_auto", "p4_maint"),
            ]),
            (T("p4_s3"), "🐾", [
                ("mascota_comida","p4_pet_food"),
                ("mascota_vet",   "p4_pet_vet"),
                ("mascota_otros", "p4_pet_other"),
            ]),
        ]:
            c = card(f, pady=8)
            section_title(c, sec, icon)
            g = tk.Frame(c, bg=W11["surface"])
            g.pack(fill="x", padx=14, pady=(0,10))
            g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
            for i,(k,lk) in enumerate(campos):
                w = W11Entry(g, label=T(lk), prefix="$")
                w.grid(row=i//2, column=i%2, sticky="ew",
                       padx=(0,10) if i%2==0 else 0, pady=4)
                w.set(str(self._datos.get(k,"")))
                self._fields[k] = w

    # ════════════════════════════════════════════════════
    #  PASO 5 — OCIO / SUSCRIPCIONES
    # ════════════════════════════════════════════════════
    def _step_ocio(self):
        f = self._scrollable()
        self._page_title(f, T("p5_title"), T("p5_sub"))
        for sec, icon, campos in [
            (T("p5_s1"), "🛒", [
                ("comida",   "p5_grocery"),
                ("salidas",  "p5_out"),
                ("delivery", "p5_delivery"),
            ]),
            (T("p5_s2"), "📱", [
                ("apple_one","Apple One"),
                ("netflix",  "Netflix"),
                ("hbo",      "HBO Max"),
                ("disney",   "Disney+"),
            ]),
        ]:
            c = card(f, pady=8)
            section_title(c, sec, icon)
            g = tk.Frame(c, bg=W11["surface"])
            g.pack(fill="x", padx=14, pady=(0,10))
            g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
            for i,(k,lk) in enumerate(campos):
                # lk puede ser una clave de traducción o un literal
                lbl = T(lk) if lk in LANGS["es"] else lk
                w = W11Entry(g, label=f"{lbl} ($)", prefix="$")
                w.grid(row=i//2, column=i%2, sticky="ew",
                       padx=(0,10) if i%2==0 else 0, pady=4)
                w.set(str(self._datos.get(k,"")))
                self._fields[k] = w

    # ════════════════════════════════════════════════════
    #  PASO 6 — EXTRAS
    # ════════════════════════════════════════════════════
    def _step_extras(self):
        f = self._scrollable()
        self._page_title(f, T("p6_title"), T("p6_sub"))
        c = card(f)
        section_title(c, T("p6_section"), "📝")
        extras = self._datos.get("gastos_extra",
                                 [{"monto":0,"desc":""},{"monto":0,"desc":""},{"monto":0,"desc":""}])
        for i in range(3):
            row = tk.Frame(c, bg=W11["surface"])
            row.pack(fill="x", padx=14, pady=4)
            row.columnconfigure(0,weight=1); row.columnconfigure(1,weight=2)
            mw = W11Entry(row, label=T("p6_extra", n=i+1), prefix="$")
            mw.grid(row=0, column=0, sticky="ew", padx=(0,12))
            mw.set(str(extras[i]["monto"]) if extras[i]["monto"] else "")
            self._fields[f"extra_m_{i}"] = mw
            dw = W11Entry(row, label=T("p6_desc"), prefix="")
            dw.grid(row=0, column=1, sticky="ew")
            dw.set(extras[i]["desc"])
            self._fields[f"extra_d_{i}"] = dw

        tk.Frame(c, bg=W11["border"], height=1).pack(fill="x", padx=14, pady=12)
        tk.Label(c, text=T("p6_hint"), font=F_SMALL, bg=W11["surface"],
                 fg=W11["text2"]).pack(padx=14, pady=(0,14), anchor="w")

    # ════════════════════════════════════════════════════
    #  PASO 7 — RESULTADO
    # ════════════════════════════════════════════════════
    def _step_resultado(self):
        self._save_step(6)
        d    = self._datos
        pais = d.get("pais","Panamá")
        imp  = PAISES[pais]["calcular"](d.get("salario",0))
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

        f = self._scrollable()
        self._page_title(f,
            T("p7_title", nombre=d.get("nombre","")),
            T("p7_sub", pais=pais, meta=meta, mes=mes_n, anio=d.get("anio_meta",2026)))

        # Banner
        col_b = W11["success"] if ahorro >= 0 else W11["danger"]
        banner = tk.Frame(f, bg=col_b)
        banner.pack(fill="x", padx=28, pady=(0,10))
        if ahorro <= 0:
            bmsg = T("p7_deficit", amt=abs(ahorro))
        elif proyecc >= meta:
            bmsg = T("p7_ontrack", amt=ahorro, mes=mes_n, anio=d.get("anio_meta",2026))
        else:
            bmsg = T("p7_need", amt=ahorro, falta=nec_mes-ahorro)
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
                tk.Label(row, text=f"${amt:,.2f}", font=(FONT,10,"bold"),
                         bg=W11["surface"], fg=col).pack(side="right")
            tk.Frame(c, bg=W11["border"], height=1).pack(fill="x", padx=14, pady=(6,4))

        # Salario
        imp_rows = [(n, m, DA) for n,m in imp["detalle"]]
        imp_rows += [(T("p7_total_ded"), imp["total_imp"], DA)]
        if sal_real > 0:
            imp_rows += [
                (T("p7_net_est"),  imp["salario_neto"], AC),
                (T("p7_net_real"), sal_real,             SU),
            ]
        else:
            imp_rows += [(T("p7_net_est"), imp["salario_neto"], SU)]
        res_card(f, T("p7_salary_imp"), imp_rows)

        note_c = card(f, pady=4)
        note_c.config(bg=W11["note_bg"], highlightbackground=W11["note_border"])
        tk.Label(note_c, text=T("p7_imp_note"), font=F_SMALL,
                 bg=W11["note_bg"], fg=W11["gold"],
                 wraplength=720, justify="left").pack(padx=12, pady=8, anchor="w")

        res_card(f, T("p7_income"), [
            (T("p7_net_base"),  sal_base,                  T_),
            (T("p7_extra_inc"), d.get("ingreso_extra",0),  AC),
            (T("p7_total_inc"), d["total_ingresos"],       SU),
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
        if ge:
            res_card(f, T("p7_extras_sec"), ge)

        res_card(f, T("p7_summary"), [
            (T("p7_tot_inc"), d["total_ingresos"], SU),
            (T("p7_tot_exp"), d["total_gastos"],   DA),
            (T("p7_saving"),  abs(ahorro), SU if ahorro>=0 else DA),
        ])

        meta_c = card(f, pady=6)
        section_title(meta_c, T("p7_goal"))
        for lbl, val_s, col in [
            (T("p7_goal_amt"),    f"${meta:,.2f}",    SU),
            (T("p7_months_left"), str(meses_r),        T_),
            (T("p7_need_mo"),     f"${nec_mes:,.2f}", WA),
            (T("p7_curr_mo"),     f"${ahorro:,.2f}",  SU if ahorro>=0 else DA),
            (T("p7_projection"),  f"${proyecc:,.2f}", AC),
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
                defaultextension=".pdf",
                filetypes=[("PDF","*.pdf")],
                initialfile=f"report_{d.get('nombre','').replace(' ','_')}.pdf",
                title=T("pdf_save_title"))
            if ruta:
                if generar_pdf(d, ruta):
                    messagebox.showinfo(T("pdf_saved"),
                                        T("pdf_saved_msg", ruta=ruta))

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
        app = CalcApp()
        app.mainloop()
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("\nError. Press Enter to close...")
