<div align="center">


# Salary & Goals Calculator
### Calculadora de Salario & Metas

**by [Erick Perez](https://github.com/eperez98) — Panama 🇵🇦**

<p>
  <a href="https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas/releases/tag/v1.0RC">
    <img src="https://img.shields.io/badge/version-v1.0_RC-0067c0?style=for-the-badge&logo=python&logoColor=white" alt="Version">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/released-March_15,_2026-0067c0?style=for-the-badge" alt="Released">
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
</p>

<p>
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-countries">Countries</a> •
  <a href="#%EF%B8%8F-screenshots">Screenshots</a> •
  <a href="#-build-exe">Build .exe</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

*A bilingual desktop app that calculates your real take-home pay, breaks down your monthly expenses, and tells you exactly how long it will take to reach your savings goal — with a native Windows 11 Fluent Design interface.*

*Una app de escritorio bilingüe que calcula tu salario neto real, desglosa tus gastos mensuales y te dice exactamente cuánto tiempo tomará alcanzar tu meta de ahorro — con interfaz Fluent Design estilo Windows 11.*

</div>

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas.git
cd Calculadora-de-Salario-Calculadora-de-metas

# 2. Install dependencies (2 packages)
pip install reportlab pillow

# 3. Run
python Calculadora_Ahorro.py
```

> **No Python?** Download the pre-built Windows `.exe` from [Releases](https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas/releases) — no installation needed.

**On first launch:**
1. 🌐 Pick your language — **English** or **Español**
2. 🎬 Watch the animated splash screen
3. 💰 Fill in 8 guided steps and get your full financial picture

---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

**🧭 Navigation**
- Vertical Win11 sidebar — jump to any step
- Horizontal breadcrumb pip bar
- Progress tracked visually in real time

**📊 Results**
- Circular progress ring (savings % of income)
- Animated count-up numbers on load
- Color-coded status: on track / deficit / surplus
- Full expense breakdown by category

**🎨 Interface**
- Windows 11 Fluent Design throughout
- Light mode (default) + Dark mode
- Anti-aliased PIL icons — no image files
- Smooth 60fps animations (cubic/spring easing)
- Tooltips on every input field

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

</td>
</tr>
</table>

---

## 🌍 Countries

The app calculates your **real net salary** after all mandatory deductions for your country.

### 🇵🇦 Panama — USD

| Deduction | Employee Rate |
|-----------|--------------|
| CSS (Social Security) | 9.75% |
| Educational Insurance | 1.25% |
| ISR (Income Tax) | 0% → 15% → 25% progressive |

> ISR brackets: 0% on ≤ $11,000/yr · 15% on $11k–$50k · 25% above $50k

### 🇨🇴 Colombia — COP

| Deduction | Employee Rate |
|-----------|--------------|
| Pensión | 4% |
| Salud | 4% |
| Retención en la Fuente | Progressive — UVT 2024 |

> Retención: 0% (≤ 95 UVT/yr) → 19% → 28% → 33% → 35% → 37% → 39%

### 🇲🇽 Mexico — MXN

| Deduction | Employee Rate |
|-----------|--------------|
| IMSS — Enfermedad y Maternidad | ~2.50% |
| IMSS — Invalidez y Vida | ~0.63% |
| IMSS — Retiro (AFORE) | ~1.13% |
| IMSS — Guarderías y Prestaciones | ~1.00% |
| ISR (Income Tax 2024) | 1.92% → 35% (10 brackets) |

> 🔜 **Coming soon:** USA 🇺🇸 · Costa Rica 🇨🇷 · Peru 🇵🇪

---

## 🖥️ Screenshots

```
┌────────────────────────────────────────────────────────────────────────────┐
│ ●  Calculadora de Salario & Metas — by Erick Perez    ☽ Claro  💾  📂  ES EN │
├──────────────────────────────────────────────────────────────────────────── │
│              ①━━━②━━━③━━━④━━━⑤━━━⑥━━━⑦━━━⑧                │
│           Perfil  Goal Income Home Debts Leisure Extras Result             │
├──┬─────────────────────────────────────────────────────────────────────────┤
│$ │                                                                         │
│─ │  ╔══════════════════════════════════════════════════════════╗           │
│P │  ║  P  Tu Perfil                                    🇵🇦    ║           │
│  │  ║     Cuéntanos quién eres para personalizar tu reporte   ║           │
│  │  ╠══════════════════════════════════════════════════════════╣           │
│G │  ║  Nombre:  [ Erick Perez_________________ ]              ║           │
│  │  ║  País:    [ 🇵🇦 Panamá ▾ ]                             ║           │
│$ │  ║                                                           ║           │
│  │  ║  🇵🇦 Panama    🇨🇴 Colombia    🇲🇽 Mexico               ║           │
│H │  ╚══════════════════════════════════════════════════════════╝           │
│  │                                                                         │
│D │  ╔══════════════════════════════════════════════════════════╗           │
│  │  ║  Results Preview                                         ║           │
│L │  ║     ⭕ 23%    Net Income: $2,400    Savings: $550       ║           │
│  │  ╚══════════════════════════════════════════════════════════╝           │
├──┴─────────────────────────────────────────────────────────────────────────┤
│  ← Atrás          Paso 3 de 8                        Siguiente →           │
└────────────────────────────────────────────────────────────────────────────┘
     ↑ Sidebar                                    Fluent cards ↑
  (click any step                           Win11 Light / Dark theme
   to go back)
```

*Light mode shown. Dark mode available via the ☽ toggle in the title bar.*

---

## 📋 The 8 Steps

| Step | Name | What you fill in |
|------|------|-----------------|
| 1 | **Profile** | Name + country selection |
| 2 | **Goal** | Savings target amount + deadline |
| 3 | **Income** | Gross salary + real-time tax preview |
| 4 | **Home** | Rent/mortgage, internet, electricity, water, mobile |
| 5 | **Debts** | Loans, car expenses, pet costs |
| 6 | **Leisure** | Food, dining out, streaming, subscriptions |
| 7 | **Extras** | 3 custom expense fields with your own labels |
| 8 | **Results** | Full breakdown + goal projection + PDF export |

---

## 📦 Build .exe

Build a standalone Windows executable — no Python required for end users.

```bat
:: Install build tools
pip install pyinstaller pillow reportlab

:: Build
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

Output → `dist\SalaryGoalsCalculator.exe`

**Or use the one-click script:**
```bat
build.bat
```
The script installs dependencies, runs PyInstaller, and compiles the Inno Setup installer automatically if Inno Setup 6 is found.

**To build the installer** (produces `SalaryGoalsCalculator_v1.0RC_Setup.exe`):
1. Install [Inno Setup 6](https://jrsoftware.org/isdl.php)
2. Open `installer.iss` → press **F9**

---

## 💾 Session Files

Your data is saved locally — never uploaded anywhere.

| OS | Location |
|----|----------|
| Windows | `C:\Users\YourName\.salary_calc_sessions.json` |
| macOS | `/Users/YourName/.salary_calc_sessions.json` |
| Linux | `/home/yourname/.salary_calc_sessions.json` |

Each session stores all form values, country, language, theme, and save date. Sessions can be deleted from the Load dialog inside the app.

---

## 🖥️ Requirements

| Requirement | Notes |
|-------------|-------|
| Python 3.10+ | Python 3.14 fully supported ✅ |
| `pillow` | Icon rendering |
| `reportlab` | PDF export |
| `tkinter` | Bundled on Windows & macOS · Linux: `sudo apt install python3-tk` |

```bash
pip install reportlab pillow
```

---

## 📁 Project Structure

```
Calculadora-de-Salario-Calculadora-de-metas/
│
├── Calculadora_Ahorro.py        ← Full application — single file, ~2,400 lines
├── assets/
│   └── icon.ico                 ← App icon (256/128/64/48/32/16px)
├── installer.iss                ← Inno Setup script → Windows installer .exe
├── build.bat                    ← One-click build: PyInstaller + Inno Setup
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
| v0.2 Beta | 2024 | Colombia 🇨🇴 · Dark mode · Save/load sessions |
| ~~v0.3 Beta~~ | *cancelled* | *Merged into v1.0 RC* |
| **v1.0 RC** | **Mar 15, 2026** | **Full Fluent UI · Mexico 🇲🇽 · Python 3.14 fix · PIL icons · Animations** |

### 🔜 Planned

<details>
<summary><b>v1.1 — Charts & More Countries</b></summary>

- Expense breakdown bar chart on results page
- Savings projection line chart over time
- USA 🇺🇸 — Federal + FICA + State tax estimator
- Costa Rica 🇨🇷 — CCSS + Impuesto sobre la Renta
- Peru 🇵🇪 — AFP/ONP + income tax
- Hover detail cards on result rows

</details>

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
- Live exchange rate API (COP/MXN ↔ USD)

</details>

---

## 🤝 Contributing

Contributions are welcome — especially:

| What | How |
|------|-----|
| 🐛 Bug report | [Open an Issue](https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas/issues) |
| 🌍 New country tax system | Open an Issue with official deduction rates |
| 🌐 New language translation | The translation dict is in one place — easy to extend |
| ✨ Feature idea | Open an Issue or Discussion |
| 🔧 Code fix | Pull Request welcome |

---

## ⚠️ Disclaimer / Aviso Legal

All tax calculations are **estimates** based on publicly available official rates for 2024–2026. Actual deductions may differ due to employer agreements, bonuses, or legislative changes. This tool is for **informational and planning purposes only** — always verify with your official pay stub or a certified accountant.

*Los cálculos son **estimados** basados en tasas oficiales públicas. Las deducciones reales pueden variar. Solo para **fines informativos**. Siempre verifica con tu recibo oficial o un contador.*

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**.

```
Copyright (c) 2026 Erick Perez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
```

See [LICENSE](LICENSE) for full text · [GPL-3.0 on choosealicense.com](https://choosealicense.com/licenses/gpl-3.0/)

---

<div align="center">

Made with ❤️ in Panama 🇵🇦 by **[Erick Perez](https://github.com/eperez98)**

*"Un ahorro mensual constante tiene un gran impacto a largo plazo."*
*"Consistent monthly savings, even small amounts, have a huge long-term impact."*

<br>

⭐ **If this project helped you, give it a star!** ⭐

</div>
