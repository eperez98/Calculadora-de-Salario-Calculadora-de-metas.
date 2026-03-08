<div align="center">

# 💰 Salary & Goals Calculator
### Calculadora de Salario & Metas

**by Erick Perez**

[![Version](https://img.shields.io/badge/version-v1.0_RC-0067c0?style=flat-square&logo=python&logoColor=white)](https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas)
[![Released](https://img.shields.io/badge/released-03%2F15%2F2026-0067c0?style=flat-square)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-Release_Candidate-brightgreen?style=flat-square)]()
[![Countries](https://img.shields.io/badge/countries-🇵🇦_Panama_|_🇨🇴_Colombia_|_🇲🇽_Mexico-blue?style=flat-square)]()
[![UI](https://img.shields.io/badge/UI-Fluent_Win11-60cdff?style=flat-square)]()

**Release Date: March 15, 2026**

*A bilingual desktop app to calculate your real take-home pay, plan monthly budgets, and track savings goals — with a native-feeling Windows 11 Fluent Design interface.*

*Una app de escritorio bilingüe para calcular tu salario neto real, planificar presupuestos y alcanzar tus metas de ahorro — con interfaz Fluent Design estilo Windows 11.*

</div>

---

## 🆕 v1.0 RC — What Changed From v0.2 Beta

> **Note on versioning:** Beta v0.3 was never publicly released. All work done during the v0.3 development cycle was folded directly into v1.0 RC — this is why the jump appears large. See `CHANGELOG.txt` for the full detailed history.

This is the first **production-ready release candidate**, released **March 15, 2026**. The entire UI was rebuilt from scratch. No more beta labels.

| Area | v0.2 Beta | v1.0 RC |
|------|-----------|---------|
| **App status** | Beta — unstable, in development | ✅ Release Candidate — production ready |
| **Release date** | — | March 15, 2026 |
| **Countries** | Panama 🇵🇦, Colombia 🇨🇴 | + Mexico 🇲🇽 (IMSS + ISR 2024 table) |
| **Navigation** | Single horizontal step bar only | Vertical sidebar pane + horizontal breadcrumb pips |
| **Icons** | Unicode text characters | PIL-generated anti-aliased circle & pill icons (2× LANCZOS) |
| **Buttons** | Flat colored blocks | Fluent press / hover / release states with optional icon compound |
| **Input fields** | Plain 1px border box | Bottom accent bar animates on focus (Win11 text field spec) |
| **Cards** | Simple frame with left accent | White surface + 1px border + 2px drop-shadow strip |
| **Section headers** | Bold text + thin underline | Colored pill badge + bold title + accent separator |
| **Animations** | Basic `after()` slide counter | `Tweener` engine — 60 fps, cubic / quad / spring easing |
| **Results page** | Flat labeled value list | Circular progress ring + animated count-up from zero |
| **Tooltips** | None | Dark popup on hover for every input field |
| **Light theme** | Win11 Light (basic) | Full Fluent Win11 Light (#f3f3f3 / #0067c0) as default |
| **Dark theme** | Basic dark toggle | Full Win11 Dark (#202020 / #60cdff) with all Fluent tokens |
| **Python 3.14** | Crashed on launch (dual `tk.Tk`) | ✅ Fixed — single root, `root.update()` gate, no Toplevel before init |
| **Emoji in UI** | Flickering / crash on Windows PIL | ✅ All icons replaced with PIL-drawn ASCII symbols |
| **Splash screen** | `Toplevel` window (crash-prone) | Drawn directly on root canvas — zero crash risk |
| **Language boot** | Toplevel dialog (crash-prone) | Drawn directly on root — single `tk.Tk` architecture |
| **Session management** | Save/load local JSON | Same + improved popup dialogs |
| **Dependencies** | `reportlab` only | `reportlab` + `pillow` |

---

## ✨ Full Feature List

| | Feature | English | Español |
|--|---------|---------|---------|
| 🌐 | **Language boot screen** | Pick EN/ES before the app loads | Elige EN/ES antes de que cargue la app |
| ☽ | **Dark / Light mode** | Fluent Win11 light default + dark | Modo claro Fluent (default) + oscuro |
| 💾 | **Save & load sessions** | Name and store your data locally | Guarda y recarga tus datos por nombre |
| 🎬 | **Animated splash** | Language-aware intro with progress bar | Animación con barra de progreso |
| 🧭 | **Sidebar navigation** | Click any visited step to jump back | Toca cualquier paso visitado para volver |
| 🔵 | **Breadcrumb step bar** | Horizontal pips with live state colors | Pasos con colores según estado actual |
| 🖼 | **PIL icon system** | Anti-aliased circles & pills, no files | Iconos generados en RAM, sin archivos |
| 💬 | **Tooltips** | Hover any label for a hint popup | Hover cualquier campo para ver una pista |
| ⭕ | **Progress ring** | Savings % as animated circular arc | % de ahorro como arco circular animado |
| 🔢 | **Animated counters** | Results count up from 0 on load | Resultados cuentan desde 0 con easing |
| 🇵🇦 | **Panama taxes** | CSS 9.75% + Edu 1.25% + ISR progressive | CSS + Seg. Educativo + ISR progresivo |
| 🇨🇴 | **Colombia taxes** | Pension + Health + Retención UVT 2024 | Pensión + Salud + Retención en la fuente |
| 🇲🇽 | **Mexico taxes** | IMSS ~5.25% + ISR 2024 monthly table | IMSS + ISR tabla mensual 2024 |
| 💱 | **Local currency** | USD, COP, MXN — auto-formatted | Montos en USD, COP o MXN según país |
| 📋 | **Pay stub override** | Enter your actual received salary | Ingresa el salario real del recibo de pago |
| 📊 | **Full expense breakdown** | 7 categories + 3 custom extras | 7 categorías + 3 extras personalizados |
| 🎯 | **Goal analysis** | Projection, months left, deficit/surplus | Proyección, meses restantes, déficit |
| 📄 | **PDF export** | Full bilingual formatted report | Reporte completo bilingüe |
| 🔄 | **Multi-session** | New query without reopening the app | Nueva consulta sin cerrar la app |

---

## 🌍 Supported Countries / Países Soportados

### 🇵🇦 Panama / Panamá — USD ($)

| Deduction | Rate |
|-----------|------|
| CSS — Social Security (employee) | 9.75% of gross |
| Educational Insurance | 1.25% of gross |
| ISR — Progressive income tax | 0% (≤ $11,000/yr) → 15% (≤ $50,000/yr) → 25% (above) |

### 🇨🇴 Colombia — COP ($)

| Deduction | Rate |
|-----------|------|
| Pensión (employee share) | 4% of gross |
| Salud (employee share) | 4% of gross |
| Retención en la Fuente | Progressive — UVT 2024 ($47,065 COP) |

> Retención brackets: 0% (≤ 95 UVT/yr) → 19% → 28% → 33% → 35% → 37% → 39% (> 2,300 UVT/yr)

### 🇲🇽 Mexico / México — MXN ($) — *Added in v1.0 RC*

| Deduction | Rate |
|-----------|------|
| IMSS — Enfermedad y Maternidad | ~2.50% |
| IMSS — Invalidez y Vida | ~0.63% |
| IMSS — Retiro (AFORE) | ~1.13% |
| IMSS — Guarderías y Prestaciones Sociales | ~1.00% |
| ISR — Progressive monthly table (2024) | 1.92% → 35% across 10 brackets |

---

## 🖥️ Requirements / Requisitos

```bash
pip install reportlab pillow
```

| Package | Purpose |
|---------|---------|
| **Python 3.10+** | Core runtime — Python 3.14 fully supported ✅ |
| **reportlab** | PDF report export |
| **pillow** | PIL icon rendering (circle/pill badges, anti-aliased) |
| **tkinter** | GUI — bundled with Python on Windows & macOS. Linux: `sudo apt install python3-tk` |

---

## ▶️ How to Run / Cómo Ejecutar

```bash
git clone https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas.git
cd Calculadora-de-Salario-Calculadora-de-metas

pip install reportlab pillow

python Calculadora_Ahorro.py
```

**Launch sequence:**
1. 🌐 Language selection screen — pick EN or ES
2. 🎬 Animated splash screen with bouncing coin + progress bar
3. 💰 8-step calculator with sidebar + breadcrumb navigation

---

## 🏗️ Build .exe (Windows)

```bash
pip install pyinstaller

pyinstaller --onefile --windowed ^
  --name "SalaryGoalsCalculator" ^
  --hidden-import reportlab ^
  --hidden-import PIL ^
  --hidden-import PIL.ImageFont ^
  --hidden-import PIL.ImageDraw ^
  --collect-all reportlab ^
  --collect-all PIL ^
  Calculadora_Ahorro.py
```

Output: `dist/SalaryGoalsCalculator.exe` — no Python required for end users.

---

## 💾 Session Storage

No cloud, no account. Data is saved as JSON on your machine:

| OS | Path |
|----|------|
| Windows | `C:\Users\YourName\.salary_calc_sessions.json` |
| macOS | `/Users/YourName/.salary_calc_sessions.json` |
| Linux | `/home/yourname/.salary_calc_sessions.json` |

Each session stores: all form data, country, language, dark mode state, current step, and save date. Delete sessions from the Load dialog inside the app.

---

## 🗺️ Version History

### ✅ v0.1 Beta — Panama Launch *(Initial Release)*
- Panama CSS + Educational Insurance + Progressive ISR
- Bilingual EN/ES interface, 8-step form
- PDF export via reportlab

### ✅ v0.2 Beta — Multi-Country *(Last public Beta)*
- Language boot screen (pick EN/ES before splash loads)
- Dark / Light mode toggle
- Save & load named sessions (local JSON)
- Colombia 🇨🇴 — pension + health + retención en la fuente + COP formatting
- Country flag previews in combobox

### ⛔ v0.3 Beta — Cancelled *(Merged into v1.0 RC)*
> Development of v0.3 Beta was underway but never publicly released.
> All v0.3 work — Mexico taxes, Win11 UI, new animation engine — was folded directly into v1.0 RC.
> See `CHANGELOG.txt` for the complete technical record.

### ✅ v1.0 RC — *Current release — March 15, 2026*
- **Full UI rebuild** — Fluent Win11 Design language throughout
- **Vertical sidebar** navigation pane with active state indicator bar
- **Horizontal breadcrumb** step pip bar with live state colors
- **PIL icon system** — 2× supersampled, LANCZOS downscaled, runtime-generated
- **Tweener animation engine** — 60fps, cubic / quad / spring easing curves
- **Circular progress ring** on results page
- **Tooltip system** on all input fields
- **Mexico 🇲🇽** — IMSS + ISR 2024 monthly table
- **Python 3.14 crash fix** — single `tk.Tk`, `root.update()` gate, no Toplevel before init
- **Emoji crash fix** — all UI icons replaced with ASCII via PIL (Windows-safe)
- USA removed (incomplete data — returns properly in v1.1)
- All Beta labels removed

---

## 🔮 Coming Soon / Próximamente

### 🚀 v1.1 — Charts & More Countries
- [ ] **Expense bar chart** — visual spending breakdown on results page
- [ ] **Savings projection line chart** — trajectory toward goal over time
- [ ] **USA 🇺🇸** — Federal + FICA (SS + Medicare) + State estimator, returning with complete 2025 data
- [ ] **Costa Rica 🇨🇷** — CCSS + Impuesto sobre la Renta
- [ ] **Peru 🇵🇪** — AFP/ONP + income tax
- [ ] **Hover detail cards** — click any result row to expand a full breakdown

### 🎨 v1.2 — UI/UX Deep Polish
- [ ] **Mica material effect** — Windows 11 translucent background blur via `ctypes`
- [ ] **Acrylic sidebar** — frosted glass navigation panel
- [ ] **Animated page transitions** — slide-in / slide-out between steps
- [ ] **Custom borderless title bar** — fully native Win11-style with minimize / maximize / close
- [ ] **Accent color picker** — choose your own theme highlight color
- [ ] **Compact mode** — smaller layout for lower-resolution screens (1280×720)
- [ ] **Font size scaling** — accessibility-friendly text size slider
- [ ] **Splash screen themes** — dark card, light card, minimal variants

### 📊 v1.3 — Power User Features
- [ ] **Multiple savings goals** — track up to 5 goals simultaneously with progress rings
- [ ] **Month-by-month budget history** — compare spending over time
- [ ] **Export to Excel (.xlsx)** — full data table + embedded charts
- [ ] **Recurring expense templates** — save and reuse common expense profiles
- [ ] **Salary negotiation mode** — what-if slider to visualize impact of a raise
- [ ] **Debt payoff calculator** — months to zero balance at current savings rate
- [ ] **Bonus / 13th month handling** — one-time income scenario support

### 📱 v2.0 — Platform Expansion
- [ ] **Android APK** — Kivy/BeeWare port (prototype exists, being rebuilt for v2.0)
- [ ] **Web version** — PyScript or standalone React build
- [ ] **Optional cloud sync** — encrypted session backup across devices
- [ ] **Live currency conversion** — exchange rates via public API

---

## 📁 Project Structure

```
salary-goals-calculator/
│
├── Calculadora_Ahorro.py   ← Entire application (~2,400 lines, single file)
├── README.md               ← This file
├── CHANGELOG.txt           ← Full version history and technical changelog
└── LICENSE                 ← MIT License
```

---

## ⚠️ Disclaimer / Aviso Legal

**English:** All tax calculations are **estimates** based on publicly available official rates for 2024–2025. Actual payroll deductions may differ due to benefits, bonuses, special agreements, or legislative changes. This tool is for **informational and planning purposes only**. Always verify with your official pay stub or a certified accountant.

**Español:** Todos los cálculos son **estimados** basados en tasas oficiales públicas de 2024–2025. Las deducciones reales pueden variar. Esta herramienta es solo para **fines informativos y de planificación**. Siempre verifica con tu recibo de pago oficial o un contador certificado.

---

## 🤝 Contributing / Contribuir

```
🐛 Bug report        → Open an Issue
🌍 New country       → Open an Issue with official deduction rates
✨ Feature request   → Open an Issue or start a Discussion
🔧 Code fix / PR     → Pull Requests welcome
```

---

## 📜 License

```
MIT License — Copyright (c) 2026 Erick Perez
Free to use, modify and distribute with attribution.
```

---

<div align="center">

Made with ❤️ by **Erick Perez** — Panama 🇵🇦

*"Un ahorro mensual constante tiene un gran impacto a largo plazo."*
*"Consistent monthly savings, even small amounts, have a huge long-term impact."*

⭐ **Star the repo if this helped you!**

**[github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas](https://github.com/eperez98/Calculadora-de-Salario-Calculadora-de-metas)**

</div>
