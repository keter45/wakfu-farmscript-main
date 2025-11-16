@echo off
REM ============================================================
REM Instalador do Wakfu FarmScript
REM ============================================================
color 0A
title Wakfu FarmScript - Instalador

echo.
echo ============================================================
echo   INSTALADOR - WAKFU FARMSCRIPT
echo ============================================================
echo.
echo Este programa instalara todas as dependencias necessarias
echo.
pause

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERRO] Python nao foi encontrado no sistema!
    echo.
    echo Baixe Python 3.14+ em: https://www.python.org/downloads/
    echo Certifique-se de marcar "Add Python to PATH" durante instalacao
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado!
echo.
echo Instalando dependencias...
echo.

REM Atualizar pip
echo [1/2] Atualizando pip...
python -m pip install --upgrade pip >nul 2>&1

REM Instalar requirements
echo [2/2] Instalando bibliotecas...
python -m pip install -r requirements.txt

echo.
echo ============================================================
echo INSTALACAO CONCLUIDA!
echo ============================================================
echo.
echo Agora voce pode rodar: python FarmScriptGUI_Tkinter.py
echo.
pause
