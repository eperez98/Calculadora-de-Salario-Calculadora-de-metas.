@echo off
:: ============================================================================
::  Salary & Goals Calculator — v1.0 RC
::  One-click build script: PyInstaller → Inno Setup
::  Author: Erick Perez  |  Released: 03/15/2026
:: ============================================================================
title Building SalaryGoalsCalculator v1.0 RC...

echo.
echo ============================================================
echo   Salary ^& Goals Calculator — v1.0 RC Build Script
echo   by Erick Perez
echo ============================================================
echo.

:: ── Check Python ─────────────────────────────────────────────────────────────
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Install from https://python.org
    pause & exit /b 1
)
echo [OK] Python found:
python --version

:: ── Install / upgrade dependencies ───────────────────────────────────────────
echo.
echo [1/4] Installing dependencies...
pip install --upgrade pyinstaller pillow reportlab >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip install failed. Check your internet connection.
    pause & exit /b 1
)
echo [OK] pyinstaller, pillow, reportlab ready

:: ── Clean previous build ─────────────────────────────────────────────────────
echo.
echo [2/4] Cleaning previous build artifacts...
if exist dist\SalaryGoalsCalculator.exe (
    del /q dist\SalaryGoalsCalculator.exe
    echo [OK] Removed old dist\SalaryGoalsCalculator.exe
)
if exist build rmdir /s /q build >nul 2>&1
if exist SalaryGoalsCalculator.spec del /q SalaryGoalsCalculator.spec >nul 2>&1

:: ── PyInstaller ──────────────────────────────────────────────────────────────
echo.
echo [3/4] Running PyInstaller (this may take 1-3 minutes)...
echo.

pyinstaller --onefile --windowed ^
  --name "SalaryGoalsCalculator" ^
  --icon "assets\icon.ico" ^
  --add-data "assets;assets" ^
  --hidden-import reportlab ^
  --hidden-import reportlab.graphics ^
  --hidden-import reportlab.platypus ^
  --hidden-import reportlab.lib ^
  --hidden-import PIL ^
  --hidden-import PIL.Image ^
  --hidden-import PIL.ImageDraw ^
  --hidden-import PIL.ImageFont ^
  --hidden-import PIL.ImageTk ^
  --hidden-import PIL.ImageFilter ^
  --collect-all reportlab ^
  --collect-all PIL ^
  Calculadora_Ahorro.py

if errorlevel 1 (
    echo.
    echo [ERROR] PyInstaller failed. See output above.
    pause & exit /b 1
)

if not exist dist\SalaryGoalsCalculator.exe (
    echo [ERROR] dist\SalaryGoalsCalculator.exe was not created.
    pause & exit /b 1
)

echo.
echo [OK] dist\SalaryGoalsCalculator.exe created successfully
for %%I in (dist\SalaryGoalsCalculator.exe) do echo     Size: %%~zI bytes

:: ── Inno Setup ───────────────────────────────────────────────────────────────
echo.
echo [4/4] Running Inno Setup compiler...
echo.

:: Try common Inno Setup install locations
set ISCC=
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    set ISCC="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
)
if exist "C:\Program Files\Inno Setup 6\ISCC.exe" (
    set ISCC="C:\Program Files\Inno Setup 6\ISCC.exe"
)

if "%ISCC%"=="" (
    echo [SKIP] Inno Setup not found at default location.
    echo.
    echo  To create the installer manually:
    echo    1. Download Inno Setup 6 from: https://jrsoftware.org/isdl.php
    echo    2. Open installer.iss in the Inno Setup IDE
    echo    3. Press F9 to compile
    echo    4. Find output at: Output\SalaryGoalsCalculator_v1.0RC_Setup.exe
    echo.
    echo  Your .exe is ready at: dist\SalaryGoalsCalculator.exe
    echo  You can distribute that file directly without the installer.
    goto :done
)

if not exist Output mkdir Output
%ISCC% installer.iss

if errorlevel 1 (
    echo [ERROR] Inno Setup compilation failed. See output above.
    pause & exit /b 1
)

echo.
echo [OK] Installer created:
dir Output\SalaryGoalsCalculator_v1.0RC_Setup.exe

:: ── Done ────────────────────────────────────────────────────────────────────
:done
echo.
echo ============================================================
echo   BUILD COMPLETE
echo ============================================================
echo.
echo   Standalone EXE : dist\SalaryGoalsCalculator.exe
echo   Installer      : Output\SalaryGoalsCalculator_v1.0RC_Setup.exe
echo   (installer only present if Inno Setup was found)
echo.
echo   To test the app now, run:
echo     dist\SalaryGoalsCalculator.exe
echo.
pause
