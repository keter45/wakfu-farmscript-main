#!/usr/bin/env python3
"""
Instalador do Wakfu FarmScript
Verifica dependências e instala automaticamente
"""

import sys
import subprocess
import os

def print_header():
    print("\n" + "="*60)
    print("  INSTALADOR - WAKFU FARMSCRIPT v0.2.1")
    print("="*60 + "\n")

def check_python_version():
    """Verifica versão do Python"""
    print("🔍 Verificando versão do Python...")
    version = sys.version_info
    print(f"   Versão encontrada: Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3:
        print(f"   ✗ ERRO: Python 3.8+ é necessário!")
        print(f"   Baixe em: https://www.python.org/downloads/")
        return False
    
    if version.major == 3 and version.minor < 8:
        print(f"   ⚠️  Aviso: Python 3.8+ é recomendado (você tem {version.major}.{version.minor})")
        print(f"   O script pode não funcionar corretamente.")
        resp = input("\n   Deseja continuar mesmo assim? (s/N): ")
        if resp.lower() != 's':
            return False
    else:
        print(f"   ✓ Versão compatível!\n")
    
    return True

def check_pip():
    """Verifica se pip está instalado"""
    print("🔍 Verificando pip...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
        print("   ✓ pip instalado!\n")
        return True
    except:
        print("   ✗ pip não encontrado!")
        print("   Por favor, instale o pip primeiro.")
        print("   Visite: https://pip.pypa.io/en/stable/installation/")
        return False

def install_requirements():
    """Instala os requirements"""
    print("📦 Instalando dependências...")
    print("   (Isso pode levar alguns minutos...)\n")
    
    # Garante que está no diretório correto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    requirements_path = os.path.join(script_dir, 'requirements.txt')
    
    if not os.path.exists(requirements_path):
        print(f"   ✗ Arquivo requirements.txt não encontrado!")
        print(f"   Procurado em: {requirements_path}")
        return False
    
    try:
        # Atualizar pip primeiro
        print("   [1/2] Atualizando pip...")
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip', '--quiet'
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("        ✓ pip atualizado\n")
        
        # Instalar requirements
        print("   [2/2] Instalando bibliotecas...")
        print("        - pyautogui")
        print("        - pynput")
        print("        - opencv-python")
        print("        - pillow")
        
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', requirements_path
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("\n        ✓ Todas as bibliotecas instaladas!\n")
            return True
        else:
            print(f"\n   ✗ Erro ao instalar dependências:")
            print(f"   {result.stderr}")
            return False
            
    except Exception as e:
        print(f"\n   ✗ Erro ao instalar dependências:")
        print(f"   {e}\n")
        return False

def check_files():
    """Verifica se os arquivos necessários existem"""
    print("🔍 Verificando estrutura do projeto...")
    
    files_needed = [
        'main.py',
        'calibrator.py',
        'constants.py',
        'requirements.txt',
    ]
    
    folders_needed = [
        'src',
        'img',
        'docs',
    ]
    
    all_ok = True
    
    print("\n   Arquivos:")
    for file in files_needed:
        if os.path.exists(file):
            print(f"   ✓ {file}")
        else:
            print(f"   ✗ {file} - NÃO ENCONTRADO")
            all_ok = False
    
    print("\n   Pastas:")
    for folder in folders_needed:
        if os.path.exists(folder) and os.path.isdir(folder):
            print(f"   ✓ {folder}/")
        else:
            print(f"   ✗ {folder}/ - NÃO ENCONTRADO")
            all_ok = False
    
    print()
    return all_ok

def create_shortcuts():
    """Cria atalhos para facilitar o uso"""
    print("🔗 Criando atalhos...")
    
    try:
        # Atalho para iniciar (batch file)
        start_bat = """@echo off
title Wakfu FarmScript
pythonw main.py
"""
        with open('Iniciar FarmScript.cmd', 'w') as f:
            f.write(start_bat)
        print("   ✓ Iniciar FarmScript.cmd")
        
        # Atalho .bat (com terminal)
        bat_file = """@echo off
title Wakfu FarmScript
cd /d "%~dp0"
python main.py
pause
"""
        with open('Wakfu FarmScript.bat', 'w') as f:
            f.write(bat_file)
        print("   ✓ Wakfu FarmScript.bat")
        
        # Atalho .vbs (sem terminal)
        vbs_file = """Set WshShell = CreateObject("WScript.Shell")
WshShell.CurrentDirectory = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WshShell.Run "python main.py", 1, False
"""
        with open('Wakfu FarmScript.vbs', 'w') as f:
            f.write(vbs_file)
        print("   ✓ Wakfu FarmScript.vbs (sem terminal)")
        
        # Atalho para calibrar
        calibrate_bat = """@echo off
title Wakfu FarmScript - Calibrador
python calibrator.py
pause
"""
        with open('Calibrar.cmd', 'w') as f:
            f.write(calibrate_bat)
        print("   ✓ Calibrar.cmd")
        
        # Atalho para verificar instalação
        verify_bat = """@echo off
title Wakfu FarmScript - Verificar
python verificar.cmd
pause
"""
        with open('Verificar Instalação.cmd', 'w') as f:
            f.write(verify_bat)
        print("   ✓ Verificar Instalação.cmd\n")
        
        return True
    except Exception as e:
        print(f"   ⚠️  Não foi possível criar atalhos: {e}\n")
        return False

def print_next_steps():
    """Mostra os próximos passos"""
    print("="*60)
    print("✓ INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)
    print("\n🚀 PRÓXIMOS PASSOS:\n")
    print("1. CALIBRAR o jogo:")
    print("   → Execute: Calibrar.cmd")
    print("   → Ou: python calibrator.py")
    print("   → Capture a área do jogo na tela\n")
    
    print("2. CONFIGURAR profissão:")
    print("   → Execute: Iniciar FarmScript.cmd")
    print("   → Ou: python main.py")
    print("   → Selecione profissão e recurso\n")
    
    print("3. CAPTURAR imagens dos recursos:")
    print("   → Na interface, clique em '📷 Calibrar'")
    print("   → Capture as imagens dos recursos que deseja farmar")
    print("   → Recursos com ✓ já têm imagem\n")
    
    print("4. INICIAR automação:")
    print("   → Clique em 'Start'")
    print("   → Pressione a hotkey (padrão: F2) para ativar/desativar\n")
    
    print("="*60)
    print("📚 DOCUMENTAÇÃO: docs/")
    print("❓ DÚVIDAS: Leia o README.md")
    print("="*60 + "\n")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    
    print("Este instalador irá:")
    print("  • Verificar Python e pip")
    print("  • Instalar todas as dependências")
    print("  • Verificar arquivos do projeto")
    print("  • Criar atalhos de conveniência")
    print("\nPressione ENTER para começar (ou Ctrl+C para cancelar)...")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\n\nInstalação cancelada pelo usuário.")
        return False
    
    # 1. Verificar Python
    if not check_python_version():
        input("\nPressione ENTER para sair...")
        return False
    
    # 2. Verificar pip
    if not check_pip():
        input("\nPressione ENTER para sair...")
        return False
    
    # 3. Verificar arquivos
    if not check_files():
        print("⚠️  Aviso: Alguns arquivos estão faltando!")
        print("Certifique-se de estar no diretório correto do projeto.\n")
        resp = input("Deseja continuar mesmo assim? (s/N): ")
        if resp.lower() != 's':
            return False
    
    # 4. Instalar requirements
    print()
    if not install_requirements():
        input("\nPressione ENTER para sair...")
        return False
    
    # 5. Criar atalhos
    create_shortcuts()
    
    # 6. Sucesso!
    print_next_steps()
    
    input("Pressione ENTER para sair...")
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nInstalação cancelada pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n✗ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        input("\nPressione ENTER para sair...")
        sys.exit(1)
