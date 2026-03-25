<div align="center">

<img src="assets/icon.ico" alt="Salary & Goals Calculator" width="96" height="96">

# Salary & Goals Calculator
### Calculadora de Salario & Metas

**by [Erick Perez](https://github.com/eperez98) — Panama 🇵🇦**

<p>
  <a href="https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas/releases/tag/v1.1">
    <img src="https://img.shields.io/badge/version-v1.1-0067c0?style=for-the-badge&logo=python&logoColor=white" alt="Version">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/released-March_24,_2026-0067c0?style=for-the-badge" alt="Released">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/python-3.10%2B-FFD43B?style=for-the-badge&logo=python&logoColor=black" alt="Python">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-GPL--3.0-22c55e?style=for-the-badge" alt="License">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/platform-Windows_%7C_macOS_%7C_Linux-blueviolet?style=for-the-badge" alt="Platform">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/countries-6-brightgreen?style=for-the-badge" alt="Countries">
  </a>
</p>

<p>
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-whats-new-in-v11">What's New</a> •
  <a href="#-features">Features</a> •
  <a href="#-countries">Countries</a> •
  <a href="#-build-exe">Build .exe</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

*A bilingual desktop app that calculates your real take-home pay, breaks down your monthly expenses visually, and tells you exactly how long it will take to reach your savings goal — with a native Windows 11 Fluent Design interface.*

*Una app de escritorio bilingüe que calcula tu salario neto real, visualiza tus gastos y te dice exactamente cuánto tiempo tomará alcanzar tu meta de ahorro — con interfaz Fluent Design estilo Windows 11.*

</div>

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas.git
cd Calculadora-de-Salario-Calculadora-de-metas

# 2. Install dependencies
pip install reportlab pillow

# 3. Run
python Calculadora_Ahorro.py
```

> **No Python?** Download the pre-built `.exe` from [Releases](https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas/releases) — no installation needed.

**First launch:**
1. 🌐 Pick your language — **English** or **Español**
2. 🎬 Animated splash screen
3. 💰 8 guided steps → full financial picture

---

## 🆕 What's New in v1.1

> **Released March 24, 2026**

### 🌍 3 New Countries

| Country | Currency | Key Deductions |
|---------|----------|---------------|
| 🇺🇸 USA | USD | Social Security 6.2% + Medicare 1.45% + Federal Tax 2024 (7 brackets) |
| 🇨🇷 Costa Rica | CRC ₡ | CCSS SEM 5.5% + IVM 3.84% + ISR 2024 (5 tramos, exento ≤ ₡929k/mo) |
| 🇵🇪 Peru | PEN S/ | ONP 13% + Impuesto a la Renta 2024 (5 brackets, 7 UIT deduction) |

### 📊 Visual Results — Charts & Hover Details

**Expense breakdown bar chart** — horizontal bars per category, color-coded, with hover tooltip showing the exact amount and percentage of total expenses.

**Savings projection line chart** — plots your cumulative savings month-by-month up to your goal deadline. The line turns green when the goal is reached. Hover anywhere on the chart to see the exact accumulated amount at that month.

**Hover detail cards** — hover any row in the results page to see a dark popup listing every individual line item that makes up that total. Example: hover "Salary & Taxes" to see CSS, Educational Insurance, and ISR broken out separately.

### 📋 Release Notes Window

A built-in version history panel accessible from the title bar (📋 Notas / Notes button). Shows all versions with color-coded tags — NEW, FIX, CHANGE, REMOVED — fully bilingual.

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

**🧭 Navigation**
- Vertical Win11 sidebar — jump to any step
- Horizontal breadcrumb pip bar
- Progress tracked visually in real time

**📊 Results & Charts**
- Circular progress ring (savings % of income)
- Expense breakdown horizontal bar chart
- Savings projection line chart with goal line
- Animated count-up numbers on load
- Hover detail cards on every result row
- Color-coded status: on track / deficit / surplus

**🎨 Interface**
- Windows 11 Fluent Design throughout
- Light mode (default) + Dark mode
- Anti-aliased PIL icons — no image files
- 60fps animations (cubic / spring easing)
- Tooltips on every input field
- Built-in Release Notes window

</td>
<td width="50%" valign="top">

**💼 Financial Tools**
- Real-time tax deduction preview as you type
- Pay stub override — enter your actual net salary
- 7 expense categories + 3 custom extras
- Savings goal: months remaining, deficit/surplus
- PDF export — full bilingual formatted report

**💾 Data & Sessions**
- Save & load named sessions (local JSON)
- Data never leaves your machine
- Multi-session: new query without restarting

**🌐 Bilingual**
- Full English / Español UI
- Language selector on every launch
- PDF report follows your language choice
- Release Notes window fully bilingual

</td>
</tr>
</table>

---

## 🌍 Countries

### 🇵🇦 Panama — USD

| Deduction | Rate |
|-----------|------|
| CSS (Social Security) | 9.75% |
| Educational Insurance | 1.25% |
| ISR (Income Tax) | 0% → 15% → 25% progressive |

> ISR: 0% ≤ $11,000/yr · 15% on $11k–$50k · 25% above $50k

### 🇨🇴 Colombia — COP

| Deduction | Rate |
|-----------|------|
| Pensión (employee) | 4% |
| Salud (employee) | 4% |
| Retención en la Fuente | Progressive — UVT 2024 ($47,065 COP) |

> Retención: 0% (≤95 UVT/yr) → 19% → 28% → 33% → 35% → 37% → 39%

### 🇲🇽 Mexico — MXN

| Deduction | Rate |
|-----------|------|
| IMSS — Enfermedad y Maternidad | ~2.50% |
| IMSS — Invalidez y Vida | ~0.63% |
| IMSS — Retiro (AFORE) | ~1.13% |
| IMSS — Guarderías y Prestaciones | ~1.00% |
| ISR 2024 monthly table | 1.92% → 35% (10 brackets) |

### 🇺🇸 USA — USD *(New in v1.1)*

| Deduction | Rate |
|-----------|------|
| Social Security | 6.2% (cap $168,600/yr) |
| Medicare | 1.45% |
| Federal Income Tax 2024 | 10% → 37% (7 brackets, std. deduction $14,600) |

### 🇨🇷 Costa Rica — CRC ₡ *(New in v1.1)*

| Deduction | Rate |
|-----------|------|
| CCSS — Enfermedad y Maternidad | 5.5% |
| CCSS — Invalidez, Vejez y Muerte | 3.84% |
| CCSS — Banco Popular + ASFA | ~1.0% |
| Impuesto sobre la Renta 2024 | 0% → 10% → 15% → 20% → 25% |

> ISR exento: ≤ ₡929,000/mo · Applied on base after CCSS

### 🇵🇪 Peru — PEN S/ *(New in v1.1)*

| Deduction | Rate |
|-----------|------|
| ONP (Pensión) | 13% |
| Impuesto a la Renta 2024 | 8% → 30% (5 tramos, deducción 7 UIT) |

> UIT 2024 = S/ 5,150 · Deducción anual = 7 UIT = S/ 36,050

---

## 📋 The 8 Steps

| Step | Name | What you fill in |
|------|------|-----------------|
| 1 | **Profile** | Name + country (6 available) |
| 2 | **Goal** | Savings target + deadline month/year |
| 3 | **Income** | Gross salary + real-time tax preview |
| 4 | **Home** | Rent, internet, electricity, water, mobile |
| 5 | **Debts** | Loans, car expenses, pet costs |
| 6 | **Leisure** | Food, dining out, streaming, subscriptions |
| 7 | **Extras** | 3 custom expense fields |
| 8 | **Results** | Full breakdown + charts + goal projection + PDF |

---

## 🖥️ Requirements

```bash
pip install reportlab pillow
```

| Package | Purpose |
|---------|---------|
| Python 3.10+ | Runtime — Python 3.14 fully supported ✅ |
| `pillow` | PIL icon rendering, bar chart, projection chart |
| `reportlab` | PDF export |
| `tkinter` | GUI — bundled on Windows & macOS · Linux: `sudo apt install python3-tk` |

---

## 📦 Build .exe

```bat
pip install pyinstaller pillow reportlab

pyinstaller --onefile --windowed ^
  --name "SalaryGoalsCalculator" ^
  --icon "assets\icon.ico" ^
  --add-data "assets;assets" ^
  --hidden-import reportlab ^
  --hidden-import PIL ^
  --hidden-import PIL.ImageFont ^
  --hidden-import PIL.ImageDraw ^
  --collect-all reportlab ^
  --collect-all PIL ^
  Calculadora_Ahorro.py
```

Or run **`build.bat`** — installs dependencies, runs PyInstaller, and compiles the Inno Setup installer automatically if Inno Setup 6 is detected.

Output → `dist\SalaryGoalsCalculator.exe`
Installer → `Output\SalaryGoalsCalculator_v1.1_Setup.exe`

---

## 💾 Session Files

No cloud, no account. Saved locally as JSON:

| OS | Path |
|----|------|
| Windows | `C:\Users\YourName\.salary_calc_sessions.json` |
| macOS | `/Users/YourName/.salary_calc_sessions.json` |
| Linux | `/home/yourname/.salary_calc_sessions.json` |

---

## 📁 Project Structure

```
Calculadora-de-Salario-Calculadora-de-metas/
│
├── Calculadora_Ahorro.py        ← Full application — single file, ~2,760 lines
├── assets/
│   └── icon.ico                 ← App icon (256/128/64/48/32/16px)
├── installer.iss                ← Inno Setup script → Windows installer
├── build.bat                    ← One-click: PyInstaller + Inno Setup
├── requirements.txt             ← pip dependencies
├── README.md                    ← This file
├── CHANGELOG.txt                ← Full version history
└── LICENSE                      ← GPL-3.0
```

---

## 🗺️ Roadmap

### ✅ Released

| Version | Date | Highlights |
|---------|------|-----------|
| v0.1 Beta | 2024 | Panama 🇵🇦 · Bilingual EN/ES · PDF export |
| v0.2 Beta | 2024 | Colombia 🇨🇴 · Dark mode · Sessions |
| ~~v0.3 Beta~~ | *cancelled* | *Merged into v1.0 RC* |
| v1.0 RC | Mar 15, 2026 | Full Fluent UI · Mexico 🇲🇽 · Python 3.14 fix |
| **v1.1** | **Mar 24, 2026** | **USA 🇺🇸 · Costa Rica 🇨🇷 · Peru 🇵🇪 · Charts · Hover details · Release Notes** |

### 🔜 Planned

<details>
<summary><b>v1.2 — UI/UX Deep Polish</b></summary>

- Mica material effect (Windows 11 background blur via `ctypes`)
- Acrylic frosted glass sidebar
- Animated page transitions between steps
- Custom borderless Win11-style title bar
- Accent color picker
- Compact mode for 1280×720 screens
- Font size scaling for accessibility

</details>

<details>
<summary><b>v1.3 — Power Features</b></summary>

- Multiple savings goals (up to 5) with individual progress rings
- Month-by-month budget history
- Export to Excel (.xlsx) with embedded charts
- Recurring expense templates
- Salary negotiation what-if slider
- Debt payoff calculator
- Bonus / 13th month income support

</details>

<details>
<summary><b>v2.0 — Platform Expansion</b></summary>

- Android APK (Kivy/BeeWare — prototype exists)
- Web version (PyScript or React)
- Optional encrypted cloud session sync
- Live exchange rate API (COP / MXN / CRC / PEN ↔ USD)

</details>

---

## 🤝 Contributing

| What | How |
|------|-----|
| 🐛 Bug report | [Open an Issue](https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas/issues) |
| 🌍 New country | Open an Issue with official deduction rates |
| 🌐 New language | Translation dict is in one place — easy to extend |
| ✨ Feature idea | Open an Issue or Discussion |
| 🔧 Code fix | Pull Request welcome |

---

## ⚠️ Disclaimer / Aviso Legal

All tax calculations are **estimates** based on publicly available official rates for 2024–2026. Actual deductions may differ due to employer agreements, bonuses, or legislative changes. For **informational and planning purposes only** — always verify with your pay stub or a certified accountant.

*Los cálculos son estimados. Las deducciones reales pueden variar. Solo para fines informativos. Verifica con tu recibo oficial o un contador.*

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**.

```
Copyright (c) 2026 Erick Perez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

See [LICENSE](LICENSE) · [GPL-3.0 on choosealicense.com](https://choosealicense.com/licenses/gpl-3.0/)

---

<div align="center">

Made with ❤️ in Panama 🇵🇦 by **[Erick Perez](https://github.com/eperez98)**

*"Un ahorro mensual constante tiene un gran impacto a largo plazo."*
*"Consistent monthly savings, even small amounts, have a huge long-term impact."*

<br>

⭐ **Star the repo if this project helped you!** ⭐

**[github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas](https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas)**

</div>
