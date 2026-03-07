<div align="center">

# 💰 Salary & Goals Calculator
### Calculadora de Salario & Metas

**by Erick Perez**

[![Version](https://img.shields.io/badge/version-v0.2_BETA-blue?style=flat-square)](https://github.com)
[![Python](https://img.shields.io/badge/python-3.10+-yellow?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-BETA-orange?style=flat-square)]()
[![Countries](https://img.shields.io/badge/countries-🇵🇦_Panama_|_🇨🇴_Colombia-red?style=flat-square)]()

> ⚠️ **BETA VERSION IN DEVELOPMENT** — More countries, features and improvements coming soon.
>
> ⚠️ **VERSIÓN BETA EN DESARROLLO** — Próximamente más países, funcionalidades y mejoras.

---

*A bilingual desktop app to calculate your real take-home pay, plan monthly budgets, and track your savings goals — with a Windows 11-style interface.*

*Una app de escritorio bilingüe para calcular tu salario neto real, planificar presupuestos y alcanzar tus metas de ahorro — con interfaz estilo Windows 11.*

</div>

---

## 📸 Interface Preview

```
┌──────────────────────────────────────────────────────────────────────┐
│  💰  Salary & Goals Calculator — by Erick Perez    🌙  💾  📂  🇪🇸  🇺🇸 │
├────────┬────────┬──────────┬────────┬────────┬────────┬────────┬─────┤
│   ①   │   ②   │    ③    │   ④   │   ⑤   │   ⑥   │   ⑦   │  ⑧  │
│Profile │  Goal  │  Income  │  Home  │ Debts  │Leisure │ Extras │Result│
└────────┴────────┴──────────┴────────┴────────┴────────┴────────┴─────┘
```

---

## 🌐 Bilingual / Bilingüe

Fully available in **English 🇺🇸** and **Español 🇪🇸**.

On first launch, a dedicated language selection screen appears before the splash — choose your language once and the entire app, animations, labels, validations, and PDF report all follow. Switch again at any time from the toolbar.

---

## ✨ Features / Características

| | Feature | English | Español |
|--|---------|---------|---------|
| 🗣️ | **Language boot screen** | Pick EN/ES before the app loads | Elige EN/ES antes de que cargue la app |
| 🌙 | **Dark / Light mode** | Toggle theme instantly from toolbar | Cambia el tema al instante desde la barra |
| 💾 | **Save & load sessions** | Name and store your data locally | Guarda y recarga tus datos por nombre |
| 🎬 | **Animated splash** | Language-aware intro animation | Animación de inicio según el idioma elegido |
| 🧮 | **Real-time tax preview** | See net salary as you type gross | Ve el neto mientras escribes el bruto |
| 🇵🇦 | **Panama tax system** | CSS + Educational Insurance + ISR | CSS + Seg. Educativo + ISR progresivo |
| 🇨🇴 | **Colombia tax system** | Pension + Health + Income withholding | Pensión + Salud + Retención en la fuente |
| 💱 | **Local currency** | Amounts shown in USD or COP | Montos en USD o COP según el país |
| 📋 | **Pay stub override** | Enter your actual received salary | Ingresa el salario real de tu recibo de pago |
| 📊 | **Full expense breakdown** | 7 categories + 3 custom extras | 7 categorías + 3 extras personalizados |
| 🎯 | **Savings goal analysis** | Projection, months remaining, deficit | Proyección, meses restantes, déficit |
| 📄 | **PDF export** | Bilingual formatted report | Reporte bilingüe completo |
| 🔄 | **Multi-session** | Start a new query without reopening | Nueva consulta sin cerrar la app |

---

## 🌍 Supported Countries / Países Soportados

### 🇵🇦 Panama / Panamá — USD ($)

| Deduction | Rate |
|-----------|------|
| CSS (Social Security) | 9.75% of gross salary |
| Educational Insurance | 1.25% of gross salary |
| ISR — Progressive income tax | 0% (≤ $11,000/yr) → 15% (≤ $50,000/yr) → 25% (above) |

### 🇨🇴 Colombia — COP ($)

| Deduction | Rate |
|-----------|------|
| Pension (employee share) | 4% of gross salary |
| Health (employee share) | 4% of gross salary |
| *Retención en la Fuente* | Progressive — based on UVT 2024 ($47,065 COP) |

> Retención brackets: 0% (≤ 95 UVT/yr) → 19% → 28% → 33% → 35% → 37% → 39% (> 2,300 UVT/yr)

### 🔜 Coming Soon / Próximamente

| Country | Status |
|---------|--------|
| 🇨🇷 Costa Rica | Planned |
| 🇲🇽 México | Planned |
| 🇺🇸 United States | Planned |
| 🇵🇪 Perú | Planned |
| More on request | Open an issue! |

---

## 🖥️ Requirements / Requisitos

| Requirement | Notes |
|-------------|-------|
| **Python 3.10+** | [python.org/downloads](https://python.org/downloads) |
| **reportlab** | For PDF export — `pip install reportlab` |
| **tkinter** | Included with Python on Windows/macOS. Linux: `sudo apt install python3-tk` |

```bash
pip install reportlab
```

---

## ▶️ How to Run / Cómo Ejecutar

```bash
# Clone
git clone https://github.com/your-username/salary-goals-calculator.git
cd salary-goals-calculator

# Install dependency
pip install reportlab

# Run
python Calculadora_Ahorro.py
```

**First launch flow:**
1. 🌐 Language selection screen (EN / ES)
2. 🎬 Animated splash screen
3. 💰 Main 8-step calculator

---

## 🏗️ Build Standalone .exe (Windows)

Distribute as a single executable — no Python needed by the end user:

```bash
pip install pyinstaller

pyinstaller --onefile --windowed ^
  --name "SalaryGoalsCalculator" ^
  --hidden-import reportlab ^
  --collect-all reportlab ^
  Calculadora_Ahorro.py
```

Output: `dist/SalaryGoalsCalculator.exe`

---

## 💾 Session Storage

Sessions are saved locally as JSON — no cloud, no account needed:

| OS | Location |
|----|----------|
| Windows | `C:\Users\YourName\.salary_calc_sessions.json` |
| macOS | `/Users/YourName/.salary_calc_sessions.json` |
| Linux | `/home/yourname/.salary_calc_sessions.json` |

Each session stores: all form data, country, language preference, dark mode state, and the date saved. Delete individual sessions directly from the Load dialog inside the app.

---

## 📁 Project Structure

```
salary-goals-calculator/
│
├── Calculadora_Ahorro.py      ← Entire application (single file)
├── README.md               ← This file
└── LICENSE                 ← MIT License
```

No frameworks, no build system, no config files. One Python file + one pip package.

---

## 🗺️ Roadmap

### ✅ v0.1 — Panama Tax Only
- Panama CSS + Educational Insurance + Progressive ISR
- Bilingual EN/ES interface
- 8-step form with real-time tax preview
- PDF export, pay stub override

### ✅ v0.2 — Current Release
- Language boot screen (pick EN/ES before splash)
- Dark mode / Light mode toggle
- Save & load named sessions (local JSON)
- Colombia 🇨🇴 — pension + health + *retención en la fuente* + COP currency
- Country flag in dropdown, currency-aware formatting

### 🔜 v0.3 — Planned
- [ ] Costa Rica 🇨🇷 tax system (CCSS + IR)
- [ ] México 🇲🇽 tax system (IMSS + ISR)
- [ ] Expense breakdown charts in results view
- [ ] Monthly budget history

### 🔜 v0.4+
- [ ] USA 🇺🇸 federal + state tax estimator
- [ ] Multiple concurrent savings goals
- [ ] Export to Excel (.xlsx)
- [ ] Installer wizard (Inno Setup)

---

## 🤝 Contributing / Contribuir

All contributions welcome — especially:

- **🌍 New country tax systems** — open an issue with the official deduction rates for your country and I'll add it
- **🐛 Bug reports** — tested primarily on Windows 11; macOS/Linux reports appreciated  
- **🌐 Additional languages** — the translation system is a single dictionary, easy to extend
- **💡 Feature ideas** — open an issue to discuss

```
🐛 Bug report  → Open an Issue
🌍 New country → Open an Issue with tax rates
✨ Feature     → Open an Issue or PR
🔧 Code fix    → Pull Request welcome
```

---

## ⚠️ Disclaimer / Aviso Legal

**English:** All tax calculations in this application are **estimates** based on publicly available official rates as of 2024–2025. Actual payroll deductions may differ due to additional benefits, bonuses, special employment agreements, or legislative changes. This tool is for **informational and planning purposes only**. Always verify with your official pay stub or a certified accountant.

**Español:** Todos los cálculos de impuestos son **estimados** basados en tasas oficiales públicas de 2024–2025. Las deducciones reales pueden variar. Esta herramienta es solo para **fines informativos y de planificación**. Siempre verifica con tu recibo de pago oficial o un contador certificado.

---

## 📜 License

```
MIT License — Copyright (c) 2025 Erick Perez

Free to use, modify and distribute with attribution.
```

---

<div align="center">

Made with ❤️ by **Erick Perez** — Panama 🇵🇦

*"Un ahorro mensual constante tiene un gran impacto a largo plazo."*

*"Consistent monthly savings, even small amounts, have a huge long-term impact."*

⭐ If this helped you, consider starring the repo!

</div>
