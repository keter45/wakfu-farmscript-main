@echo off
REM Verificação da estrutura organizada
echo ==========================================
echo  Verificacao da Estrutura do Projeto
echo ==========================================
echo.

echo [Verificando estrutura...]
echo.

REM Verificar pastas principais
if exist "src\core" (
    echo [OK] src\core\ existe
) else (
    echo [ERRO] src\core\ NAO encontrada
)

if exist "src\gui" (
    echo [OK] src\gui\ existe
) else (
    echo [ERRO] src\gui\ NAO encontrada
)

if exist "src\automation" (
    echo [OK] src\automation\ existe
) else (
    echo [ERRO] src\automation\ NAO encontrada
)

if exist "src\utils" (
    echo [OK] src\utils\ existe
) else (
    echo [ERRO] src\utils\ NAO encontrada
)

if exist "docs" (
    echo [OK] docs\ existe
) else (
    echo [ERRO] docs\ NAO encontrada
)

if exist "legacy" (
    echo [OK] legacy\ existe (arquivos antigos)
) else (
    echo [AVISO] legacy\ NAO encontrada
)

echo.
echo [Verificando arquivos principais...]
echo.

if exist "main.py" (
    echo [OK] main.py existe
) else (
    echo [ERRO] main.py NAO encontrado
)

if exist "constants.py" (
    echo [OK] constants.py existe
) else (
    echo [ERRO] constants.py NAO encontrado
)

if exist "start.cmd" (
    echo [OK] start.cmd existe
) else (
    echo [ERRO] start.cmd NAO encontrado
)

echo.
echo [Verificando modulos em src/...]
echo.

if exist "src\core\state.py" (
    echo [OK] src\core\state.py
) else (
    echo [ERRO] src\core\state.py NAO encontrado
)

if exist "src\core\hotkey_manager.py" (
    echo [OK] src\core\hotkey_manager.py
) else (
    echo [ERRO] src\core\hotkey_manager.py NAO encontrado
)

if exist "src\gui\controller.py" (
    echo [OK] src\gui\controller.py
) else (
    echo [ERRO] src\gui\controller.py NAO encontrado
)

if exist "src\automation\engine.py" (
    echo [OK] src\automation\engine.py
) else (
    echo [ERRO] src\automation\engine.py NAO encontrado
)

if exist "src\automation\routines.py" (
    echo [OK] src\automation\routines.py
) else (
    echo [ERRO] src\automation\routines.py NAO encontrado
)

if exist "src\utils\logger.py" (
    echo [OK] src\utils\logger.py
) else (
    echo [ERRO] src\utils\logger.py NAO encontrado
)

if exist "src\utils\config.py" (
    echo [OK] src\utils\config.py
) else (
    echo [ERRO] src\utils\config.py NAO encontrado
)

if exist "src\utils\helpers.py" (
    echo [OK] src\utils\helpers.py
) else (
    echo [ERRO] src\utils\helpers.py NAO encontrado
)

if exist "src\utils\resource_loader.py" (
    echo [OK] src\utils\resource_loader.py
) else (
    echo [ERRO] src\utils\resource_loader.py NAO encontrado
)

echo.
echo [Verificando documentacao...]
echo.

if exist "docs\ESTRUTURA_PASTAS.md" (
    echo [OK] docs\ESTRUTURA_PASTAS.md
) else (
    echo [ERRO] docs\ESTRUTURA_PASTAS.md NAO encontrado
)

if exist "docs\ARQUITETURA.md" (
    echo [OK] docs\ARQUITETURA.md
) else (
    echo [ERRO] docs\ARQUITETURA.md NAO encontrado
)

if exist "docs\REFATORACAO.md" (
    echo [OK] docs\REFATORACAO.md
) else (
    echo [ERRO] docs\REFATORACAO.md NAO encontrado
)

echo.
echo ==========================================
echo  Verificacao Completa!
echo ==========================================
echo.
echo Para iniciar o FarmScript, execute:
echo     start.cmd
echo.
pause
