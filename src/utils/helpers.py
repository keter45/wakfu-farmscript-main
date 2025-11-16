"""
Funções auxiliares para automação
"""
import math
import random
import time
import os
import pyautogui as auto
from .config import game_config
from .logger import logger
import constants as const

def locate_in_center_region(image_path, confidence=0.70):
    """Busca imagem apenas na região central (60% da tela)"""
    region = game_config.search_region
    try:
        return list(auto.locateAllOnScreen(image_path, confidence=confidence, region=region))
    except:
        return []

def get_closest_point(pointlist):
    """Retorna o ponto mais próximo ao centro da tela"""
    if not pointlist:
        return None
    
    center_of_screen = game_config.center
    
    # Ordena os pontos por distância ao centro
    sorted_points = sorted(
        pointlist,
        key=lambda point: math.dist(center_of_screen, auto.center(point))
    )
    
    return auto.center(sorted_points[0]) if sorted_points else None

def get_all_points_from_center(pointlist):
    """Retorna todos os pontos ordenados do centro para as bordas"""
    if not pointlist:
        return []
    
    center_of_screen = game_config.center
    
    # Ordena todos os pontos por distância ao centro
    sorted_points = sorted(
        pointlist,
        key=lambda point: math.dist(center_of_screen, auto.center(point))
    )
    
    return [auto.center(point) for point in sorted_points]

def toss_coin(chance_event_a: float = 0.5):
    return random.random() < chance_event_a

def move_and_click(x: int, y: int, button: str = "left", sleep_time: float = 0.15):
    auto.moveTo(x, y)
    auto.click(button=button)
    time.sleep(sleep_time)

def find_icon_and_click(icon_filename: str, confidence: float = 0.75, duration: float = 0.1):
    icon_path = const.ICONS_PATH + icon_filename
    
    if not os.path.exists(icon_path):
        logger.error(f"Ícone não encontrado: {icon_path}")
        return False
    
    try:
        # Aguarda o menu aparecer
        time.sleep(0.3)
        
        # Pega a posição atual do mouse (onde o menu deve estar)
        mouse_x, mouse_y = auto.position()
        
        # Define região de busca de 500x700 pixels ao redor do cursor
        search_width = 500
        search_height = 700
        region = (
            max(0, mouse_x - search_width // 2),
            max(0, mouse_y - 100),  # Menu geralmente aparece abaixo/ao lado do cursor
            search_width,
            search_height
        )
        
        for conf in [confidence, 0.70]:
            try:
                location = auto.locateCenterOnScreen(icon_path, confidence=conf, region=region)
                if location:
                    logger.debug(f"Ícone {icon_filename} encontrado (conf={conf}) em ({location.x}, {location.y})")
                    auto.moveTo(location.x, location.y, duration=0.1)
                    time.sleep(0.1)
                    auto.click()
                    return True
            except:
                continue
        
        logger.warning(f"Ícone {icon_filename} não encontrado na região do menu (tentou conf 0.75 e 0.70)")
        return False
    
    except Exception as e:
        logger.error(f"Erro ao procurar ícone {icon_filename}: {e}")
        return False

def get_action_icon_by_resource(job: str, resource_name: str, action: str):
    if job == const.JOB_FARMER:
        resource_icons = const.ICON_FOR_ACTIONS_FARMER.get(resource_name)
        if resource_icons is None:
            return const.ICON_ACTION_FARMING_CUT if action == "harvest" else const.ICON_ACTION_FARMING_SEEDS
        
        icon = resource_icons.get(action)
        if icon is None:
            return const.ICON_ACTION_FARMING_CUT if action == "harvest" else const.ICON_ACTION_FARMING_SEEDS
        
        return icon
    
    return None
