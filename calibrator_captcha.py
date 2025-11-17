"""
Calibrador para Captcha do Wakfu
Permite capturar as regiões e padrões necessários
"""
import pyautogui as auto
import cv2
import numpy as np
from PIL import Image
import os

def capture_cat_reference():
    """Captura imagem de referência do gato branco"""
    print("\n=== CAPTURAR GATO DE REFERÊNCIA ===")
    print("Posicione o cursor sobre o GATO BRANCO e pressione ENTER...")
    input()
    
    x, y = auto.position()
    print(f"Capturando região ao redor de ({x}, {y})...")
    
    # Captura área 100x100 ao redor do gato
    screenshot = auto.screenshot(region=(x-50, y-50, 100, 100))
    
    os.makedirs('img/captcha', exist_ok=True)
    screenshot.save('img/captcha/cat.png')
    print("✓ Gato salvo em: img/captcha/cat.png\n")

def capture_pattern_samples():
    """Captura amostras dos diferentes padrões de tile"""
    print("\n=== CAPTURAR PADRÕES DE TILES ===")
    
    patterns = [
        ("X (cruz)", "x_pattern.png"),
        ("Vazio", "empty_pattern.png"),
        ("Padrão 1 (bolhas)", "pattern1.png"),
        ("Padrão 2", "pattern2.png"),
        ("Padrão 3", "pattern3.png"),
    ]
    
    for name, filename in patterns:
        print(f"\nPosicione o cursor sobre um tile com: {name}")
        print("Pressione ENTER para capturar...")
        input()
        
        x, y = auto.position()
        # Captura tile inteiro (aproximadamente 80x80)
        screenshot = auto.screenshot(region=(x-40, y-40, 80, 80))
        screenshot.save(f'img/captcha/{filename}')
        print(f"✓ Salvo: img/captcha/{filename}")

def capture_number_samples():
    """Captura múltiplas amostras dos números 1-8 (para lidar com animação)"""
    print("\n=== CAPTURAR NÚMEROS (1-8) ===")
    print("Vamos capturar MÚLTIPLOS FRAMES de cada número")
    print("Isso ajuda a reconhecer mesmo com a animação!")
    print("\nOpções:")
    print("  1. Captura rápida (5 frames)")
    print("  2. Captura média (10 frames)")
    print("  3. Captura completa (20 frames - ciclo inteiro)")
    print("  4. Personalizado")
    
    choice = input("\nEscolha (padrão: 2): ").strip() or "2"
    
    if choice == "1":
        num_frames = 5
        delay = 0.2
    elif choice == "2":
        num_frames = 10
        delay = 0.15
    elif choice == "3":
        num_frames = 20
        delay = 0.1
    else:
        try:
            num_frames = int(input("Quantos frames? ").strip() or "10")
            delay = float(input("Delay entre frames (seg)? ").strip() or "0.15")
        except:
            num_frames = 10
            delay = 0.15
    
    print(f"\n✓ Capturando {num_frames} frames por número (delay: {delay}s)\n")
    
    for num in range(1, 9):
        print(f"\n{'='*60}")
        print(f"NÚMERO {num}")
        print(f"{'='*60}")
        print(f"Posicione o cursor sobre o número {num}")
        print(f"Vamos capturar {num_frames} frames da animação completa")
        print("Pressione ENTER para começar...")
        input()
        
        x, y = auto.position()
        
        # Criar pasta para este número
        num_folder = f'img/captcha/number_{num}'
        os.makedirs(num_folder, exist_ok=True)
        
        print(f"\n📸 Capturando animação...")
        print("▶ Gravando", end="", flush=True)
        
        import time
        best_frame = None
        
        for frame in range(num_frames):
            screenshot = auto.screenshot(region=(x-40, y-40, 80, 80))
            screenshot.save(f'{num_folder}/frame_{frame:03d}.png')
            
            # Salvar frame do meio como "melhor"
            if frame == num_frames // 2:
                best_frame = screenshot
            
            print(".", end="", flush=True)
            time.sleep(delay)
        
        print(f" ✓\n")
        print(f"✓ {num_frames} frames salvos em: {num_folder}/")
        
        # Salvar melhor frame
        if best_frame:
            best_frame.save(f'img/captcha/number_{num}_best.png')
            print(f"✓ Melhor frame: img/captcha/number_{num}_best.png")

def calibrate_grid_regions():
    """Define as regiões dos grids"""
    print("\n=== CALIBRAR REGIÕES DOS GRIDS ===")
    
    print("\nGrid do JOGADOR (números 1-8):")
    print("Clique no canto SUPERIOR ESQUERDO do grid e pressione ENTER...")
    input()
    player_x1, player_y1 = auto.position()
    
    print("Clique no canto INFERIOR DIREITO do grid e pressione ENTER...")
    input()
    player_x2, player_y2 = auto.position()
    
    print("\nGrid do GATO (padrões):")
    print("Clique no canto SUPERIOR ESQUERDO do grid e pressione ENTER...")
    input()
    cat_x1, cat_y1 = auto.position()
    
    print("Clique no canto INFERIOR DIREITO do grid e pressione ENTER...")
    input()
    cat_x2, cat_y2 = auto.position()
    
    # Salvar configuração
    config = {
        "player_grid": {
            "x1": player_x1, "y1": player_y1,
            "x2": player_x2, "y2": player_y2
        },
        "cat_grid": {
            "x1": cat_x1, "y1": cat_y1,
            "x2": cat_x2, "y2": cat_y2
        }
    }
    
    import json
    with open('captcha_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print("\n✓ Configuração salva em: captcha_config.json")
    print(f"Grid Jogador: ({player_x1},{player_y1}) -> ({player_x2},{player_y2})")
    print(f"Grid Gato: ({cat_x1},{cat_y1}) -> ({cat_x2},{cat_y2})")

def main():
    print("="*60)
    print("  CALIBRADOR DE CAPTCHA - WAKFU")
    print("="*60)
    print("\nEste calibrador vai capturar:")
    print("  1. Imagem do gato branco (detector)")
    print("  2. Padrões de tiles (X, vazio, padrões)")
    print("  3. Números 1-8 (para reconhecimento)")
    print("  4. Regiões dos grids")
    print("\nCertifique-se de que o captcha está ATIVO na tela!")
    print("\nPressione ENTER para começar...")
    input()
    
    # Menu
    while True:
        print("\n" + "="*60)
        print("MENU:")
        print("  1. Capturar gato de referência")
        print("  2. Capturar padrões de tiles")
        print("  3. Capturar números (1-8)")
        print("  4. Calibrar regiões dos grids")
        print("  5. Fazer tudo automaticamente")
        print("  0. Sair")
        print("="*60)
        
        choice = input("\nEscolha: ").strip()
        
        if choice == "1":
            capture_cat_reference()
        elif choice == "2":
            capture_pattern_samples()
        elif choice == "3":
            capture_number_samples()
        elif choice == "4":
            calibrate_grid_regions()
        elif choice == "5":
            capture_cat_reference()
            capture_pattern_samples()
            capture_number_samples()
            calibrate_grid_regions()
            print("\n✓ Calibração completa!")
            break
        elif choice == "0":
            break
        else:
            print("Opção inválida!")
    
    print("\nCalibrador finalizado!")

if __name__ == "__main__":
    main()
