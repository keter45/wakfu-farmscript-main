"""
Configurações centralizadas do FarmScript
"""
import json
import os
import pyautogui as auto

CONFIG_FILE = "game_area_config.json"

class GameConfig:
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    self.width = config["game_width"]
                    self.height = config["game_height"]
                    self.offset_x = config["game_x"]
                    self.offset_y = config["game_y"]
                    self.is_configured = True
            except Exception as e:
                print(f"Erro ao carregar configuração: {e}")
                self._use_screen_defaults()
        else:
            self._use_screen_defaults()
    
    def _use_screen_defaults(self):
        self.width, self.height = auto.size()
        self.offset_x = 0
        self.offset_y = 0
        self.is_configured = False
        print(f"Usando resolução padrão: {self.width}x{self.height}")
    
    @property
    def center(self):
        return [
            int(self.offset_x + self.width / 2),
            int(self.offset_y + self.height / 2)
        ]
    
    @property
    def search_region(self):
        """Retorna região de busca de 60% da tela centralizada (left, top, width, height)"""
        search_width = int(self.width * 0.60)
        search_height = int(self.height * 0.60)
        left = int(self.offset_x + (self.width - search_width) / 2)
        top = int(self.offset_y + (self.height - search_height) / 2)
        return (left, top, search_width, search_height)

game_config = GameConfig()
