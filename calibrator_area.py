#!/usr/bin/env python3
"""
Calibrador de Área do Jogo para Wakfu FarmScript
Permite definir a área correta da tela onde o jogo está rodando
Especialmente útil para resoluções ultra-wide
"""
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
import json
import pyautogui as auto

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = "game_area_config.json"

class GameAreaCalibrator:
    def __init__(self, root):
        self.root = root
        self.root.title("Wakfu FarmScript - Calibrador de Área do Jogo")
        self.root.geometry("600x500")
        
        self.screen_width, self.screen_height = auto.size()
        self.load_config()
        self.create_widgets()
        
    def load_config(self):
        """Carregar configuração existente ou usar padrão"""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    self.config = json.load(f)
            except:
                self.config = self.get_default_config()
        else:
            self.config = self.get_default_config()
    
    def get_default_config(self):
        """Configuração padrão (tela inteira)"""
        return {
            "game_x": 0,
            "game_y": 0,
            "game_width": self.screen_width,
            "game_height": self.screen_height,
            "center_x": self.screen_width // 2,
            "center_y": self.screen_height // 2
        }
    
    def save_config(self):
        """Salvar configuração em arquivo"""
        with open(CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=2)
        messagebox.showinfo("Sucesso", "Configuração salva!")
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Info
        info_frame = ttk.LabelFrame(main_frame, text="Informações", padding="10")
        info_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        info_text = f"""
Resolução da tela: {self.screen_width}x{self.screen_height}

Este calibrador define a área exata onde o jogo está rodando.
Útil para resoluções ultra-wide onde o jogo ocupa apenas parte da tela.

INSTRUÇÕES:
1. Defina as coordenadas X, Y onde o jogo começa
2. Defina a largura e altura da janela do jogo
3. Clique em "Salvar Configuração"

Exemplo para ultra-wide (jogo à esquerda):
X: 0, Y: 0, Largura: 1920, Altura: 1440
"""
        ttk.Label(info_frame, text=info_text, justify=tk.LEFT).pack()
        
        # Configuration
        config_frame = ttk.LabelFrame(main_frame, text="Configuração", padding="10")
        config_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Game X
        ttk.Label(config_frame, text="Posição X (esquerda):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.x_var = tk.StringVar(value=str(self.config["game_x"]))
        ttk.Entry(config_frame, textvariable=self.x_var, width=10).grid(row=0, column=1, padx=5, pady=5)
        
        # Game Y
        ttk.Label(config_frame, text="Posição Y (topo):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.y_var = tk.StringVar(value=str(self.config["game_y"]))
        ttk.Entry(config_frame, textvariable=self.y_var, width=10).grid(row=1, column=1, padx=5, pady=5)
        
        # Game Width
        ttk.Label(config_frame, text="Largura (width):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.width_var = tk.StringVar(value=str(self.config["game_width"]))
        ttk.Entry(config_frame, textvariable=self.width_var, width=10).grid(row=2, column=1, padx=5, pady=5)
        
        # Game Height
        ttk.Label(config_frame, text="Altura (height):").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.height_var = tk.StringVar(value=str(self.config["game_height"]))
        ttk.Entry(config_frame, textvariable=self.height_var, width=10).grid(row=3, column=1, padx=5, pady=5)
        
        # Center calculation
        ttk.Label(config_frame, text="Centro X (calculado):").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.center_x_label = ttk.Label(config_frame, text=str(self.config["center_x"]), foreground='blue')
        self.center_x_label.grid(row=4, column=1, padx=5, pady=5)
        
        ttk.Label(config_frame, text="Centro Y (calculado):").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.center_y_label = ttk.Label(config_frame, text=str(self.config["center_y"]), foreground='blue')
        self.center_y_label.grid(row=5, column=1, padx=5, pady=5)
        
        # Bind changes to update center
        self.width_var.trace('w', self.update_center)
        self.height_var.trace('w', self.update_center)
        self.x_var.trace('w', self.update_center)
        self.y_var.trace('w', self.update_center)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        ttk.Button(button_frame, text="Resetar para Padrão", command=self.reset_default).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Salvar Configuração", command=self.on_save).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Pronto", foreground='blue')
        self.status_label.pack(pady=10)
    
    def update_center(self, *args):
        """Atualizar o centro calculado"""
        try:
            x = int(self.x_var.get())
            y = int(self.y_var.get())
            width = int(self.width_var.get())
            height = int(self.height_var.get())
            
            center_x = x + (width // 2)
            center_y = y + (height // 2)
            
            self.center_x_label.config(text=str(center_x))
            self.center_y_label.config(text=str(center_y))
        except:
            pass
    
    def reset_default(self):
        """Resetar para configuração padrão"""
        self.x_var.set("0")
        self.y_var.set("0")
        self.width_var.set(str(self.screen_width))
        self.height_var.set(str(self.screen_height))
        self.status_label.config(text="Reset para padrão", foreground='orange')
    
    def on_save(self):
        """Salvar a configuração"""
        try:
            self.config = {
                "game_x": int(self.x_var.get()),
                "game_y": int(self.y_var.get()),
                "game_width": int(self.width_var.get()),
                "game_height": int(self.height_var.get()),
                "center_x": int(self.center_x_label.cget("text")),
                "center_y": int(self.center_y_label.cget("text"))
            }
            self.save_config()
            self.status_label.config(text="✅ Configuração salva com sucesso!", foreground='green')
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos! Digite apenas números.")
            self.status_label.config(text="❌ Erro ao salvar", foreground='red')


if __name__ == "__main__":
    root = tk.Tk()
    app = GameAreaCalibrator(root)
    root.mainloop()
