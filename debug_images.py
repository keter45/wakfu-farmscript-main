#!/usr/bin/env python3
"""
Script de debug para verificar as imagens disponíveis e a resolução da tela
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import constants as const
import pyautogui as auto
from pathlib import Path

print("="*60)
print("🔍 DEBUG: Verificação de Imagens e Resolução")
print("="*60)

# Resolução da tela
screenResX, screenResY = auto.size()
print(f"\n📺 Resolução da tela: {screenResX}x{screenResY}")

# Verificar imagens disponíveis
print(f"\n📁 Caminho de imagens:")
print(f"   - Farmer: {const.FARMER_RES_PATH}")
print(f"   - Herbalist: {const.HERBALIST_RES_PATH}")
print(f"   - Miner: {const.MINER_RES_PATH}")
print(f"   - Lumberjack: {const.LUMBERJACK_RES_PATH}")
print(f"   - Icons: {const.ICONS_PATH}")

# Listar imagens disponíveis
print(f"\n🖼️  Imagens disponíveis:")

def list_images(path, job_name):
    full_path = path
    if os.path.exists(full_path):
        files = os.listdir(full_path)
        print(f"\n   {job_name}:")
        for f in sorted(files):
            print(f"      - {f}")
    else:
        print(f"\n   ❌ {job_name}: Caminho não encontrado ({full_path})")

list_images(const.FARMER_RES_PATH, "Farmer")
list_images(const.HERBALIST_RES_PATH, "Herbalist")
list_images(const.MINER_RES_PATH, "Miner")
list_images(const.LUMBERJACK_RES_PATH, "Lumberjack")
list_images(const.ICONS_PATH, "Icons")

print(f"\n" + "="*60)
print("✅ Verifique se as imagens acima correspondem aos recursos que você")
print("   quer farmar. Se as imagens forem diferentes da sua resolução de tela,")
print("   será difícil detectar os recursos.")
print("="*60)
