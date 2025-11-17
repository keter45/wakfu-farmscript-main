@echo off
REM ============================================================
REM Instalador do Wakfu FarmScript v0.2.1
REM ============================================================
color 0A
title Wakfu FarmScript - Instalador

echo.
echo ============================================================
echo   INSTALADOR - WAKFU FARMSCRIPT
echo ============================================================
echo.

REM Executar instalador Python
python instalar.py

if errorlevel 1 (
    echo.
    echo ============================================================
    echo INSTALACAO FALHOU!
    echo ============================================================
    echo.
    echo Verifique os erros acima e tente novamente.
    echo.
    echo Solucoes comuns:
    echo   - Certifique-se que Python 3.8+ esta instalado
    echo   - Execute como Administrador
    echo   - Verifique sua conexao com internet
    echo.
    pause
    exit /b 1
)

echo.
echo Instalacao finalizada com sucesso!
echo.
pause
