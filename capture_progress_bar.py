#!/usr/bin/env python3
"""
Script para capturar a imagem da barra de progresso
Instruções:
1. Execute este script
2. Clique em uma área do jogo e comece uma colheita
3. Quando a barra de progresso aparecer, pressione ESPAÇO para capturar
4. Pressione ESC para sair
"""

import pyautogui as auto
import time
from PIL import Image, ImageDraw
import os

# Criar pasta se não existir
os.makedirs("img", exist_ok=True)

print("=" * 60)
print("CAPTURADOR DE BARRA DE PROGRESSO")
print("=" * 60)
print("\nInstruções:")
print("1. Inicie uma colheita no jogo")
print("2. Quando a barra aparecer, pressione ESPAÇO para capturar")
print("3. Pressione ESC para sair")
print("\n⏳ Aguardando...")

# Variáveis globais
capture_ready = False
exit_program = False

def on_space():
    global capture_ready
    capture_ready = True
    print("\n📸 Capturando barra de progresso...")

def on_escape():
    global exit_program
    exit_program = True
    print("\n👋 Encerrando...")

# Listener de teclado
from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.space:
            on_space()
        elif key == keyboard.Key.esc:
            on_escape()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while not exit_program:
        time.sleep(0.1)
        
        if capture_ready:
            # Tirar screenshot da tela inteira
            screenshot = auto.screenshot()
            
            # Salvar com timestamp
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"img/progress_bar_{timestamp}.png"
            screenshot.save(filename)
            print(f"✓ Imagem salva: {filename}")
            print(f"  Resolução: {screenshot.size}")
            print(f"\nPróxima captura: pressione ESPAÇO novamente")
            print(f"Sair: pressione ESC\n")
            
            capture_ready = False
            time.sleep(0.5)

except KeyboardInterrupt:
    print("\n⚠️ Interrompido pelo usuário")

listener.stop()
print("✓ Programa finalizado")
