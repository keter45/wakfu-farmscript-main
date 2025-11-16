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
    print("  INSTALADOR - WAKFU FARMSCRIPT")
    print("="*60 + "\n")

def check_python_version():
    """Verifica versão do Python"""
    print("✓ Verificando versão do Python...")
    version = sys.version_info
    print(f"  Versão encontrada: Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print(f"⚠️  Aviso: Python 3.9+ é recomendado (você tem {version.major}.{version.minor})")
    else:
        print(f"  ✓ Versão OK!")
    return True

def install_requirements():
    """Instala os requirements"""
    print("\n✓ Instalando dependências...")
    print("  (Esta pode levar alguns minutos...)\n")
    
    try:
        # Atualizar pip
        print("[1/2] Atualizando pip...")
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("      ✓ pip atualizado\n")
        
        # Instalar requirements
        print("[2/2] Instalando bibliotecas do requirements.txt...")
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ])
        print("      ✓ Bibliotecas instaladas!\n")
        return True
    except Exception as e:
        print(f"\n✗ Erro ao instalar dependências:")
        print(f"  {e}\n")
        return False

def check_files():
    """Verifica se os arquivos necessários existem"""
    print("✓ Verificando arquivos do projeto...")
    
    files_needed = [
        'FarmScriptGUI_Tkinter.py',
        'calibrator.py',
        'constants.py',
        'core.py',
        'routines.py',
        'requirements.txt',
    ]
    
    all_ok = True
    for file in files_needed:
        if os.path.exists(file):
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - NÃO ENCONTRADO")
            all_ok = False
    
    return all_ok

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    
    print("Este programa instalará todas as dependências necessárias.\n")
    input("Pressione ENTER para continuar...")
    
    # Verificar Python
    if not check_python_version():
        return False
    
    # Verificar arquivos
    if not check_files():
        print("\n⚠️  Aviso: Alguns arquivos não foram encontrados!")
        print("Certifique-se de estar no diretório correto do projeto.\n")
        return False
    
    # Instalar requirements
    if not install_requirements():
        return False
    
    # Sucesso
    print("="*60)
    print("✓ INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)
    print("\n🚀 Próximos passos:")
    print("  1. Execute: python FarmScriptGUI_Tkinter.py")
    print("  2. Configure o Job, Zona e Recurso")
    print("  3. Clique em '📷 Calibrar' para capturar imagens")
    print("  4. Inicie a automação!\n")
    
    input("Pressione ENTER para sair...")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
