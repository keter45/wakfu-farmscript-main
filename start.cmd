@echo off
REM Script de inicialização - Wakfu FarmScript (Versão Organizada)
echo ==========================================
echo  Wakfu FarmScript v0.3.0
echo  Versao Organizada em Pastas
echo ==========================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Verificar dependências
echo Verificando dependencias...
python -c "import pyautogui; import pynput; import tkinter" >nul 2>&1
if errorlevel 1 (
    echo [AVISO] Instalando dependencias...
    pip install -r requirements.txt
)

echo [OK] Dependencias verificadas
echo.

REM Iniciar aplicação
echo Iniciando FarmScript...
echo.
python main.py

pause
