# ============================================================
#  SALARY & GOALS CALCULATOR / CALCULADORA DE SALARIO & METAS
#  by Erick Perez  |  v1.0 RC — Release Date: 03/15/2026
#  Requires: pip install reportlab pillow
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import date
import os, sys, math, json, random, time, threading, colorsys

try:
    from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageFilter
    PIL_OK = True
except ImportError:
    PIL_OK = False

# ══════════════════════════════════════════════════════════
#  ICON / RESOURCE PATH  (works in dev and PyInstaller .exe)
# ══════════════════════════════════════════════════════════
def _resource_path(relative):
    """Return absolute path — handles PyInstaller --onefile bundle."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative)

_APP_ICON_PATH = _resource_path(os.path.join("assets", "icon.ico"))

def _set_window_icon(win):
    """Apply logo.ico to any tk window (title bar + taskbar)."""
    try:
        if os.path.isfile(_APP_ICON_PATH):
            win.iconbitmap(_APP_ICON_PATH)
    except Exception:
        pass  # icon is cosmetic — never crash over it


# ══════════════════════════════════════════════════════════
#  GLOBAL STATE
# ══════════════════════════════════════════════════════════
_LANG      = "es"
_DARK_MODE = False
_APP_REF   = None

SESSIONS_FILE = os.path.join(os.path.expanduser("~"), ".salary_calc_sessions.json")

def set_lang(lang):    global _LANG;      _LANG      = lang
def set_dark(v):       global _DARK_MODE; _DARK_MODE = v

def toggle_dark():
    global _DARK_MODE
    _DARK_MODE = not _DARK_MODE
    _rebuild_theme()
    if _APP_REF:
        _APP_REF._apply_theme()
        _APP_REF._change_lang(_LANG)

# ══════════════════════════════════════════════════════════
#  THEMES  — Fluent Win11
# ══════════════════════════════════════════════════════════

THEME_LIGHT = {
    "bg":           "#f3f3f3",
    "surface":      "#ffffff",
    "surface2":     "#f9f9f9",
    "surface3":     "#efefef",
    "sidebar_bg":   "#f0f0f0",
    "sidebar_sel":  "#e0e0f0",
    "sidebar_hover":"#e8e8e8",
    "accent":       "#0067c0",
    "accent_h":     "#1a86d4",
    "accent_dk":    "#004e8c",
    "accent_soft":  "#cce4f7",
    "text":         "#1a1a1a",
    "text2":        "#5a5a5a",
    "text3":        "#9a9a9a",
    "border":       "#e0e0e0",
    "border2":      "#c8c8c8",
    "success":      "#107c10",
    "success_bg":   "#dff6dd",
    "danger":       "#c42b1c",
    "danger_bg":    "#fde7e9",
    "warning":      "#9d5d00",
    "warning_bg":   "#fff4ce",
    "gold":         "#8a6914",
    "gold_bg":      "#fef9e7",
    "gold_border":  "#f0c040",
    "title_bar":    "#1f1f1f",
    "titlebar_txt": "#ffffff",
    "step_done":    "#107c10",
    "step_act":     "#0067c0",
    "step_pend":    "#c8c8c8",
    "input_bg":     "#ffffff",
    "input_border": "#aaaaaa",
    "input_focus":  "#0067c0",
    "btn_bg":       "#0067c0",
    "btn_fg":       "#ffffff",
    "btn_sec":      "#f3f3f3",
    "btn_sec_fg":   "#1a1a1a",
    "btn_acc":      "#0067c0",
    "btn_acc_fg":   "#ffffff",
    "note_bg":      "#fff4ce",
    "note_border":  "#f0b400",
    "tag_green":    "#107c10",
    "tag_blue":     "#0067c0",
    "tag_purple":   "#7719aa",
    "tag_red":      "#c42b1c",
    "tag_orange":   "#9d5d00",
    "cursor":       "#0067c0",
    "scrollbar":    "#c8c8c8",
    "prompt":       "#107c10",
    "card_shadow":  "#e0e0e0",
    "divider":      "#e0e0e0",
    "hover_overlay":"#00000008",
    "progress_bg":  "#e0e0e0",
}

THEME_DARK = {
    "bg":           "#202020",
    "surface":      "#2d2d2d",
    "surface2":     "#383838",
    "surface3":     "#404040",
    "sidebar_bg":   "#1a1a1a",
    "sidebar_sel":  "#2a2a40",
    "sidebar_hover":"#303030",
    "accent":       "#60cdff",
    "accent_h":     "#99e4ff",
    "accent_dk":    "#0067c0",
    "accent_soft":  "#0a3a5a",
    "text":         "#ffffff",
    "text2":        "#c0c0c0",
    "text3":        "#808080",
    "border":       "#454545",
    "border2":      "#555555",
    "success":      "#6ccb5f",
    "success_bg":   "#0d3b0d",
    "danger":       "#ff6b6b",
    "danger_bg":    "#3b0d0d",
    "warning":      "#fce100",
    "warning_bg":   "#3b3300",
    "gold":         "#fce100",
    "gold_bg":      "#2a2500",
    "gold_border":  "#a08000",
    "title_bar":    "#1a1a1a",
    "titlebar_txt": "#ffffff",
    "step_done":    "#6ccb5f",
    "step_act":     "#60cdff",
    "step_pend":    "#454545",
    "input_bg":     "#2d2d2d",
    "input_border": "#555555",
    "input_focus":  "#60cdff",
    "btn_bg":       "#60cdff",
    "btn_fg":       "#000000",
    "btn_sec":      "#383838",
    "btn_sec_fg":   "#ffffff",
    "btn_acc":      "#60cdff",
    "btn_acc_fg":   "#000000",
    "note_bg":      "#2a2500",
    "note_border":  "#a08000",
    "tag_green":    "#1a6b1a",
    "tag_blue":     "#004e8c",
    "tag_purple":   "#5c1a7a",
    "tag_red":      "#8b1a1a",
    "tag_orange":   "#6b3d00",
    "cursor":       "#60cdff",
    "scrollbar":    "#555555",
    "prompt":       "#6ccb5f",
    "card_shadow":  "#181818",
    "divider":      "#454545",
    "hover_overlay":"#ffffff10",
    "progress_bg":  "#404040",
}

W11 = dict(THEME_LIGHT)

def _rebuild_theme():
    W11.clear()
    W11.update(THEME_DARK if _DARK_MODE else THEME_LIGHT)

# ══════════════════════════════════════════════════════════
#  FONTS
# ══════════════════════════════════════════════════════════
import platform
_os = platform.system()
if _os == "Windows":
    FONT_UI   = "Segoe UI"
    FONT_MONO = "Consolas"
elif _os == "Darwin":
    FONT_UI   = "SF Pro Display"
    FONT_MONO = "Menlo"
else:
    FONT_UI   = "Ubuntu"
    FONT_MONO = "DejaVu Sans Mono"

FONT    = FONT_UI
MONO    = FONT_MONO
F_TITLE = (FONT, 20, "bold")
F_SUBH  = (FONT, 11, "bold")
F_BODY  = (FONT, 10)
F_SMALL = (FONT, 9)
F_INPUT = (FONT, 10)
F_BTN   = (FONT, 10)
F_LABEL = (FONT, 9)
F_MONO  = (MONO, 9)
F_TAG   = (FONT, 8, "bold")
F_HEAD  = (FONT, 13, "bold")

# ══════════════════════════════════════════════════════════
#  PIL ICON SYSTEM — crisp vector-quality icons, no files
# ══════════════════════════════════════════════════════════

_icon_cache: dict = {}

def _hex_to_rgb(c):
    c = c.lstrip("#")
    return (int(c[0:2],16), int(c[2:4],16), int(c[4:6],16), 255)

def _get_font(size):
    candidates = [
        "segoeuib.ttf","segoeui.ttf","arial.ttf","arialbd.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for f in candidates:
        try:  return ImageFont.truetype(f, size)
        except: pass
    return ImageFont.load_default()

def _draw_circle_icon(size, bg, fg, sym, scale=0.45):
    if not PIL_OK: return None
    key = f"ci_{size}_{bg}_{fg}_{sym}"
    if key in _icon_cache: return _icon_cache[key]
    # 2× supersampled for anti-aliased result
    S = size * 2
    img  = Image.new("RGBA", (S, S), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([2,2,S-2,S-2], fill=_hex_to_rgb(bg))
    fnt  = _get_font(int(S * scale))
    bbox = draw.textbbox((0,0), sym, font=fnt)
    tw,th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text(((S-tw)//2-bbox[0], (S-th)//2-bbox[1]), sym, font=fnt, fill=_hex_to_rgb(fg))
    img  = img.resize((size,size), Image.LANCZOS)
    ph   = ImageTk.PhotoImage(img)
    _icon_cache[key] = ph
    return ph

def _draw_pill_icon(w, h, bg, fg, sym, r=6, scale=0.38):
    if not PIL_OK: return None
    key = f"pill_{w}_{h}_{bg}_{fg}_{sym}"
    if key in _icon_cache: return _icon_cache[key]
    W2,H2 = w*2,h*2
    img  = Image.new("RGBA",(W2,H2),(0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([2,2,W2-2,H2-2], radius=r*2, fill=_hex_to_rgb(bg))
    fnt  = _get_font(int(min(W2,H2)*scale))
    bbox = draw.textbbox((0,0),sym,font=fnt)
    tw,th= bbox[2]-bbox[0],bbox[3]-bbox[1]
    draw.text(((W2-tw)//2-bbox[0],(H2-th)//2-bbox[1]),sym,font=fnt,fill=_hex_to_rgb(fg))
    img  = img.resize((w,h),Image.LANCZOS)
    ph   = ImageTk.PhotoImage(img)
    _icon_cache[key] = ph
    return ph

def _draw_sidebar_icon(sym, bg, fg, size=36):
    """Large icon for sidebar nav items."""
    return _draw_circle_icon(size, bg, fg, sym, scale=0.42)

def make_step_icon(num, state="pending", size=26):
    colors = {
        "done":    (W11["step_done"], "#ffffff", "✓"),
        "active":  (W11["step_act"],  "#ffffff", str(num)),
        "pending": (W11["step_pend"], W11["text3"], str(num)),
    }
    bg, fg, sym = colors.get(state, colors["pending"])
    return _draw_circle_icon(size, bg, fg, sym, scale=0.42)

# Sidebar step icons — resolved at runtime so theme changes propagate
_STEP_ICON_SYMS = ["P", "G", "$", "H", "D", "L", "+", "R"]
_STEP_ICON_KEYS = ["tag_blue","tag_purple","tag_green","accent",
                   "tag_red","tag_orange","tag_purple","step_done"]

def _get_step_icon_colors(i):
    return (_STEP_ICON_SYMS[i], W11[_STEP_ICON_KEYS[i]], "#ffffff")

# Keep STEP_ICONS as a compat shim (rebuilt on demand)
STEP_ICONS = [(s, "#0067c0", "#ffffff") for s in _STEP_ICON_SYMS]

def make_sidebar_icon(step, active=False, size=32):
    sym, bg, fg = _get_step_icon_colors(step)
    if not active:
        bg = W11["surface3"]
        fg = W11["text3"]
    return _draw_circle_icon(size, bg, fg, sym, scale=0.44)

def make_btn_icon(sym, bg, fg, w=22, h=22):
    return _draw_pill_icon(w, h, bg, fg, sym, r=5, scale=0.40)

# ══════════════════════════════════════════════════════════
#  EASING / ANIMATION ENGINE
# ══════════════════════════════════════════════════════════

class Easing:
    @staticmethod
    def out_cubic(t):  return 1-(1-t)**3
    @staticmethod
    def out_quad(t):   return 1-(1-t)**2
    @staticmethod
    def in_out(t):     return t*t*(3-2*t)
    @staticmethod
    def spring(t):
        s=1.70158; t-=1; return t*t*((s+1)*t+s)+1

class Tweener:
    """One-shot value animator using after()."""
    def __init__(self, root):
        self._root = root

    def run(self, start, end, ms=220, ease=Easing.out_cubic,
            on_update=None, on_done=None, fps=60):
        frame_ms = max(8, 1000//fps)
        steps    = max(1, ms // frame_ms)
        counter  = [0]
        def tick():
            counter[0] += 1
            t   = min(counter[0]/steps, 1.0)
            val = start + (end-start)*ease(t)
            try:
                if on_update: on_update(val)
            except: pass
            if t < 1.0:
                self._root.after(frame_ms, tick)
            else:
                try:
                    if on_done: on_done()
                except: pass
        self._root.after(0, tick)

_tw = None   # set after root exists

def animate_count(label, end_val, pais, ms=550):
    """Animate a currency value label from 0 → end_val."""
    if _tw is None:
        try: label.config(text=f_v(end_val,pais))
        except: pass
        return
    _tw.run(0, end_val, ms, Easing.out_cubic,
            on_update=lambda v: _safe_cfg(label, text=f_v(v,pais)))

def _safe_cfg(widget, **kw):
    try: widget.config(**kw)
    except: pass

# ══════════════════════════════════════════════════════════
#  TOOLTIP SYSTEM
# ══════════════════════════════════════════════════════════

class Tooltip:
    def __init__(self, widget, text):
        self._w   = widget
        self._txt = text
        self._tip = None
        widget.bind("<Enter>", self._show, add="+")
        widget.bind("<Leave>", self._hide, add="+")

    def _show(self, e):
        if self._tip: return
        x = self._w.winfo_rootx() + 10
        y = self._w.winfo_rooty() + self._w.winfo_height() + 4
        self._tip = tk.Toplevel(self._w)
        self._tip.overrideredirect(True)
        self._tip.geometry(f"+{x}+{y}")
        self._tip.attributes("-alpha", 0.95)
        lbl = tk.Label(self._tip, text=self._txt, font=(FONT,9),
                       bg="#1f1f1f", fg="#ffffff", padx=10, pady=5)
        lbl.pack()

    def _hide(self, e):
        if self._tip:
            try: self._tip.destroy()
            except: pass
            self._tip = None

# ══════════════════════════════════════════════════════════
#  FLUENT WIDGETS
# ══════════════════════════════════════════════════════════

class FluentEntry(tk.Frame):
    """Input field with animated accent underline on focus (Win11 style)."""
    def __init__(self, parent, label="", prefix="", width=20, tooltip="", **kw):
        super().__init__(parent, bg=W11["surface"])

        if label:
            tk.Label(self, text=label, font=F_LABEL,
                     bg=W11["surface"], fg=W11["text2"], anchor="w"
                     ).pack(fill="x", pady=(0,2))

        # Card shell with border
        shell = tk.Frame(self, bg=W11["input_border"])
        shell.pack(fill="x")
        inner = tk.Frame(shell, bg=W11["input_bg"])
        inner.pack(fill="x", padx=1, pady=(1,0))

        if prefix:
            tk.Label(inner, text=prefix, font=(FONT,10),
                     bg=W11["input_bg"], fg=W11["text3"],
                     padx=8).pack(side="left")

        self.var   = tk.StringVar()
        self.entry = tk.Entry(inner, textvariable=self.var, font=F_INPUT,
                              bg=W11["input_bg"], fg=W11["text"],
                              relief="flat", width=width,
                              insertbackground=W11["cursor"],
                              selectbackground=W11["accent"],
                              selectforeground="#ffffff",
                              bd=0, highlightthickness=0)
        self.entry.pack(side="left", fill="x", expand=True,
                        padx=(0,8), pady=8)

        # Animated bottom bar
        self._bar = tk.Frame(shell, height=2, bg=W11["input_border"])
        self._bar.pack(fill="x")

        self._shell = shell
        self.entry.bind("<FocusIn>",  self._focus_in)
        self.entry.bind("<FocusOut>", self._focus_out)

        if tooltip:
            Tooltip(self, tooltip)

    def _focus_in(self, _):
        self._shell.config(bg=W11["input_focus"])
        self._bar.config(bg=W11["accent"])

    def _focus_out(self, _):
        self._shell.config(bg=W11["input_border"])
        self._bar.config(bg=W11["input_border"])

    def get(self):    return self.var.get()
    def set(self, v): self.var.set(str(v) if v else "")


class FluentCombo(tk.Frame):
    """Combobox with flag canvas and styled dropdown."""
    def __init__(self, parent, label="", values=[], width=20,
                 show_flags=False, **kw):
        super().__init__(parent, bg=W11["surface"])
        self._show_flags = show_flags

        if label:
            tk.Label(self, text=label, font=F_LABEL,
                     bg=W11["surface"], fg=W11["text2"], anchor="w"
                     ).pack(fill="x", pady=(0,2))

        row = tk.Frame(self, bg=W11["surface"])
        row.pack(fill="x")

        if show_flags:
            self._fc = tk.Canvas(row, bg=W11["surface"],
                                 width=46, height=30, highlightthickness=0)
            self._fc.pack(side="left", padx=(0,6), pady=2)

        s = ttk.Style()
        s.configure("Fluent.TCombobox",
                    fieldbackground=W11["input_bg"],
                    background=W11["surface"],
                    foreground=W11["text"],
                    selectbackground=W11["accent"],
                    selectforeground="#ffffff",
                    padding=6)
        s.map("Fluent.TCombobox",
              fieldbackground=[("readonly", W11["input_bg"])],
              foreground=[("readonly", W11["text"])])

        self.cb = ttk.Combobox(row, values=values, state="readonly",
                               font=F_INPUT, width=width,
                               style="Fluent.TCombobox")
        self.cb.pack(side="left", fill="x", expand=True)
        if values: self.cb.set(values[0])

        if show_flags:
            self.cb.bind("<<ComboboxSelected>>", self._update_flag)
            self._update_flag()

    def _update_flag(self, _=None):
        val = self.cb.get()
        self._fc.delete("all")
        c = next((p for p in FLAG_DRAW_FN if p in val), None)
        if c: FLAG_DRAW_FN[c](self._fc, 3, 4, 40, 22)

    def get(self):    return self.cb.get()
    def set(self, v):
        self.cb.set(v)
        if self._show_flags: self._update_flag()


class FluentButton(tk.Button):
    """Win11 Fluent button — pill shape, icon support, smooth hover/press."""
    def __init__(self, parent, text="", variant="primary",
                 icon_sym=None, command=None, **kw):
        MAP = {
            "primary": (W11["btn_bg"],   W11["btn_fg"],     W11["accent_h"],  W11["accent_dk"]),
            "accent":  (W11["btn_acc"],  W11["btn_acc_fg"], W11["accent_h"],  W11["accent_dk"]),
            "ghost":   (W11["btn_sec"],  W11["btn_sec_fg"], W11["border2"],   W11["border"]),
            "danger":  (W11["danger"],   "#ffffff",         "#e53935",        "#b71c1c"),
            "success": (W11["success"],  "#ffffff",         "#2e7d32",        "#1b5e20"),
        }
        bg, fg, hov, prs = MAP.get(variant, MAP["primary"])

        self._photo = None
        if icon_sym and PIL_OK:
            self._photo = make_btn_icon(icon_sym, bg, fg, 20, 20)

        kw_img = {"image": self._photo, "compound": "left"} if self._photo else {}
        super().__init__(parent, text=f"  {text}" if icon_sym else text,
                         font=F_BTN, bg=bg, fg=fg,
                         activebackground=hov, activeforeground=fg,
                         relief="flat", padx=16, pady=8,
                         cursor="hand2", command=command,
                         bd=0, highlightthickness=0, **kw_img, **kw)
        self._bg = bg; self._hov = hov; self._prs = prs
        self.bind("<Enter>",            lambda _: self.config(bg=self._hov))
        self.bind("<Leave>",            lambda _: self.config(bg=self._bg))
        self.bind("<ButtonPress-1>",    lambda _: self.config(bg=self._prs))
        self.bind("<ButtonRelease-1>",  lambda _: self.config(bg=self._hov))

# Backward compat aliases
TermEntry  = FluentEntry
TermCombo  = FluentCombo
TermButton = FluentButton


def fluent_card(parent, padx=20, pady=8):
    """Card with subtle drop-shadow strip (bottom 2px offset)."""
    shadow = tk.Frame(parent, bg=W11["card_shadow"])
    shadow.pack(fill="x", padx=padx, pady=pady)
    card = tk.Frame(shadow, bg=W11["surface"],
                    highlightbackground=W11["border"], highlightthickness=1)
    card.pack(fill="x", padx=0, pady=(0,2))
    return card

term_card = fluent_card
w11_card  = fluent_card


def section_title(parent, text, icon="", icon_sym=None):
    """Section header with colored pill icon and accent separator."""
    row = tk.Frame(parent, bg=W11["surface"])
    row.pack(fill="x", padx=16, pady=(14,4))

    if icon_sym and PIL_OK:
        sym_disp = icon_sym[:2] if len(icon_sym) > 2 else icon_sym
        ico = _draw_pill_icon(30, 22, W11["accent_soft"], W11["accent"],
                              sym_disp, r=5, scale=0.36)
        lbl = tk.Label(row, image=ico, bg=W11["surface"])
        lbl.pack(side="left", padx=(0,8))
        lbl._ico = ico

    tk.Label(row, text=text, font=F_SUBH,
             bg=W11["surface"], fg=W11["text"]).pack(side="left")
    tk.Frame(parent, bg=W11["divider"], height=1).pack(fill="x", padx=16, pady=(0,10))


def note_box(parent, text, color_bg=None, color_border=None, icon="ℹ"):
    bg  = color_bg    or W11["note_bg"]
    brd = color_border or W11["note_border"]
    f   = tk.Frame(parent, bg=bg, highlightbackground=brd, highlightthickness=1)
    f.pack(fill="x", padx=16, pady=(0,10))
    row = tk.Frame(f, bg=bg)
    row.pack(fill="x", padx=12, pady=10)
    tk.Label(row, text=icon, font=(FONT,11,"bold"),
             bg=bg, fg=W11["gold"]).pack(side="left", anchor="n", padx=(0,10))
    tk.Label(row, text=text, font=F_SMALL, bg=bg, fg=W11["text2"],
             wraplength=700, justify="left").pack(side="left", fill="x", expand=True)


def tag_pill(parent, text, bg_color):
    tk.Label(parent, text=f"  {text}  ", font=F_TAG,
             bg=bg_color, fg="#ffffff", pady=3, relief="flat"
             ).pack(side="left", padx=3)

tag_label = tag_pill   # alias


def progress_ring(canvas, cx, cy, r, pct, fg_color, bg_color, width=8):
    """Draw a circular progress arc on a canvas."""
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r, outline=bg_color, width=width)
    if pct > 0:
        extent = min(pct, 1.0) * 359.9
        canvas.create_arc(cx-r,cy-r,cx+r,cy+r,
                          start=90, extent=-extent,
                          style="arc", outline=fg_color, width=width)


# ══════════════════════════════════════════════════════════
#  FLUENT SIDEBAR + STEP BAR
# ══════════════════════════════════════════════════════════

class SideStepBar(tk.Frame):
    """Vertical sidebar navigation — Win11 Navigation Pane style."""
    def __init__(self, parent, on_step_click=None, **kw):
        super().__init__(parent, bg=W11["sidebar_bg"], width=56)
        self.pack_propagate(False)
        self._on_click = on_step_click
        self._btns     = []
        self._step     = 0

        # Top logo area
        logo = tk.Frame(self, bg=W11["sidebar_bg"], height=52)
        logo.pack(fill="x")
        logo.pack_propagate(False)
        # Dollar-sign pill
        ico = _draw_circle_icon(32, W11["accent"], "#ffffff", "$", 0.46) if PIL_OK else None
        if ico:
            lbl = tk.Label(logo, bg=W11["sidebar_bg"], image=ico)
            lbl._ico = ico
        else:
            lbl = tk.Label(logo, bg=W11["sidebar_bg"], text="$",
                           font=(FONT, 14, "bold"), fg=W11["accent"])
        lbl.pack(expand=True)

        tk.Frame(self, bg=W11["divider"], height=1).pack(fill="x", padx=8)
        tk.Frame(self, bg=W11["sidebar_bg"], height=6).pack()

    def build_steps(self, step_names):
        # Clear old
        for b in self._btns:
            try: b.destroy()
            except: pass
        self._btns.clear()

        for i, name in enumerate(step_names):
            btn = self._make_step_btn(i, name)
            self._btns.append(btn)

        tk.Frame(self, bg=W11["sidebar_bg"]).pack(expand=True, fill="both")

    def _make_step_btn(self, idx, name):
        """Each nav button: icon + label stacked, click → go to step."""
        f = tk.Frame(self, bg=W11["sidebar_bg"], cursor="hand2")
        f.pack(fill="x", pady=1)

        # Active indicator bar (left edge)
        bar = tk.Frame(f, bg=W11["sidebar_bg"], width=3)
        bar.pack(side="left", fill="y")

        ico_lbl = tk.Label(f, bg=W11["sidebar_bg"])
        ico_lbl.pack(pady=(6,0))

        name_lbl = tk.Label(f, text=name, font=(FONT,7),
                            bg=W11["sidebar_bg"], fg=W11["text3"])
        name_lbl.pack(pady=(0,6))

        btn_data = {"frame":f, "bar":bar, "ico":ico_lbl, "name":name_lbl}

        def click(event, i=idx):
            if self._on_click:
                self._on_click(i)

        for w in [f, ico_lbl, name_lbl]:
            w.bind("<Button-1>", click)
            w.bind("<Enter>", lambda e, fd=btn_data: self._hover(fd, True))
            w.bind("<Leave>", lambda e, fd=btn_data: self._hover(fd, False))

        return btn_data

    def _hover(self, d, entering):
        if d == self._btns[self._step] if self._step < len(self._btns) else False:
            return
        bg = W11["sidebar_hover"] if entering else W11["sidebar_bg"]
        d["frame"].config(bg=bg)
        d["ico"].config(bg=bg)
        d["name"].config(bg=bg)
        d["bar"].config(bg=bg)

    def update_step(self, step, step_names=None):
        self._step = step
        for i, d in enumerate(self._btns):
            is_active  = (i == step)
            is_done    = (i < step)
            state      = "active" if is_active else ("done" if is_done else "pending")
            bg         = W11["sidebar_sel"] if is_active else W11["sidebar_bg"]
            bar_bg     = W11["accent"]      if is_active else W11["sidebar_bg"]
            txt_fg     = W11["accent"]      if is_active else (W11["text2"] if is_done else W11["text3"])
            txt_font   = (FONT,7,"bold")    if is_active else (FONT,7)

            d["frame"].config(bg=bg)
            d["bar"].config(bg=bar_bg)
            d["name"].config(bg=bg, fg=txt_fg, font=txt_font)

            if PIL_OK:
                ico = make_sidebar_icon(i, active=is_active, size=28)
                d["ico"].config(image=ico, bg=bg)
                d["ico"]._ico = ico
            else:
                sym, c_bg, c_fg = STEP_ICONS[i]
                if not is_active:
                    c_bg = W11["surface3"]; c_fg = W11["text3"]
                d["ico"].config(text=sym, bg=bg, fg=c_fg)

            if step_names and i < len(step_names):
                d["name"].config(text=step_names[i])


class TopStepBar(tk.Frame):
    """Horizontal step pip bar shown ABOVE content (compact breadcrumb)."""
    def __init__(self, parent, **kw):
        super().__init__(parent, bg=W11["surface2"], height=44)
        self.pack_propagate(False)
        self._pips  = []
        self._lines = []
        self._inner = tk.Frame(self, bg=W11["surface2"])
        self._inner.place(relx=0.5, rely=0.5, anchor="center")

    def build(self, step_names):
        for w in self._inner.winfo_children(): w.destroy()
        self._pips.clear(); self._lines.clear()
        for i, name in enumerate(step_names):
            if i > 0:
                ln = tk.Frame(self._inner, bg=W11["border"], height=1, width=18)
                ln.pack(side="left", anchor="center", padx=0)
                self._lines.append(ln)
            col = tk.Frame(self._inner, bg=W11["surface2"])
            col.pack(side="left")
            pip = tk.Label(col, bg=W11["surface2"])
            pip.pack()
            self._pips.append(pip)

    def update_step(self, step, step_names=None):
        self.config(bg=W11["surface2"])
        self._inner.config(bg=W11["surface2"])
        for i, pip in enumerate(self._pips):
            state = "active" if i==step else ("done" if i<step else "pending")
            pip.master.config(bg=W11["surface2"])
            if PIL_OK:
                ico = make_step_icon(i+1, state, size=22)
                pip.config(image=ico, bg=W11["surface2"])
                pip._ico = ico
            else:
                colors = {"done":W11["step_done"],"active":W11["step_act"],"pending":W11["step_pend"]}
                syms   = {"done":"✓","active":str(i+1),"pending":str(i+1)}
                pip.config(text=syms[state], bg=colors[state],
                           fg="#ffffff", font=(FONT,8,"bold"), width=2)

        for i, ln in enumerate(self._lines):
            ln.config(bg=W11["step_done"] if i < step else W11["border"])



# ══════════════════════════════════════════════════════════
#  TRANSLATIONS
# ══════════════════════════════════════════════════════════
LANGS = {
    "es": {
        "app_title":        "Calculadora de Salario & Metas  —  by Erick Perez",
        "title_bar":        "  💰  Calculadora de Salario & Metas  —  by Erick Perez",
        "splash_sub":       "Calculadora de Salario & Metas",
        "splash_edition":   "v1.0 RC •  🇵🇦 🇨🇴 🇲🇽",
        "splash_loading":   ["Iniciando sistema...", "Cargando módulos...",
                             "Configurando impuestos...",
                             "Preparando interfaz...", "¡Listo!"],
        "back":             "← Atrás",
        "next":             "Siguiente →",
        "new_query":        "⟳  Nueva Consulta",
        "step_of":          "Paso {s} de {t}",
        "steps":            ["Perfil","Meta","Ingresos","Hogar","Deudas","Ocio","Extras","Resultado"],
        "dark_mode":        "☀ Claro",
        "light_mode":       "◐ Oscuro",
        "save_session":     "▼ Guardar",
        "load_session":     "▲ Cargar",
        "sessions_title":   "Sesiones Guardadas",
        "save_name_prompt": "Nombre para esta sesión:",
        "save_success":     "Sesión guardada: {name}",
        "save_error":       "No se pudo guardar la sesión.",
        "load_select":      "Selecciona una sesión:",
        "load_none":        "No hay sesiones guardadas.",
        "load_success":     "Sesión cargada: {name}",
        "delete_session":   "Eliminar",
        "cancel":           "Cancelar",
        "ok":               "OK",
        "req_name":         "Por favor ingresa tu nombre.",
        "req_field":        "Campo requerido",
        "req_meta":         "Ingresa una meta de ahorro válida.",
        "req_anio":         "Ingresa un año válido (ej: 2026).",
        "invalid_year":     "Año inválido",
        "req_salary":       "Ingresa tu salario mensual bruto.",
        "p0_title":         "Tu Perfil",
        "p0_sub":           "Cuéntanos quién eres para personalizar tu reporte.",
        "p0_section":       "Información Personal",
        "p0_name":          "Nombre completo *",
        "p0_country":       "País de residencia *",
        "p0_note":          "v1.0 RC — Disponible: Panamá 🇵🇦  Colombia 🇨🇴  México 🇲🇽 · Los cálculos son estimados.",
        "p1_title":         "Meta de Ahorro",
        "p1_sub":           "Define cuánto quieres ahorrar y para cuándo.",
        "p1_section":       "Tu Objetivo Financiero",
        "p1_meta":          "Meta de ahorro *",
        "p1_month":         "Mes objetivo *",
        "p1_year":          "Año objetivo *",
        "p1_tip":           "Un ahorro mensual constante, aunque sea pequeño, tiene un gran impacto a largo plazo.",
        "p2_title":         "Ingresos — {nombre}",
        "p2_sub":           "País: {pais}  |  Deducciones calculadas automáticamente.",
        "p2_section":       "Salario Mensual",
        "p2_gross":         "Salario mensual BRUTO *",
        "p2_extra":         "Ingresos extra este mes",
        "p2_imp_hint":      "Ingresa tu salario bruto para ver el desglose de deducciones",
        "p2_imp_title":     "Desglose estimado — {pais}",
        "p2_net_est":       "Salario Neto Estimado:",
        "p2_note":          "AVISO: El cálculo es un estimado basado en tasas oficiales. El monto real puede variar. Verifica con tu recibo de pago.",
        "p2_real":          "Salario REAL recibido (si difiere del estimado)",
        "p2_real_tip":      "Si lo dejas vacío se usará el neto estimado.",
        "p3_title":         "Gastos del Hogar",
        "p3_sub":           "Servicios básicos y vivienda.",
        "p3_section":       "Gastos Fijos Mensuales",
        "p3_rent":          "Alquiler / Hipoteca",
        "p3_internet":      "Factura de Internet Mensual",
        "p3_electric":      "Factura de Luz",
        "p3_water":         "Agua",
        "p3_mobile":        "Data Móvil / Celular",
        "p4_title":         "Deudas, Auto y Mascotas",
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
        "p5_title":         "Ocio y Suscripciones",
        "p5_sub":           "Entretenimiento, comida y plataformas digitales.",
        "p5_s1":            "Gastos Variables",
        "p5_grocery":       "Supermercado / Comida",
        "p5_out":           "Salidas / Entretenimiento",
        "p5_delivery":      "Delivery",
        "p5_s2":            "Suscripciones Digitales",
        "p6_title":         "Gastos Extra",
        "p6_sub":           "Cualquier gasto adicional que no encaje en las categorías anteriores.",
        "p6_section":       "Gastos Adicionales",
        "p6_extra":         "Gasto Extra {n}",
        "p6_desc":          "Descripción",
        "p6_hint":          "Al presionar Siguiente se calcularán todos tus resultados.",
        "p7_title":         "Resultados — {nombre}",
        "p7_sub":           "{pais}  ·  Meta: {sym}{meta:,.0f} para {mes} {anio}",
        "p7_deficit":       "DÉFICIT  {sym}{amt:,.0f}/mes  —  Gastos superan ingresos",
        "p7_ontrack":       "EN META  {sym}{amt:,.0f}/mes  —  ¡Alcanzarás tu objetivo!",
        "p7_need":          "PARCIAL  {sym}{amt:,.0f}/mes  —  Faltan {sym}{falta:,.0f} más/mes",
        "p7_salary_imp":    "Salario e Impuestos",
        "p7_total_ded":     "Total deducciones (estimado)",
        "p7_net_est":       "Salario Neto (estimado)",
        "p7_net_real":      "Salario Real (recibo)",
        "p7_imp_note":      "Estimado. Puede variar. Verifica con tu recibo de pago.",
        "p7_income":        "Ingresos",
        "p7_net_base":      "Salario Neto (base)",
        "p7_extra_inc":     "Ingreso Extra",
        "p7_total_inc":     "TOTAL INGRESOS",
        "p7_home":          "Hogar",
        "p7_rent":          "Alquiler",
        "p7_electric":      "Luz",
        "p7_water":         "Agua",
        "p7_mobile":        "Data Móvil",
        "p7_loans":         "Préstamos",
        "p7_loan_p":        "Préstamo personal",
        "p7_loan_a":        "Préstamo auto",
        "p7_debts":         "Otras deudas",
        "p7_auto_pets":     "Auto & Mascotas",
        "p7_gas":           "Gasolina",
        "p7_maint":         "Mantenimiento",
        "p7_pet_food":      "Comida mascotas",
        "p7_pet_vet":       "Veterinario",
        "p7_pet_other":     "Otros mascotas",
        "p7_vars":          "Variables & Suscripciones",
        "p7_grocery":       "Supermercado",
        "p7_out":           "Salidas",
        "p7_extras_sec":    "Gastos Extra",
        "p7_extra_lbl":     "Extra: {desc}",
        "p7_summary":       "Resumen Total",
        "p7_tot_inc":       "Total Ingresos",
        "p7_tot_exp":       "Total Gastos",
        "p7_saving":        "AHORRO MENSUAL",
        "p7_goal":          "Análisis de Meta",
        "p7_goal_amt":      "Meta de ahorro",
        "p7_months_left":   "Meses restantes",
        "p7_need_mo":       "Ahorro necesario/mes",
        "p7_curr_mo":       "Tu ahorro actual/mes",
        "p7_projection":    "Proyección total",
        "p7_export":        "▤  Exportar PDF",
        "p7_new":           "Usa 'Nueva Consulta' para empezar de nuevo.",
        "pdf_saved":        "PDF Generado",
        "pdf_saved_msg":    "Guardado en:\n{ruta}",
        "pdf_save_title":   "Guardar reporte PDF",
        "months":           ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
                             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
        "tax_css":          "CSS (9.75%)",
        "tax_edu":          "Seg. Educativo (1.25%)",
        "tax_isr_pa":       "ISR estimado",
        "tax_pension_co":   "Pensión (4%)",
        "tax_salud_co":     "Salud (4%)",
        "tax_renta_co":     "Retención Fuente",
        "tax_imss_mx":      "IMSS (6.1% aprox)",
        "tax_isr_mx":       "ISR estimado",
        "tax_ss_us":        "Social Security (6.2%)",
        "tax_medicare_us":  "Medicare (1.45%)",
        "tax_fed_us":       "Federal Tax (est.)",
        "pdf_title":        "Calculadora de Salario & Metas",
        "pdf_by":           "by Erick Perez",
        "pdf_date":         "Generado el {d}",
        "pdf_salary":       "Salario e Impuestos",
        "pdf_gross":        "Salario Bruto",
        "pdf_ded_est":      "Total Deducciones (estimado)",
        "pdf_net_est":      "Salario Neto Estimado",
        "pdf_net_real":     "Salario Real (recibo)",
        "pdf_note":         "NOTA: Calculo estimado. Verificar con recibo oficial.",
        "pdf_income":       "Ingresos",
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
        "pdf_loan_a":       "Prestamo Auto",
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
        "pdf_goal_amt":     "Meta",
        "pdf_objective":    "Objetivo: {mes} {anio}",
        "pdf_months_left":  "{n} meses restantes",
        "pdf_need_mo":      "Ahorro necesario/mes",
        "pdf_curr_mo":      "Ahorro actual/mes",
        "pdf_projection":   "Proyeccion total",
        "pdf_ok":           "EXCELENTE: Alcanzaras tu meta antes de {mes} {anio}.",
        "pdf_warn":         "ATENCION: Necesitas {sym}{n:,.0f} mas/mes.",
        "pdf_alert":        "ALERTA: Gastos superan ingresos.",
        "pdf_footer":       "Calculadora de Salario & Metas  •  by Erick Perez  •  {nombre}  •  {pais}",
    },
    "en": {
        "app_title":        "Salary & Goals Calculator  —  by Erick Perez",
        "title_bar":        "  💰  Salary & Goals Calculator  —  by Erick Perez",
        "splash_sub":       "Salary & Goals Calculator",
        "splash_edition":   "v1.0 RC •  🇵🇦 🇨🇴 🇲🇽",
        "splash_loading":   ["Booting system...", "Loading modules...",
                             "Configuring taxes...",
                             "Preparing interface...", "Ready!"],
        "back":             "← Back",
        "next":             "Next →",
        "new_query":        "⟳  New Query",
        "step_of":          "Step {s} of {t}",
        "steps":            ["Profile","Goal","Income","Home","Debts","Leisure","Extras","Results"],
        "dark_mode":        "☀ Light",
        "light_mode":       "◐ Dark",
        "save_session":     "▼ Save",
        "load_session":     "▲ Load",
        "sessions_title":   "Saved Sessions",
        "save_name_prompt": "Session name:",
        "save_success":     "Session saved: {name}",
        "save_error":       "Could not save session.",
        "load_select":      "Select a session:",
        "load_none":        "No saved sessions.",
        "load_success":     "Session loaded: {name}",
        "delete_session":   "Delete",
        "cancel":           "Cancel",
        "ok":               "OK",
        "req_name":         "Please enter your name.",
        "req_field":        "Required field",
        "req_meta":         "Enter a valid savings goal.",
        "req_anio":         "Enter a valid year (e.g. 2026).",
        "invalid_year":     "Invalid year",
        "req_salary":       "Enter your gross monthly salary.",
        "p0_title":         "Your Profile",
        "p0_sub":           "Tell us about yourself to personalize your report.",
        "p0_section":       "Personal Information",
        "p0_name":          "Full name *",
        "p0_country":       "Country of residence *",
        "p0_note":          "v1.0 RC — Available: Panama 🇵🇦  Colombia 🇨🇴  Mexico 🇲🇽 · All calculations are estimates.",
        "p1_title":         "Savings Goal",
        "p1_sub":           "Define how much you want to save and by when.",
        "p1_section":       "Your Financial Goal",
        "p1_meta":          "Savings goal *",
        "p1_month":         "Target month *",
        "p1_year":          "Target year *",
        "p1_tip":           "Consistent monthly savings, even small amounts, have a huge long-term impact.",
        "p2_title":         "Income — {nombre}",
        "p2_sub":           "Country: {pais}  |  Deductions calculated automatically.",
        "p2_section":       "Monthly Salary",
        "p2_gross":         "Gross monthly salary *",
        "p2_extra":         "Extra income this month",
        "p2_imp_hint":      "Enter your gross salary to see the deduction breakdown",
        "p2_imp_title":     "Estimated breakdown — {pais}",
        "p2_net_est":       "Estimated Net Salary:",
        "p2_note":          "NOTICE: Calculation is an estimate based on official rates. Actual amount may vary. Verify with your pay stub.",
        "p2_real":          "ACTUAL salary received (if different from estimate)",
        "p2_real_tip":      "Leave empty to use the estimated net salary.",
        "p3_title":         "Home Expenses",
        "p3_sub":           "Basic services and housing.",
        "p3_section":       "Fixed Monthly Expenses",
        "p3_rent":          "Rent / Mortgage",
        "p3_internet":      "Monthly Internet Bill",
        "p3_electric":      "Electricity Bill",
        "p3_water":         "Water",
        "p3_mobile":        "Mobile Data / Phone",
        "p4_title":         "Debts, Car & Pets",
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
        "p5_title":         "Leisure & Subscriptions",
        "p5_sub":           "Entertainment, food and digital platforms.",
        "p5_s1":            "Variable Expenses",
        "p5_grocery":       "Grocery / Food",
        "p5_out":           "Outings / Entertainment",
        "p5_delivery":      "Delivery",
        "p5_s2":            "Digital Subscriptions",
        "p6_title":         "Extra Expenses",
        "p6_sub":           "Any additional expense not fitting previous categories.",
        "p6_section":       "Additional Expenses",
        "p6_extra":         "Extra Expense {n}",
        "p6_desc":          "Description",
        "p6_hint":          "Pressing Next will calculate all your results.",
        "p7_title":         "Results — {nombre}",
        "p7_sub":           "{pais}  ·  Goal: {sym}{meta:,.0f} for {mes} {anio}",
        "p7_deficit":       "DEFICIT  {sym}{amt:,.0f}/mo  —  Expenses exceed income",
        "p7_ontrack":       "ON TRACK  {sym}{amt:,.0f}/mo  —  You'll reach your goal!",
        "p7_need":          "PARTIAL  {sym}{amt:,.0f}/mo  —  Need {sym}{falta:,.0f} more/mo",
        "p7_salary_imp":    "Salary & Taxes",
        "p7_total_ded":     "Total deductions (estimated)",
        "p7_net_est":       "Net Salary (estimated)",
        "p7_net_real":      "Actual Salary (pay stub)",
        "p7_imp_note":      "Estimated. May vary. Verify with your official pay stub.",
        "p7_income":        "Income",
        "p7_net_base":      "Net Salary (base)",
        "p7_extra_inc":     "Extra Income",
        "p7_total_inc":     "TOTAL INCOME",
        "p7_home":          "Home",
        "p7_rent":          "Rent",
        "p7_electric":      "Electricity",
        "p7_water":         "Water",
        "p7_mobile":        "Mobile Data",
        "p7_loans":         "Loans",
        "p7_loan_p":        "Personal loan",
        "p7_loan_a":        "Car loan",
        "p7_debts":         "Other debts",
        "p7_auto_pets":     "Car & Pets",
        "p7_gas":           "Gas",
        "p7_maint":         "Maintenance",
        "p7_pet_food":      "Pet food",
        "p7_pet_vet":       "Veterinarian",
        "p7_pet_other":     "Other pets",
        "p7_vars":          "Variable & Subscriptions",
        "p7_grocery":       "Grocery",
        "p7_out":           "Outings",
        "p7_extras_sec":    "Extra Expenses",
        "p7_extra_lbl":     "Extra: {desc}",
        "p7_summary":       "Total Summary",
        "p7_tot_inc":       "Total Income",
        "p7_tot_exp":       "Total Expenses",
        "p7_saving":        "MONTHLY SAVINGS",
        "p7_goal":          "Goal Analysis",
        "p7_goal_amt":      "Savings goal",
        "p7_months_left":   "Months remaining",
        "p7_need_mo":       "Required savings/mo",
        "p7_curr_mo":       "Your current savings/mo",
        "p7_projection":    "Total projection",
        "p7_export":        "▤  Export PDF",
        "p7_new":           "Use 'New Query' to start over.",
        "pdf_saved":        "PDF Generated",
        "pdf_saved_msg":    "Saved at:\n{ruta}",
        "pdf_save_title":   "Save PDF report",
        "months":           ["January","February","March","April","May","June",
                             "July","August","September","October","November","December"],
        "tax_css":          "CSS (9.75%)",
        "tax_edu":          "Educational Insurance (1.25%)",
        "tax_isr_pa":       "ISR (estimated)",
        "tax_pension_co":   "Pension (4%)",
        "tax_salud_co":     "Health (4%)",
        "tax_renta_co":     "Income Withholding",
        "tax_imss_mx":      "IMSS (~6.1%)",
        "tax_isr_mx":       "ISR (estimated)",
        "tax_ss_us":        "Social Security (6.2%)",
        "tax_medicare_us":  "Medicare (1.45%)",
        "tax_fed_us":       "Federal Tax (est.)",
        "pdf_title":        "Salary & Goals Calculator",
        "pdf_by":           "by Erick Perez",
        "pdf_date":         "Generated on {d}",
        "pdf_salary":       "Salary & Taxes",
        "pdf_gross":        "Gross Salary",
        "pdf_ded_est":      "Total Deductions (estimated)",
        "pdf_net_est":      "Estimated Net Salary",
        "pdf_net_real":     "Actual Salary (pay stub)",
        "pdf_note":         "NOTE: Estimated. Verify with your official pay stub.",
        "pdf_income":       "Income",
        "pdf_net_base":     "Net Salary (base)",
        "pdf_extra_inc":    "Extra Income",
        "pdf_total_inc":    "TOTAL INCOME",
        "pdf_home":         "Home Expenses",
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
        "pdf_warn":         "ATTENTION: You need {sym}{n:,.0f} more/mo.",
        "pdf_alert":        "ALERT: Expenses exceed income.",
        "pdf_footer":       "Salary & Goals Calculator  •  by Erick Perez  •  {nombre}  •  {pais}",
    },
}


def T(key, **kw):
    txt = LANGS[_LANG].get(key, LANGS["es"].get(key, key))
    return txt.format(**kw) if kw else txt

def get_months():
    return LANGS[_LANG]["months"]

# ══════════════════════════════════════════════════════════
#  TERMINAL / FLUENT THEME
# ══════════════════════════════════════════════════════════


# ══════════════════════════════════════════════════════════
#  COUNTRY FLAG IMAGES (drawn on canvas — no files needed)
# ══════════════════════════════════════════════════════════

def draw_flag_panama(canvas, x, y, w=32, h=22):
    """🇵🇦 Panama flag — 4 quadrants: white/red top, blue/white bottom"""
    hw = w // 2; hh = h // 2
    canvas.create_rectangle(x, y, x+hw, y+hh, fill="#ffffff", outline="")
    canvas.create_rectangle(x+hw, y, x+w, y+hh, fill="#d21034", outline="")
    canvas.create_rectangle(x, y+hh, x+hw, y+h, fill="#005293", outline="")
    canvas.create_rectangle(x+hw, y+hh, x+w, y+h, fill="#ffffff", outline="")
    # Stars
    for sx, sy, col in [(x+hw//2, y+hh//2, "#005293"), (x+hw+hw//2, y+hh+hh//2, "#d21034")]:
        r = min(hw, hh) * 0.28
        pts = []
        for i in range(5):
            a = math.radians(i*72 - 90)
            pts.extend([sx + r*math.cos(a), sy + r*math.sin(a)])
            a2 = math.radians(i*72 - 90 + 36)
            pts.extend([sx + r*0.4*math.cos(a2), sy + r*0.4*math.sin(a2)])
        if len(pts) >= 6:
            canvas.create_polygon(pts, fill=col, outline="")

def draw_flag_colombia(canvas, x, y, w=32, h=22):
    """🇨🇴 Colombia flag — yellow top half, blue middle quarter, red bottom quarter"""
    canvas.create_rectangle(x, y, x+w, y+h//2, fill="#fcd116", outline="")
    canvas.create_rectangle(x, y+h//2, x+w, y+h*3//4, fill="#003893", outline="")
    canvas.create_rectangle(x, y+h*3//4, x+w, y+h, fill="#ce1126", outline="")

def draw_flag_mexico(canvas, x, y, w=32, h=22):
    """🇲🇽 Mexico flag — green | white | red vertical stripes"""
    t = w // 3
    canvas.create_rectangle(x, y, x+t, y+h, fill="#006847", outline="")
    canvas.create_rectangle(x+t, y, x+2*t, y+h, fill="#ffffff", outline="")
    canvas.create_rectangle(x+2*t, y, x+w, y+h, fill="#ce1126", outline="")
    # Eagle (simplified circle)
    cx, cy = x+w//2, y+h//2
    canvas.create_oval(cx-4, cy-4, cx+4, cy+4, fill="#8B4513", outline="")

def draw_flag_usa(canvas, x, y, w=32, h=22):
    """🇺🇸 USA flag — simplified red/white stripes + blue canton"""
    # 13 stripes
    stripe_h = h / 13
    for i in range(13):
        col = "#B22234" if i % 2 == 0 else "#FFFFFF"
        canvas.create_rectangle(x, y+i*stripe_h, x+w, y+(i+1)*stripe_h, fill=col, outline="")
    # Blue canton
    canton_w = w * 0.4; canton_h = h * 7/13
    canvas.create_rectangle(x, y, x+canton_w, y+canton_h, fill="#3C3B6E", outline="")
    # Stars (simplified dots)
    rows = [6, 5, 6, 5, 6, 5, 6, 5, 6]; sx_start = x+4; sy_start = y+3
    for r, count in enumerate(rows[:5]):
        for c in range(count):
            sx = sx_start + c * (canton_w-6)/(count-1) if count > 1 else sx_start
            sy = sy_start + r * 3
            canvas.create_oval(sx-1, sy-1, sx+1, sy+1, fill="#FFFFFF", outline="")

FLAG_DRAW_FN = {
    "Panamá":   draw_flag_panama,
    "Colombia": draw_flag_colombia,
    "México":   draw_flag_mexico,
}

# ══════════════════════════════════════════════════════════

#  TAX CALCULATORS
# ══════════════════════════════════════════════════════════

def calcular_impuestos_panama(salario_bruto):
    css  = salario_bruto * 0.0975
    edu  = salario_bruto * 0.0125
    base = salario_bruto - css - edu
    anual = base * 12
    if anual <= 11000:   isr_a = 0
    elif anual <= 50000: isr_a = (anual - 11000) * 0.15
    else:                isr_a = (50000-11000)*0.15 + (anual-50000)*0.25
    isr   = isr_a / 12
    total = css + edu + isr
    return {"total_imp": round(total,2), "salario_neto": round(salario_bruto-total,2),
            "detalle": [(T("tax_css"),round(css,2)),(T("tax_edu"),round(edu,2)),
                        (T("tax_isr_pa"),round(isr,2))]}

def calcular_impuestos_colombia(salario_bruto):
    pension = salario_bruto * 0.04
    salud   = salario_bruto * 0.04
    uvt     = 47065
    anual_uvt = (salario_bruto / uvt) * 12
    if   anual_uvt <= 95:   renta = 0
    elif anual_uvt <= 150:  renta = (anual_uvt-95)*0.19*uvt/12
    elif anual_uvt <= 360:  renta = ((anual_uvt-150)*0.28+10.45)*uvt/12
    elif anual_uvt <= 640:  renta = ((anual_uvt-360)*0.33+69.25)*uvt/12
    elif anual_uvt <= 945:  renta = ((anual_uvt-640)*0.35+162.65)*uvt/12
    elif anual_uvt <= 2300: renta = ((anual_uvt-945)*0.37+269.40)*uvt/12
    else:                   renta = ((anual_uvt-2300)*0.39+770.85)*uvt/12
    total = pension + salud + renta
    return {"total_imp": round(total,2), "salario_neto": round(salario_bruto-total,2),
            "detalle": [(T("tax_pension_co"),round(pension,2)),(T("tax_salud_co"),round(salud,2)),
                        (T("tax_renta_co"),round(renta,2))]}

def calcular_impuestos_mexico(salario_bruto):
    # IMSS cuotas obrero (aprox): Enfermedad y Maternidad ~2.5%, Invalidez y Vida ~0.625%,
    # IVCM ~1.125%, Guarderías 0%, Retiro ~1.125%, Cesantía ~1.125% = ~6.5% aprox
    imss = salario_bruto * 0.065
    # ISR México 2024 — tabla mensual en MXN
    tabla_isr = [
        (746.04,   0,        0.0192),
        (6332.05,  14.32,    0.0640),
        (11128.01, 371.83,   0.1088),
        (12935.82, 893.63,   0.1600),
        (15487.71, 1182.88,  0.1792),
        (31236.49, 1227.07,  0.2136),
        (49233.00, 1281.96 + (31236.49-15487.71)*0.2136, 0.2352),
        (93993.90, 0,        0.3000),
        (125325.20,0,        0.3200),
        (375975.61,0,        0.3400),
        (float('inf'), 0,    0.3500),
    ]
    isr = 0
    lim_inf_prev = 0
    cuota_fija = 0
    tasa = 0
    for lim_sup, cf, t in tabla_isr:
        if salario_bruto <= lim_sup:
            cuota_fija = cf; tasa = t; lim_inf_prev_val = lim_inf_prev; break
        lim_inf_prev = lim_sup
    excedente = salario_bruto - lim_inf_prev
    isr = cuota_fija + excedente * tasa
    # Subsidio al empleo simplificado (≤ 10,420 MXN/mes reciben subsidio, ignora aquí)
    isr = max(0, isr)
    total = imss + isr
    return {"total_imp": round(total,2), "salario_neto": round(salario_bruto-total,2),
            "detalle": [(T("tax_imss_mx"),round(imss,2)),(T("tax_isr_mx"),round(isr,2))]}

def calcular_impuestos_usa(salario_bruto):
    # Social Security 6.2% (up to $168,600/yr wage base 2024)
    ss_anual_base = 168600
    ss_mensual_base = ss_anual_base / 12
    ss = min(salario_bruto, ss_mensual_base) * 0.062
    # Medicare 1.45% (+ 0.9% additional >$200k/yr, ignored here)
    medicare = salario_bruto * 0.0145
    # Federal income tax — 2024 single filer monthly
    anual = salario_bruto * 12
    std_ded = 14600  # standard deduction 2024 single
    taxable = max(0, anual - std_ded)
    brackets = [
        (11600,  0,      0.10),
        (47150,  1160,   0.12),
        (100525, 5426,   0.22),
        (191950, 17168.5,0.24),
        (243725, 39110.5,0.32),
        (609350, 55578.5,0.35),
        (float('inf'), 183647.25, 0.37),
    ]
    fed_anual = 0
    prev = 0
    for lim, base_tax, rate in brackets:
        if taxable <= lim:
            fed_anual = base_tax + (taxable - prev) * rate; break
        prev = lim
    fed = fed_anual / 12
    total = ss + medicare + fed
    return {"total_imp": round(total,2), "salario_neto": round(salario_bruto-total,2),
            "detalle": [(T("tax_ss_us"),round(ss,2)),(T("tax_medicare_us"),round(medicare,2)),
                        (T("tax_fed_us"),round(fed,2))]}

PAISES = {
    "Panamá":   {"moneda":"USD","simbolo":"$","flag":"🇵🇦","calcular":calcular_impuestos_panama,
                 "int_fmt": False},
    "Colombia": {"moneda":"COP","simbolo":"$","flag":"🇨🇴","calcular":calcular_impuestos_colombia,
                 "int_fmt": True},
    "México":   {"moneda":"MXN","simbolo":"$","flag":"🇲🇽","calcular":calcular_impuestos_mexico,
                 "int_fmt": True},
}

def get_sym(pais): return PAISES.get(pais,{}).get("simbolo","$")
def is_int_fmt(pais): return PAISES.get(pais,{}).get("int_fmt", False)

def f_v(v, pais):
    sym = get_sym(pais)
    return f"{sym}{v:,.0f}" if is_int_fmt(pais) else f"{sym}{v:,.2f}"

def calcular_meses(anio_meta, mes_meta):
    hoy  = date.today()
    meta = date(anio_meta, mes_meta, 1)
    if hoy >= meta: return 0
    return (meta.year-hoy.year)*12 + (meta.month-hoy.month)

def val(entry):
    try: return max(0.0, float(entry.get().strip().replace(",",".")))
    except: return 0.0

# ══════════════════════════════════════════════════════════
#  SESSION SAVE / LOAD
# ══════════════════════════════════════════════════════════

def load_sessions():
    try:
        if os.path.exists(SESSIONS_FILE):
            with open(SESSIONS_FILE,"r",encoding="utf-8") as f:
                return json.load(f)
    except: pass
    return {}

def save_sessions(sessions):
    try:
        with open(SESSIONS_FILE,"w",encoding="utf-8") as f:
            json.dump(sessions,f,ensure_ascii=False,indent=2)
        return True
    except: return False

# ══════════════════════════════════════════════════════════
#  OLD ANIMATION COMPAT SHIMS
# ══════════════════════════════════════════════════════════

def animate_slide_value(label, start, end, pais, steps=20, delay=25):
    animate_count(label, end, pais, ms=steps*delay)

def animate_fade_in(widget, steps=12, delay=18):
    pass  # no-op — fluent design avoids fake fades

# ══════════════════════════════════════════════════════════
#  SPLASH  (no Toplevel — drawn directly on root canvas)
# ══════════════════════════════════════════════════════════

def show_language_boot(root):
    W, H = 480, 310
    root.geometry(f"{W}x{H}")
    root.configure(bg="#f3f3f3")
    root.resizable(False, False)
    root.title("Salary & Goals Calculator")
    sw = root.winfo_screenwidth(); sh = root.winfo_screenheight()
    root.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
    root.deiconify()
    root.lift(); root.focus_force()

    chosen = {"lang":"es"}
    container = tk.Frame(root, bg="#f3f3f3")
    container.pack(fill="both", expand=True)

    # Top accent
    tk.Frame(container, bg="#0067c0", height=3).pack(fill="x")

    # Header with left blue bar
    hdr = tk.Frame(container, bg="#f3f3f3")
    hdr.pack(fill="x")
    tk.Frame(hdr, bg="#0067c0", width=4).pack(side="left", fill="y")
    htxt = tk.Frame(hdr, bg="#f3f3f3")
    htxt.pack(side="left", padx=16, pady=16)
    tk.Label(htxt, text="Salary & Goals Calculator",
             font=(FONT_UI,16,"bold"), bg="#f3f3f3", fg="#1a1a1a").pack(anchor="w")
    tk.Label(htxt, text="Calculadora de Salario & Metas  •  v1.0 RC |  by Erick Perez",
             font=(FONT_UI,9), bg="#f3f3f3", fg="#5a5a5a").pack(anchor="w")

    tk.Frame(container, bg="#e0e0e0", height=1).pack(fill="x", padx=20)

    # Flag strip
    fc_f = tk.Frame(container, bg="#f3f3f3")
    fc_f.pack(pady=(12,4))
    fc = tk.Canvas(fc_f, bg="#f3f3f3", width=240, height=26, highlightthickness=0)
    fc.pack()
    for i,(_, fn) in enumerate(FLAG_DRAW_FN.items()):
        fn(fc, 10+i*58, 2, 40, 22)

    tk.Label(container, text="Select Language / Selecciona Idioma",
             font=(FONT_UI,10), bg="#f3f3f3", fg="#5a5a5a").pack(pady=(6,10))

    btn_f = tk.Frame(container, bg="#f3f3f3")
    btn_f.pack(pady=4)

    def pick(lang):
        chosen["lang"] = lang
        try: container.destroy()
        except: pass

    for txt, lang, bgc, bgh in [
        ("  Espanol","es","#0067c0","#1a86d4"),
        ("  English","en","#5c1a7a","#7719aa"),
    ]:
        b = tk.Button(btn_f, text=txt, font=(FONT_UI,11,"bold"),
                      bg=bgc, fg="#ffffff", relief="flat",
                      padx=28, pady=9, cursor="hand2",
                      command=lambda l=lang: pick(l),
                      bd=0, highlightthickness=0)
        b.pack(side="left", padx=8)
        b.bind("<Enter>", lambda e,b=b,c=bgh: b.config(bg=c))
        b.bind("<Leave>", lambda e,b=b,c=bgc: b.config(bg=c))

    tk.Label(container, text="Panama  Colombia  Mexico",
             font=(FONT_UI,8), bg="#f3f3f3", fg="#9a9a9a").pack(pady=(12,4))

    root.wait_window(container)
    return chosen["lang"]


def show_splash(root, on_done):
    W, H = 600, 360
    sw = root.winfo_screenwidth(); sh = root.winfo_screenheight()
    root.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
    root.configure(bg="#1f1f1f")
    root.resizable(False, False)
    root.overrideredirect(True)
    root.lift(); root.attributes("-topmost",True)
    root.update()

    cv = tk.Canvas(root, bg="#1f1f1f", width=W, height=H,
                   highlightthickness=0, bd=0)
    cv.pack(fill="both", expand=True)
    root.update_idletasks()

    # Card
    CX,CY = W//2, H//2
    cw,ch = 440, 300
    cx0,cy0 = CX-cw//2, CY-ch//2
    # shadow
    cv.create_rectangle(cx0+5,cy0+5,cx0+cw+5,cy0+ch+5,fill="#0a0a0a",outline="")
    # body
    cv.create_rectangle(cx0,cy0,cx0+cw,cy0+ch,fill="#2d2d2d",outline="#454545",width=1)
    # top accent
    cv.create_rectangle(cx0,cy0,cx0+cw,cy0+3,fill="#0067c0",outline="")

    # Coin (gold circle)
    coin_y0 = cy0+52
    st = {"y": float(coin_y0)}
    ov  = cv.create_oval(CX-28,coin_y0-28,CX+28,coin_y0+28,
                          fill="#fce100",outline="#a08000",width=2)
    sym = cv.create_text(CX,coin_y0,text="$",
                         font=(FONT_UI,22,"bold"),fill="#5a3e00")

    # Texts
    cv.create_text(CX, cy0+108, text="Salary & Goals Calculator",
                   font=(FONT_UI,15,"bold"), fill="#ffffff")
    cv.create_text(CX, cy0+132, text="by Erick Perez  •  v1.0 RC  |  Released 03/15/2026",
                   font=(FONT_UI,9,"italic"), fill="#808080")
    cv.create_text(CX, cy0+152, text="Panama  Colombia  Mexico",
                   font=(FONT_UI,9), fill="#60cdff")

    # Flags
    fy = cy0+176; gap=52
    fx0 = CX - (len(FLAG_DRAW_FN)*gap)//2 + gap//4
    for i,(_,fn) in enumerate(FLAG_DRAW_FN.items()):
        fn(cv, fx0+i*gap, fy, 36, 22)

    # Progress bar
    bx0=CX-160; by=cy0+222
    cv.create_rectangle(bx0,by,bx0+320,by+5,fill="#383838",outline="#454545")
    bar = cv.create_rectangle(bx0,by,bx0,by+5,fill="#0067c0",outline="")
    msg = cv.create_text(CX,by+18,text="Loading...",
                          font=(FONT_UI,8),fill="#808080")

    MSGS = ["Initializing...","Loading modules...","Configuring taxes...","Preparing UI...","Ready!"]
    total=2400; step_ms=24; elapsed=[0]; running=[True]; aid=[None]

    def tick():
        if not running[0]: return
        elapsed[0] += step_ms
        pct = min(elapsed[0]/total, 1.0)
        p100 = int(pct*100)

        # Coin bounce with canvas.move
        ny = coin_y0 + math.sin(elapsed[0]/380)*6
        dy = ny - st["y"]; st["y"] = ny
        cv.move(ov, 0, dy); cv.move(sym, 0, dy)

        # Bar
        ease = 1-(1-pct)**3
        x1 = bx0 + int(320*ease)
        cv.coords(bar, bx0, by, x1, by+5)
        if pct > 0.85: cv.itemconfig(bar, fill="#60cdff")

        mi = min(int(pct*5), 4)
        cv.itemconfig(msg, text=f"{MSGS[mi]}  {p100}%")

        if pct < 1.0:
            aid[0] = root.after(step_ms, tick)
        else:
            root.after(280, finish)

    def finish():
        running[0] = False
        if aid[0]:
            try: root.after_cancel(aid[0])
            except: pass
        try: cv.destroy()
        except: pass
        on_done()

    tick()


# ══════════════════════════════════════════════════════════
#  MAIN APP — Fluent sidebar layout
# ══════════════════════════════════════════════════════════


def make_nav_icon(name, size=20):
    """Compat stub — icon system uses _draw_circle_icon directly."""
    return _draw_circle_icon(size, W11["surface3"], W11["text3"], name[:1], 0.44)

class CalcApp(tk.Frame):
    """Main application — lives inside the single tk.Tk root."""
    def __init__(self, root):
        global _APP_REF, _tw
        super().__init__(root, bg=W11["bg"])
        self.root = root
        _APP_REF  = self
        _tw       = Tweener(root)
        self._step  = 0
        self._datos = {}
        self._fields= {}
        self._chrome_built = False
        self.pack(fill="both", expand=True)
        self._build_chrome()
        self._show_step(0)

    # ─────────────────────────────────────────────────────
    #  CHROME
    # ─────────────────────────────────────────────────────
    def _build_chrome(self):
        # ── Title bar (dark, Win11 style) ─────────────────
        self._tb = tk.Frame(self, bg=W11["title_bar"], height=40)
        self._tb.pack(fill="x"); self._tb.pack_propagate(False)

        # App icon + title
        left = tk.Frame(self._tb, bg=W11["title_bar"])
        left.pack(side="left", fill="y", padx=(12,0))

        if PIL_OK:
            ico = _draw_circle_icon(24, W11["accent"], "#ffffff", "$", 0.48)
            il  = tk.Label(left, image=ico, bg=W11["title_bar"])
            il.pack(side="left", padx=(0,8), pady=8)
            il._ico = ico

        self._title_lbl = tk.Label(left, text=T("title_bar"),
                                   font=(FONT,9,"bold"),
                                   bg=W11["title_bar"],
                                   fg=W11["titlebar_txt"])
        self._title_lbl.pack(side="left")

        # Right controls
        right = tk.Frame(self._tb, bg=W11["title_bar"])
        right.pack(side="right", padx=10)

        # Theme toggle
        self._dark_btn = self._tb_btn(right, T("dark_mode"), self._toggle_dark)
        Tooltip(self._dark_btn, "Toggle dark / light mode")

        # Save / Load
        self._save_btn = self._tb_btn(right, "💾 " + T("save_session"),
                                      self._save_session_dialog)
        self._load_btn = self._tb_btn(right, "📂 " + T("load_session"),
                                      self._load_session_dialog)

        # Language
        self._btn_es = self._tb_btn(right, "ES", lambda: self._change_lang("es"),
                                    accent=True)
        self._btn_en = self._tb_btn(right, "EN", lambda: self._change_lang("en"))
        self._update_lang_btns()

        # ── Body: sidebar | content ───────────────────────
        body = tk.Frame(self, bg=W11["bg"])
        body.pack(fill="both", expand=True)

        # Sidebar
        self._sidebar = SideStepBar(body, on_step_click=self._sidebar_click)
        self._sidebar.pack(side="left", fill="y")

        # Right panel: top step pips + scrollable content + nav bar
        right_panel = tk.Frame(body, bg=W11["bg"])
        right_panel.pack(side="left", fill="both", expand=True)

        # Accent separator (left edge of content)
        tk.Frame(body, bg=W11["divider"], width=1).pack(side="left", fill="y")

        # Top step pip bar
        self.stepbar = TopStepBar(right_panel)
        self.stepbar.pack(fill="x")
        tk.Frame(right_panel, bg=W11["divider"], height=1).pack(fill="x")

        # Content
        self.content = tk.Frame(right_panel, bg=W11["bg"])
        self.content.pack(fill="both", expand=True)

        # Nav bar (bottom)
        self._nav = tk.Frame(right_panel, bg=W11["surface"],
                             highlightbackground=W11["border"],
                             highlightthickness=1, height=54)
        self._nav.pack(fill="x", side="bottom")
        self._nav.pack_propagate(False)

        self.btn_back = FluentButton(self._nav, text=T("back"), variant="ghost",
                                     icon_sym="<", command=self._prev_step)
        self.btn_back.pack(side="left", padx=16, pady=10)

        self.lbl_step = tk.Label(self._nav, text=T("step_of",s=1,t=8),
                                  font=F_SMALL, bg=W11["surface"], fg=W11["text3"])
        self.lbl_step.pack(side="left", expand=True)

        self.btn_next = FluentButton(self._nav, text=T("next"), variant="primary",
                                      icon_sym=">", command=self._next_step)
        self.btn_next.pack(side="right", padx=16, pady=10)

        self._chrome_built = True

        # Build sidebar items (needs step names from T())
        self._sidebar.build_steps(T("steps"))
        self.stepbar.build(T("steps"))

    def _tb_btn(self, parent, text, cmd, accent=False):
        bg = W11["step_act"] if accent else W11["surface3"]
        fg = "#ffffff"       if accent else W11["text2"]
        b  = tk.Button(parent, text=text, font=(FONT,8),
                       bg=bg, fg=fg, relief="flat",
                       padx=10, pady=3, cursor="hand2",
                       bd=0, highlightthickness=0, command=cmd)
        b.pack(side="left", padx=2)
        b.bind("<Enter>", lambda _,b=b,h=W11["accent_h"] if accent else W11["border2"]:
               b.config(bg=h))
        b.bind("<Leave>", lambda _,b=b,bg=bg: b.config(bg=bg))
        return b

    def _sidebar_click(self, step):
        # Allow clicking only already-visited steps
        if step <= self._step:
            self._save_step(self._step)
            self._show_step(step)

    # ─────────────────────────────────────────────────────
    #  THEME
    # ─────────────────────────────────────────────────────
    def _apply_theme(self):
        if not self._chrome_built: return
        self.configure(bg=W11["bg"])
        self.root.configure(bg=W11["bg"])
        self._tb.config(bg=W11["title_bar"])
        self._title_lbl.config(bg=W11["title_bar"], fg=W11["titlebar_txt"])
        self.content.config(bg=W11["bg"])
        self._nav.config(bg=W11["surface"], highlightbackground=W11["border"])
        self.lbl_step.config(bg=W11["surface"], fg=W11["text3"])
        self._dark_btn.config(text=T("dark_mode") if _DARK_MODE else T("light_mode"))
        self._sidebar.config(bg=W11["sidebar_bg"])
        self.stepbar.config(bg=W11["surface2"])

    _apply_theme_to_chrome = _apply_theme   # compat alias

    def _toggle_dark(self): toggle_dark()

    def _update_lang_btns(self):
        if not self._chrome_built: return
        self._btn_es.config(bg=W11["step_act"] if _LANG=="es" else W11["surface3"],
                            fg="#ffffff"       if _LANG=="es" else W11["text2"])
        self._btn_en.config(bg=W11["step_act"] if _LANG=="en" else W11["surface3"],
                            fg="#ffffff"       if _LANG=="en" else W11["text2"])

    def _change_lang(self, lang):
        set_lang(lang)
        if not self._chrome_built: return
        self._update_lang_btns()
        self.root.title(T("app_title"))
        _set_window_icon(self.root)
        self._title_lbl.config(text=T("title_bar"))
        self._dark_btn.config(text=T("dark_mode") if _DARK_MODE else T("light_mode"))
        steps = T("steps")
        self._sidebar.update_step(self._step, steps)
        self.stepbar.update_step(self._step, steps)
        self._refresh_nav()
        self._clear_content()
        self._dispatch_step(self._step)

    # ─────────────────────────────────────────────────────
    #  NAVIGATION
    # ─────────────────────────────────────────────────────
    def _refresh_nav(self):
        self.lbl_step.config(text=T("step_of",s=self._step+1,t=8))
        self.btn_back.config(text=T("back"))
        self.btn_next.config(text=T("new_query") if self._step==7 else T("next"))

    def _clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()

    def _scrollable(self):
        outer  = tk.Frame(self.content, bg=W11["bg"])
        outer.pack(fill="both", expand=True)
        canvas = tk.Canvas(outer, bg=W11["bg"], highlightthickness=0)
        sb     = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        frame  = tk.Frame(canvas, bg=W11["bg"])
        wid    = canvas.create_window((0,0), window=frame, anchor="nw")
        frame.bind("<Configure>",
                   lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>",
                    lambda e: canvas.itemconfig(wid, width=e.width))
        canvas.bind_all("<MouseWheel>",
                        lambda e: canvas.yview_scroll(-1*(e.delta//120),"units"))
        return frame

    def _dispatch_step(self, step):
        builders = [self._step_perfil, self._step_meta, self._step_ingresos,
                    self._step_hogar,  self._step_deudas_auto, self._step_ocio,
                    self._step_extras, self._step_resultado]
        builders[step]()

    def _show_step(self, step):
        self._step = step
        self._clear_content()
        steps = T("steps")
        self._sidebar.update_step(step, steps)
        self.stepbar.update_step(step, steps)
        self.lbl_step.config(text=T("step_of",s=step+1,t=8))
        self.btn_back.config(state="normal" if step>0 else "disabled",
                             text=T("back"))
        is_last = (step==7)
        if is_last:
            self.btn_next.config(text=T("new_query"), command=self._reset, state="normal")
            self.btn_next._bg  = W11["btn_sec"]
            self.btn_next._hov = W11["border"]
            self.btn_next.config(bg=W11["btn_sec"], fg=W11["btn_sec_fg"])
        else:
            self.btn_next.config(text=T("next"), command=self._next_step, state="normal")
            self.btn_next._bg  = W11["btn_bg"]
            self.btn_next._hov = W11["accent_h"]
            self.btn_next.config(bg=W11["btn_bg"], fg=W11["btn_fg"])
        self._dispatch_step(step)

    def _next_step(self):
        v = {0:self._validate_perfil, 1:self._validate_meta, 2:self._validate_ingresos}
        if self._step in v and not v[self._step](): return
        self._save_step(self._step)
        self._show_step(self._step+1)

    def _prev_step(self):
        self._save_step(self._step)
        self._show_step(self._step-1)

    # ─────────────────────────────────────────────────────
    #  SAVE / LOAD STEP DATA
    # ─────────────────────────────────────────────────────
    def _save_step(self, step):
        f = self._fields
        if step==0:
            raw  = f.get("pais","").get() if "pais" in f else "Panamá"
            pais = next((p for p in PAISES if p in raw),"Panamá")
            self._datos["nombre"] = f.get("nombre","").get() if "nombre" in f else ""
            self._datos["pais"]   = pais
        elif step==1:
            months = get_months()
            try:
                self._datos["meta"]      = max(0.0,float(f["meta"].get().replace(",",".")))
                self._datos["mes_num"]   = months.index(f["mes"].get())+1
                self._datos["anio_meta"] = int(f["anio"].get())
            except: pass
        elif step==2:
            self._datos["salario"]       = val(f["salario"])
            self._datos["salario_real"]  = val(f["salario_real"]) if "salario_real" in f else 0
            self._datos["ingreso_extra"] = val(f["ingreso_extra"])
        elif step==3:
            for k in ["alquiler","internet","luz","agua","data_movil"]:
                self._datos[k] = val(f[k])
        elif step==4:
            for k in ["prestamo_personal","prestamo_auto","deudas",
                      "gasolina","mantenimiento_auto",
                      "mascota_comida","mascota_vet","mascota_otros"]:
                self._datos[k] = val(f[k])
        elif step==5:
            for k in ["comida","salidas","delivery","apple_one","netflix","hbo","disney"]:
                self._datos[k] = val(f[k])
        elif step==6:
            extras=[]
            for i in range(3):
                m = val(f[f"extra_m_{i}"])
                d = f[f"extra_d_{i}"].get().strip() or T("p6_extra",n=i+1)
                extras.append({"monto":m,"desc":d})
            self._datos["gastos_extra"] = extras

    # ─────────────────────────────────────────────────────
    #  VALIDATORS
    # ─────────────────────────────────────────────────────
    def _validate_perfil(self):
        if not self._fields.get("nombre") or not self._fields["nombre"].get().strip():
            messagebox.showwarning(T("req_field"), T("req_name")); return False
        return True
    def _validate_meta(self):
        try: assert float(self._fields["meta"].get().replace(",",".")) > 0
        except: messagebox.showwarning(T("req_field"),T("req_meta")); return False
        try: int(self._fields["anio"].get())
        except: messagebox.showwarning(T("req_field"),T("req_year")); return False
        return True
    def _validate_ingresos(self):
        if val(self._fields["salario"]) == 0:
            messagebox.showwarning(T("req_field"),T("req_sal")); return False
        return True

    # ─────────────────────────────────────────────────────
    #  SESSION DIALOGS
    # ─────────────────────────────────────────────────────
    def _save_session_dialog(self):
        popup = tk.Toplevel(self)
        popup.title(T("save_session"))
        popup.configure(bg=W11["surface"])
        popup.geometry("400x180")
        popup.transient(self); popup.grab_set()
        sw,sh = popup.winfo_screenwidth(),popup.winfo_screenheight()
        popup.geometry(f"400x180+{(sw-400)//2}+{(sh-180)//2}")
        tk.Frame(popup, bg=W11["accent"], height=3).pack(fill="x")
        tk.Label(popup, text=T("save_name"), font=F_BODY,
                 bg=W11["surface"], fg=W11["text"]).pack(padx=20,pady=(14,4),anchor="w")
        name_var = tk.StringVar(value=self._datos.get("nombre","Session"))
        entry = tk.Entry(popup, textvariable=name_var, font=F_INPUT,
                         bg=W11["input_bg"], fg=W11["text"], relief="flat",
                         insertbackground=W11["cursor"])
        entry.pack(padx=20,fill="x",pady=4); entry.select_range(0,"end"); entry.focus()
        def do_save():
            name = name_var.get().strip()
            if not name: return
            sessions = load_sessions()
            sessions[name] = {"data":self._datos,"lang":_LANG,"dark":_DARK_MODE,
                              "step":self._step,"saved_at":date.today().isoformat()}
            if save_sessions(sessions):
                popup.destroy()
                messagebox.showinfo("✓", T("save_success",name=name))
            else:
                messagebox.showerror("✗", T("save_error"))
        bf = tk.Frame(popup, bg=W11["surface"]); bf.pack(fill="x",padx=20,pady=12)
        FluentButton(bf, text=T("ok"), variant="primary", command=do_save).pack(side="right",padx=4)
        FluentButton(bf, text=T("cancel"), variant="ghost", command=popup.destroy).pack(side="right",padx=4)

    def _load_session_dialog(self):
        sessions = load_sessions()
        popup = tk.Toplevel(self)
        popup.title(T("load_session")); popup.configure(bg=W11["surface"])
        popup.geometry("460x380"); popup.transient(self); popup.grab_set()
        sw,sh = popup.winfo_screenwidth(),popup.winfo_screenheight()
        popup.geometry(f"460x380+{(sw-460)//2}+{(sh-380)//2}")
        tk.Frame(popup, bg=W11["accent"], height=3).pack(fill="x")
        tk.Label(popup, text=T("load_select") if sessions else T("load_none"),
                 font=F_BODY, bg=W11["surface"], fg=W11["text"]
                 ).pack(padx=20,pady=(14,8),anchor="w")
        if not sessions:
            FluentButton(popup,text=T("cancel"),variant="ghost",command=popup.destroy).pack(pady=16)
            return
        fr = tk.Frame(popup, bg=W11["surface"]); fr.pack(fill="both",expand=True,padx=20)
        sb2 = ttk.Scrollbar(fr, orient="vertical")
        lb  = tk.Listbox(fr, font=F_MONO, bg=W11["input_bg"], fg=W11["text"],
                         selectbackground=W11["accent"], selectforeground=W11["bg"],
                         relief="flat", bd=0, highlightthickness=0, yscrollcommand=sb2.set)
        sb2.config(command=lb.yview)
        lb.pack(side="left",fill="both",expand=True); sb2.pack(side="right",fill="y")
        for name,meta in sessions.items():
            lb.insert("end",f"  {name}   [{meta.get('saved_at','')}]")
        lb.selection_set(0)
        def do_load():
            sel = lb.curselection()
            if not sel: return
            name = list(sessions.keys())[sel[0]]
            self._datos = dict(sessions[name].get("data",{}))
            popup.destroy()
            messagebox.showinfo("✓", T("load_success",name=name))
            self._show_step(0)
        def do_delete():
            sel = lb.curselection()
            if not sel: return
            name = list(sessions.keys())[sel[0]]
            sessions.pop(name,None); save_sessions(sessions); lb.delete(sel[0])
        bf = tk.Frame(popup,bg=W11["surface"]); bf.pack(fill="x",padx=20,pady=12)
        FluentButton(bf,text=T("ok"),variant="primary",command=do_load).pack(side="right",padx=4)
        FluentButton(bf,text=T("delete_session"),variant="ghost",command=do_delete).pack(side="right",padx=4)
        FluentButton(bf,text=T("cancel"),variant="ghost",command=popup.destroy).pack(side="right",padx=4)

    # ─────────────────────────────────────────────────────
    #  PAGE HEADER
    # ─────────────────────────────────────────────────────
    def _page_title(self, parent, title, subtitle="", pais=None):
        hdr = tk.Frame(parent, bg=W11["bg"])
        hdr.pack(fill="x", padx=24, pady=(20,4))

        row = tk.Frame(hdr, bg=W11["bg"])
        row.pack(fill="x")

        # Left accent bar
        tk.Frame(row, bg=W11["accent"], width=4).pack(side="left", fill="y", padx=(0,12))

        col = tk.Frame(row, bg=W11["bg"])
        col.pack(side="left", fill="x", expand=True)
        tk.Label(col, text=title, font=F_TITLE,
                 bg=W11["bg"], fg=W11["text"], anchor="w").pack(fill="x")
        if subtitle:
            tk.Label(col, text=subtitle, font=F_SMALL,
                     bg=W11["bg"], fg=W11["text3"], anchor="w").pack(fill="x", pady=(2,0))

        if pais and pais in FLAG_DRAW_FN:
            fc = tk.Canvas(row, bg=W11["bg"], width=56, height=38, highlightthickness=0)
            fc.pack(side="right", padx=(0,16))
            FLAG_DRAW_FN[pais](fc, 7, 8, 42, 24)

        tk.Frame(parent, bg=W11["divider"], height=1).pack(fill="x", padx=24, pady=(10,16))

    # ═══════════════════════════════════════════════════════
    #  STEP 0 — PROFILE
    # ═══════════════════════════════════════════════════════
    def _step_perfil(self):
        self._fields = {}
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá")
        self._page_title(f, T("p0_title"), T("p0_sub"), pais)

        c = fluent_card(f)
        section_title(c, T("p0_section"), icon_sym="P")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=16, pady=(0,16))
        g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)

        nom = FluentEntry(g, label=T("p0_name"), prefix="",
                          tooltip=T("p0_name"))
        nom.grid(row=0,column=0,sticky="ew",padx=(0,12),pady=4)
        nom.set(self._datos.get("nombre",""))
        self._fields["nombre"] = nom

        pais_list = [f"{PAISES[p]['flag']} {p}" for p in PAISES]
        pw = FluentCombo(g, label=T("p0_country"), values=pais_list,
                         width=22, show_flags=True)
        saved = self._datos.get("pais","Panamá")
        match = next((o for o in pais_list if saved in o), pais_list[0])
        pw.set(match)
        pw.grid(row=0,column=1,sticky="ew",pady=4)
        self._fields["pais"] = pw

        # Country pills
        pills = tk.Frame(c, bg=W11["surface"])
        pills.pack(fill="x", padx=16, pady=(0,8))
        for txt, col in [("Panama","tag_blue"),("Colombia","tag_green"),
                          ("Mexico","tag_red")]:
            tag_pill(pills, txt, W11[col])

        note_box(c, T("p0_note"), icon="⚡")

    # ═══════════════════════════════════════════════════════
    #  STEP 1 — GOAL
    # ═══════════════════════════════════════════════════════
    def _step_meta(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p1_title"), T("p1_sub"), pais)
        c = fluent_card(f)
        section_title(c, T("p1_section"), icon_sym="G")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=16, pady=(0,16))
        g.columnconfigure(0,weight=2); g.columnconfigure(1,weight=1); g.columnconfigure(2,weight=1)

        meta_w = FluentEntry(g, label=T("p1_meta"), prefix=sym)
        meta_w.grid(row=0,column=0,sticky="ew",padx=(0,12),pady=4)
        meta_w.set(str(self._datos.get("meta","")))
        self._fields["meta"] = meta_w

        months = get_months()
        mes_w = FluentCombo(g, label=T("p1_month"), values=months, width=14)
        mes_w.set(months[self._datos.get("mes_num",11)-1])
        mes_w.grid(row=0,column=1,sticky="ew",padx=(0,12),pady=4)
        self._fields["mes"] = mes_w

        anio_w = FluentEntry(g, label=T("p1_year"), prefix="")
        anio_w.grid(row=0,column=2,sticky="ew",pady=4)
        anio_w.set(str(self._datos.get("anio_meta","2026")))
        self._fields["anio"] = anio_w

        tip = fluent_card(f, pady=4)
        tk.Label(tip, text=T("p1_tip"), font=F_SMALL, bg=W11["surface"],
                 fg=W11["text2"], wraplength=780, justify="left"
                 ).pack(padx=16, pady=12, anchor="w")

    # ═══════════════════════════════════════════════════════
    #  STEP 2 — INCOME
    # ═══════════════════════════════════════════════════════
    def _step_ingresos(self):
        f = self._scrollable()
        pais   = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p2_title"), T("p2_sub"), pais)
        c = fluent_card(f)
        section_title(c, T("p2_section"), icon_sym="$")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=16, pady=(0,16))
        g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1); g.columnconfigure(2,weight=1)

        for col,(k,lk) in enumerate([("salario","p2_gross"),("salario_real","p2_real"),("ingreso_extra","p2_extra")]):
            w = FluentEntry(g, label=T(lk), prefix=sym)
            w.grid(row=0, column=col, sticky="ew",
                   padx=(0,12) if col<2 else 0, pady=4)
            w.set(str(self._datos.get(k,"")))
            self._fields[k] = w

        note_box(c, T("p2_note"), icon="ℹ")

    # ═══════════════════════════════════════════════════════
    #  STEP 3 — HOME
    # ═══════════════════════════════════════════════════════
    def _step_hogar(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p3_title"), T("p3_sub"), pais)
        c = fluent_card(f)
        section_title(c, T("p3_section"), icon_sym="H")
        g = tk.Frame(c, bg=W11["surface"])
        g.pack(fill="x", padx=16, pady=(0,16))
        g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
        for i,(k,lk) in enumerate([("alquiler","p3_rent"),("internet","p3_internet"),
                                    ("luz","p3_electric"),("agua","p3_water"),("data_movil","p3_mobile")]):
            w = FluentEntry(g, label=T(lk), prefix=sym)
            w.grid(row=i//2, column=i%2, sticky="ew",
                   padx=(0,12) if i%2==0 else 0, pady=4)
            w.set(str(self._datos.get(k,""))); self._fields[k] = w

    # ═══════════════════════════════════════════════════════
    #  STEP 4 — DEBTS / AUTO / PETS
    # ═══════════════════════════════════════════════════════
    def _step_deudas_auto(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p4_title"), T("p4_sub"), pais)
        for sec, isym, campos in [
            (T("p4_s1"),"D",[("prestamo_personal","p4_loan_p"),
                              ("prestamo_auto","p4_loan_a"),("deudas","p4_debts")]),
            (T("p4_s2"),"C",[("gasolina","p4_gas"),("mantenimiento_auto","p4_maint")]),
            (T("p4_s3"),"~",[("mascota_comida","p4_pet_food"),
                              ("mascota_vet","p4_pet_vet"),("mascota_otros","p4_pet_other")]),
        ]:
            c = fluent_card(f, pady=8)
            section_title(c, sec, icon_sym=isym)
            g = tk.Frame(c, bg=W11["surface"])
            g.pack(fill="x", padx=16, pady=(0,12))
            g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
            for i,(k,lk) in enumerate(campos):
                w = FluentEntry(g, label=T(lk), prefix=sym)
                w.grid(row=i//2,column=i%2,sticky="ew",
                       padx=(0,12) if i%2==0 else 0,pady=4)
                w.set(str(self._datos.get(k,""))); self._fields[k] = w

    # ═══════════════════════════════════════════════════════
    #  STEP 5 — LEISURE
    # ═══════════════════════════════════════════════════════
    def _step_ocio(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p5_title"), T("p5_sub"), pais)
        for sec, isym, campos in [
            (T("p5_s1"),"F",[("comida","p5_grocery"),("salidas","p5_out"),
                              ("delivery","p5_delivery")]),
            (T("p5_s2"),"@",[("apple_one","Apple One"),("netflix","Netflix"),
                              ("hbo","HBO Max"),("disney","Disney+")]),
        ]:
            c = fluent_card(f, pady=8)
            section_title(c, sec, icon_sym=isym)
            g = tk.Frame(c, bg=W11["surface"])
            g.pack(fill="x", padx=16, pady=(0,12))
            g.columnconfigure(0,weight=1); g.columnconfigure(1,weight=1)
            for i,(k,lk) in enumerate(campos):
                lbl = T(lk) if lk in LANGS["es"] else lk
                w   = FluentEntry(g, label=lbl, prefix=sym)
                w.grid(row=i//2,column=i%2,sticky="ew",
                       padx=(0,12) if i%2==0 else 0,pady=4)
                w.set(str(self._datos.get(k,""))); self._fields[k] = w

    # ═══════════════════════════════════════════════════════
    #  STEP 6 — EXTRAS
    # ═══════════════════════════════════════════════════════
    def _step_extras(self):
        f = self._scrollable()
        pais = self._datos.get("pais","Panamá"); sym = get_sym(pais)
        self._page_title(f, T("p6_title"), T("p6_sub"), pais)
        c = fluent_card(f)
        section_title(c, T("p6_section"), icon_sym="+")
        extras = self._datos.get("gastos_extra",
                                 [{"monto":0,"desc":""},{"monto":0,"desc":""},{"monto":0,"desc":""}])
        for i in range(3):
            row = tk.Frame(c, bg=W11["surface"])
            row.pack(fill="x", padx=16, pady=4)
            row.columnconfigure(0,weight=1); row.columnconfigure(1,weight=2)
            mw = FluentEntry(row, label=T("p6_extra",n=i+1), prefix=sym)
            mw.grid(row=0,column=0,sticky="ew",padx=(0,12))
            mw.set(str(extras[i]["monto"]) if extras[i]["monto"] else "")
            self._fields[f"extra_m_{i}"] = mw
            dw = FluentEntry(row, label=T("p6_desc"), prefix="")
            dw.grid(row=0,column=1,sticky="ew")
            dw.set(extras[i]["desc"]); self._fields[f"extra_d_{i}"] = dw
        tk.Frame(c, bg=W11["divider"], height=1).pack(fill="x", padx=16, pady=12)
        tk.Label(c, text=T("p6_hint"), font=F_SMALL,
                 bg=W11["surface"], fg=W11["text3"]
                 ).pack(padx=16, pady=(0,14), anchor="w")

    # ═══════════════════════════════════════════════════════
    #  STEP 7 — RESULTS
    # ═══════════════════════════════════════════════════════
    def _step_resultado(self):
        self._save_step(6)
        d    = self._datos
        pais = d.get("pais","Panamá")
        cfg  = PAISES.get(pais, PAISES["Panamá"])
        sym  = cfg["simbolo"]
        imp  = cfg["calcular"](d.get("salario",0))
        d["impuestos"] = imp

        sal_real = d.get("salario_real",0)
        sal_base = sal_real if sal_real>0 else imp["salario_neto"]
        d["salario_neto"]   = sal_base
        d["total_ingresos"] = sal_base + d.get("ingreso_extra",0)

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

        meses_r  = calcular_meses(d.get("anio_meta",2026), d.get("mes_num",11))
        d["meses_restantes"] = meses_r
        meta     = d.get("meta",0)
        nec_mes  = meta/meses_r if meses_r>0 else 0
        proyecc  = max(d["ahorro_mensual"],0)*meses_r
        ahorro   = d["ahorro_mensual"]
        months   = get_months()
        mes_n    = months[d.get("mes_num",11)-1]
        fmt_v    = lambda v: f_v(v, pais)

        SU = W11["success"]; DA = W11["danger"]; WA = W11["warning"]; AC = W11["accent"]
        T_ = W11["text"];    T2 = W11["text2"]

        f = self._scrollable()
        self._page_title(f, T("p7_title",nombre=d.get("nombre","")),
                         T("p7_sub",pais=pais,sym=sym,meta=meta,
                           mes=mes_n,anio=d.get("anio_meta",2026)), pais)

        # ── Status banner ─────────────────────────────────
        if ahorro <= 0:
            bg_c=W11["danger_bg"]; fg_c=DA; pfx="✗"; bm=T("p7_deficit",sym=sym,amt=abs(ahorro))
        elif proyecc >= meta:
            bg_c=W11["success_bg"]; fg_c=SU; pfx="✓"; bm=T("p7_ontrack",sym=sym,amt=ahorro,
                                                              mes=mes_n,anio=d.get("anio_meta",2026))
        else:
            bg_c=W11["warning_bg"]; fg_c=WA; pfx="⚡"; bm=T("p7_need",sym=sym,amt=ahorro,
                                                               falta=nec_mes-ahorro)

        bann_o = tk.Frame(f, bg=fg_c); bann_o.pack(fill="x", padx=24, pady=(0,16))
        bann   = tk.Frame(bann_o, bg=bg_c); bann.pack(fill="x", padx=2, pady=2)
        brow   = tk.Frame(bann, bg=bg_c); brow.pack(fill="x", padx=16, pady=12)
        tk.Label(brow, text=pfx, font=(FONT,14,"bold"),
                 bg=bg_c, fg=fg_c).pack(side="left", padx=(0,10))
        tk.Label(brow, text=bm, font=(FONT,11,"bold"),
                 bg=bg_c, fg=fg_c, wraplength=780, justify="left").pack(side="left")

        # ── Progress ring + key stats ─────────────────────
        ring_card = fluent_card(f, pady=6)
        section_title(ring_card, T("p7_summary"), icon_sym="=")
        ring_row = tk.Frame(ring_card, bg=W11["surface"])
        ring_row.pack(fill="x", padx=16, pady=(0,12))

        # Ring on left
        ring_cv = tk.Canvas(ring_row, bg=W11["surface"],
                            width=100, height=100, highlightthickness=0)
        ring_cv.pack(side="left", padx=(0,20))
        pct_saved = max(0, min(ahorro/d["total_ingresos"],1.0)) if d["total_ingresos"]>0 else 0
        ring_col  = SU if ahorro>=0 else DA
        progress_ring(ring_cv, 50,50, 40, pct_saved, ring_col, W11["progress_bg"], 10)
        ring_cv.create_text(50,50, text=f"{int(pct_saved*100)}%",
                            font=(FONT,13,"bold"), fill=ring_col)
        ring_cv.create_text(50,68, text=T("p7_saving")[:8],
                            font=(FONT,7), fill=W11["text3"])

        # Stats on right
        stats = tk.Frame(ring_row, bg=W11["surface"])
        stats.pack(side="left", fill="x", expand=True)
        for lbl, amt, col in [
            (T("p7_tot_inc"), d["total_ingresos"], SU),
            (T("p7_tot_exp"), d["total_gastos"],   DA),
            (T("p7_saving"),  abs(ahorro),          SU if ahorro>=0 else DA),
        ]:
            row_f = tk.Frame(stats, bg=W11["surface"])
            row_f.pack(fill="x", pady=3)
            tk.Label(row_f, text=lbl, font=F_BODY,
                     bg=W11["surface"], fg=T2).pack(side="left")
            vl = tk.Label(row_f, text="—", font=(FONT,11,"bold"),
                          bg=W11["surface"], fg=col)
            vl.pack(side="right")
            animate_count(vl, amt, pais)
        tk.Frame(ring_card, bg=W11["divider"], height=1).pack(fill="x",padx=16,pady=(4,4))

        # ── Result cards helper ───────────────────────────
        def res_card(parent, title, rows, isym=""):
            c2 = fluent_card(parent, pady=6)
            section_title(c2, title, icon_sym=isym)
            for lbl, amt, col in rows:
                if amt==0: continue
                r = tk.Frame(c2, bg=W11["surface"]); r.pack(fill="x",padx=16,pady=1)
                tk.Label(r, text=lbl, font=F_BODY, bg=W11["surface"], fg=T2).pack(side="left")
                tk.Label(r, text=fmt_v(amt), font=(FONT,10,"bold"),
                         bg=W11["surface"], fg=col).pack(side="right")
            tk.Frame(c2, bg=W11["divider"], height=1).pack(fill="x",padx=16,pady=(6,4))

        # Tax breakdown
        imp_rows = [(n,m,DA) for n,m in imp["detalle"]]
        imp_rows += [(T("p7_total_ded"),imp["total_imp"],DA)]
        if sal_real>0:
            imp_rows += [(T("p7_net_est"),imp["salario_neto"],AC),
                         (T("p7_net_real"),sal_real,SU)]
        else:
            imp_rows += [(T("p7_net_est"),imp["salario_neto"],SU)]
        res_card(f, T("p7_salary_imp"), imp_rows, "$")
        note_box(fluent_card(f,pady=4), T("p7_imp_note"), W11["note_bg"], W11["note_border"],"⚠")
        res_card(f, T("p7_income"), [(T("p7_net_base"),sal_base,T_),
                                     (T("p7_extra_inc"),d.get("ingreso_extra",0),AC),
                                     (T("p7_total_inc"),d["total_ingresos"],SU)], "$")
        res_card(f, T("p7_home"),   [(T("p7_rent"),d.get("alquiler",0),T2),
                                     ("Internet",d.get("internet",0),T2),
                                     (T("p7_electric"),d.get("luz",0),T2),
                                     (T("p7_water"),d.get("agua",0),T2),
                                     (T("p7_mobile"),d.get("data_movil",0),T2)], "H")
        res_card(f, T("p7_loans"),  [(T("p7_loan_p"),d.get("prestamo_personal",0),T2),
                                     (T("p7_loan_a"),d.get("prestamo_auto",0),T2),
                                     (T("p7_debts"),d.get("deudas",0),T2)], "D")
        res_card(f, T("p7_auto_pets"),[(T("p7_gas"),d.get("gasolina",0),T2),
                                       (T("p7_maint"),d.get("mantenimiento_auto",0),T2),
                                       (T("p7_pet_food"),d.get("mascota_comida",0),T2),
                                       (T("p7_pet_vet"),d.get("mascota_vet",0),T2),
                                       (T("p7_pet_other"),d.get("mascota_otros",0),T2)], "~")
        res_card(f, T("p7_vars"),   [(T("p7_grocery"),d.get("comida",0),T2),
                                     (T("p7_out"),d.get("salidas",0),T2),
                                     ("Delivery",d.get("delivery",0),T2),
                                     ("Apple One",d.get("apple_one",0),T2),
                                     ("Netflix",d.get("netflix",0),T2),
                                     ("HBO Max",d.get("hbo",0),T2),
                                     ("Disney+",d.get("disney",0),T2)], "@")
        ge = [(T("p7_extra_lbl",desc=g["desc"]),g["monto"],T2)
              for g in d.get("gastos_extra",[]) if g["monto"]>0]
        if ge: res_card(f, T("p7_extras_sec"), ge, "+")

        # ── Goal analysis ─────────────────────────────────
        goal_c = fluent_card(f, pady=6)
        section_title(goal_c, T("p7_goal"), icon_sym="G")
        for lbl, vs, col in [
            (T("p7_goal_amt"),   fmt_v(meta),  SU),
            (T("p7_months_left"),str(meses_r), T_),
            (T("p7_need_mo"),    fmt_v(nec_mes), WA),
            (T("p7_curr_mo"),    fmt_v(ahorro), SU if ahorro>=0 else DA),
            (T("p7_projection"), fmt_v(proyecc), AC),
        ]:
            r = tk.Frame(goal_c, bg=W11["surface"]); r.pack(fill="x",padx=16,pady=2)
            tk.Label(r, text=lbl, font=F_BODY, bg=W11["surface"],fg=T2).pack(side="left")
            tk.Label(r, text=vs,  font=(FONT,10,"bold"),
                     bg=W11["surface"],fg=col).pack(side="right")
        tk.Frame(goal_c, bg=W11["divider"], height=1).pack(fill="x",padx=16,pady=(8,4))

        btn_row = tk.Frame(goal_c, bg=W11["surface"])
        btn_row.pack(fill="x", padx=16, pady=(4,14))

        def exportar():
            ruta = filedialog.asksaveasfilename(
                defaultextension=".pdf", filetypes=[("PDF","*.pdf")],
                initialfile=f"report_{d.get('nombre','').replace(' ','_')}.pdf",
                title=T("pdf_save_title"))
            if ruta:
                if generar_pdf(d, ruta):
                    messagebox.showinfo(T("pdf_saved"), T("pdf_saved_msg",ruta=ruta))

        FluentButton(btn_row, text=T("p7_export"), variant="accent",
                     icon_sym="P", command=exportar).pack(side="left", padx=(0,10))
        tk.Label(goal_c, text=T("p7_new"), font=F_SMALL,
                 bg=W11["surface"], fg=W11["text3"]
                 ).pack(padx=16, pady=(0,10), anchor="w")

    def _reset(self):
        self._datos  = {}
        self._fields = {}
        self._show_step(0)

# ══════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        root = tk.Tk()
        root.withdraw()
        root.update()    # flush Tk internals — critical for Python 3.14+
        _set_window_icon(root)

        # 1) Language boot (drawn on root, no Toplevel)
        root.deiconify()
        chosen_lang = show_language_boot(root)
        set_lang(chosen_lang)
        _rebuild_theme()

        # 2) Splash (drawn on root canvas, no Toplevel)
        def _on_splash_done():
            root.overrideredirect(False)
            root.resizable(True, True)
            root.attributes("-topmost", False)
            sw = root.winfo_screenwidth(); sh = root.winfo_screenheight()
            root.geometry(f"1020x700+{(sw-1020)//2}+{(sh-700)//2}")
            root.minsize(820, 580)
            root.configure(bg=W11["bg"])
            root.title(T("app_title"))
            CalcApp(root)

        show_splash(root, _on_splash_done)
        root.mainloop()

    except Exception as e:
        import traceback
        traceback.print_exc()
        input("\nError. Press Enter / Presiona Enter para cerrar...")
