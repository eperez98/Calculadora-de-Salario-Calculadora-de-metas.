# 💰 Salary & Goals Calculator — Calculadora de Salario & Metas

**by Erick Perez**

> ⚠️ **BETA VERSION IN DEVELOPMENT** | **VERSIÓN BETA EN DESARROLLO**
> Currently supports Panama tax system only. More countries coming soon.
> Actualmente solo disponible para Panamá. Próximamente más países.

---

## 🇬🇧 English

### What is this?

A **desktop salary and savings calculator** built with Python and a Windows 11-style GUI. It helps you understand your real take-home pay after taxes, track your monthly expenses by category, and plan towards a savings goal — all in one clean, step-by-step interface.

### ✨ Features

- 🪟 **Windows 11 style interface** — clean cards, smooth navigation, step-by-step flow
- 🌐 **Bilingual** — full Spanish 🇪🇸 and English 🇺🇸 support, switch instantly with one click
- 🧮 **Panama tax calculator** — CSS (9.75%) + Educational Insurance (1.25%) + progressive ISR
- 📄 **Pay stub override** — enter your actual received salary from your pay stub if it differs from the estimate
- 💸 **Full expense breakdown** — Home, Loans, Car, Pets, Leisure, Subscriptions, and custom extras
- 🎯 **Savings goal analysis** — monthly projection, months remaining, deficit/surplus tracking
- 📊 **PDF report export** — full bilingual report with all your data
- 🎬 **Animated splash screen** — intro animation on launch
- 🔄 **Multi-session** — start a new query without reopening the app

### 🚧 Current Version: v0.1 Panama Tax Only (BETA)

| Status | Detail |
|--------|--------|
| ✅ Available | Panama (CSS + Seg. Educativo + ISR) |
| 🔜 Coming soon | Costa Rica, Colombia, México, USA and more |
| 🔜 Coming soon | Dark mode |
| 🔜 Coming soon | Save/load sessions |

### 📋 Requirements

```
Python 3.10+
reportlab
```

Install dependencies:
```bash
pip install reportlab
```

### ▶️ Run

```bash
python calculadora_w11.py
```

### 🖥️ Build as .exe (Windows)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "SalaryCalculator" --hidden-import reportlab --collect-all reportlab calculadora_w11.py
```

Your `.exe` will be in the `dist/` folder.

### 📸 Screenshots

> Step-by-step Windows 11 style flow with real-time tax preview, bilingual UI, and PDF export.

---

## 🇪🇸 Español

### ¿Qué es esto?

Una **calculadora de salario y metas de ahorro** de escritorio, hecha con Python y una interfaz estilo Windows 11. Te ayuda a entender cuánto recibes realmente después de impuestos, controlar tus gastos por categoría y planificar tu meta de ahorro, todo en una interfaz limpia paso a paso.

### ✨ Características

- 🪟 **Interfaz estilo Windows 11** — tarjetas limpias, navegación fluida, flujo por pasos
- 🌐 **Bilingüe** — soporte completo en Español 🇪🇸 e Inglés 🇺🇸, cambia con un clic
- 🧮 **Calculadora de impuestos de Panamá** — CSS (9.75%) + Seg. Educativo (1.25%) + ISR progresivo
- 📄 **Salario real** — ingresa el monto exacto de tu slip de pago si difiere del estimado
- 💸 **Desglose completo de gastos** — Hogar, Préstamos, Auto, Mascotas, Ocio, Suscripciones y extras
- 🎯 **Análisis de meta de ahorro** — proyección mensual, meses restantes, seguimiento de déficit/superávit
- 📊 **Exportar reporte PDF** — reporte bilingüe completo con todos tus datos
- 🎬 **Pantalla de bienvenida animada** — animación al iniciar la app
- 🔄 **Multi-consulta** — empieza de nuevo sin cerrar la app

### 🚧 Versión actual: v0.1 Solo Impuestos Panamá (BETA)

| Estado | Detalle |
|--------|---------|
| ✅ Disponible | Panamá (CSS + Seg. Educativo + ISR) |
| 🔜 Próximamente | Costa Rica, Colombia, México, USA y más |
| 🔜 Próximamente | Modo oscuro |
| 🔜 Próximamente | Guardar / cargar sesiones |

### 📋 Requisitos

```
Python 3.10+
reportlab
```

Instalar dependencias:
```bash
pip install reportlab
```

### ▶️ Ejecutar

```bash
python calculadora_w11.py
```

### 🖥️ Generar .exe (Windows)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "CalculadoraSalario" --hidden-import reportlab --collect-all reportlab calculadora_w11.py
```

El `.exe` quedará en la carpeta `dist/`.

---

## 📁 Project Structure

```
calculadora_w11.py   ← Main application (single file)
README.md            ← This file
```

---

## 🤝 Contributing

This is a personal project in active development. Feel free to open issues or suggestions — especially for **tax systems of other countries** you'd like to see added.

Este es un proyecto personal en desarrollo activo. Abre un issue o sugerencia — especialmente si quieres ver el **sistema tributario de tu país** incluido.

---

## 📜 License

MIT License — free to use, modify and distribute.

---

*Made with ❤️ by Erick Perez — Panama 🇵🇦*
