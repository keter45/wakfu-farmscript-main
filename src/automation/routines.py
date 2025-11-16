"""
Routines de colheita para cada profissão
"""
import pyautogui as auto
from src.core.state import globalState
import constants as const
from src.utils.helpers import get_closest_point, toss_coin, move_and_click, find_icon_and_click, get_action_icon_by_resource, locate_in_center_region
from src.utils.logger import logger

def _get_img_name(resource: str, subcategory: str = ""):
    suffix = f"-{subcategory}" if subcategory else ""
    return resource.replace(" ", "-") + suffix + ".png"

def simple_mining_actions():
    auto.rightClick(duration=0.2)
    find_icon_and_click(const.ICON_ACTION_MINING_HARVEST)

def simple_trapper_actions():
    auto.rightClick(duration=0.2)
    icon = const.ICON_ACTION_TRAPPER_SEEDS if toss_coin(0.50) else const.ICON_ACTION_FARMING_SEEDS
    find_icon_and_click(icon)

def advanced_mining_actions():
    ore_locations = locate_in_center_region(
        const.MINER_RES_PATH + _get_img_name(globalState.selectedResource),
        confidence=0.86
    )

    if ore_locations:
        closest = get_closest_point(ore_locations)
        if closest:
            move_and_click(closest.x, closest.y, "right")
            if not find_icon_and_click(const.ICON_ACTION_MINING_HARVEST):
                logger.warning("Ícone de mineração não encontrado")
    else:
        logger.info("Minério não encontrado")

def advanced_fisherman_actions():
    accuracy = 0.88
    fish_locations = (
        locate_in_center_region(const.FISHERMAN_RES_PATH + "fish1.png", confidence=accuracy) +
        locate_in_center_region(const.FISHERMAN_RES_PATH + "fish2.png", confidence=accuracy) +
        locate_in_center_region(const.FISHERMAN_RES_PATH + "fish3.png", confidence=accuracy) +
        locate_in_center_region(const.FISHERMAN_RES_PATH + "fish4.png", confidence=accuracy)
    )

    if fish_locations:
        closest = get_closest_point(fish_locations)
        if closest:
            move_and_click(closest.x, closest.y, "right")
            if not find_icon_and_click(const.ICON_ACTION_FISHERMAN_FISH):
                logger.warning("Ícone de pesca não encontrado")
    else:
        logger.info("Peixes não encontrados")

def advanced_farming_actions():
    resource = globalState.selectedResource
    cut_only = globalState.cutOnlyMode
    
    try:
        seeds_locations = locate_in_center_region(
            const.FARMER_RES_PATH + _get_img_name(resource, "seed"),
            confidence=0.80
        )
    except:
        seeds_locations = []

    try:
        resource_locations = locate_in_center_region(
            const.FARMER_RES_PATH + _get_img_name(resource),
            confidence=0.80
        )
    except:
        resource_locations = []

    has_seeds = len(seeds_locations) > 0
    has_resources = len(resource_locations) > 0

    if cut_only:
        # Modo Cut-Only: sempre usa "harvest" (cut)
        if has_seeds:
            closest = get_closest_point(seeds_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(get_action_icon_by_resource(const.JOB_FARMER, resource, "harvest"), confidence=0.70)
        elif has_resources:
            closest = get_closest_point(resource_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(get_action_icon_by_resource(const.JOB_FARMER, resource, "harvest"), confidence=0.70)
        else:
            logger.info("Recurso não encontrado")
    else:
        # Modo normal: alterna entre harvest e seeds
        if has_seeds and has_resources:
            if toss_coin(0.5):
                closest = get_closest_point(seeds_locations)
                if closest:
                    move_and_click(closest.x, closest.y, "right")
                    action = "harvest" if toss_coin(0.33) and len(seeds_locations) > 1 else "seeds"
                    find_icon_and_click(get_action_icon_by_resource(const.JOB_FARMER, resource, action), confidence=0.70)
            else:
                closest = get_closest_point(resource_locations)
                if closest:
                    move_and_click(closest.x, closest.y, "right")
                    find_icon_and_click(get_action_icon_by_resource(const.JOB_FARMER, resource, "harvest"), confidence=0.70)
        elif has_seeds:
            closest = get_closest_point(seeds_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(get_action_icon_by_resource(const.JOB_FARMER, resource, "seeds"), confidence=0.70)
        elif has_resources:
            closest = get_closest_point(resource_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(get_action_icon_by_resource(const.JOB_FARMER, resource, "harvest"), confidence=0.70)
        else:
            logger.info("Recurso não encontrado")

def advanced_lumberjack_actions():
    resource = globalState.selectedResource
    cut_only = globalState.cutOnlyMode
    
    mature_locations = locate_in_center_region(
        const.LUMBERJACK_RES_PATH + _get_img_name(resource, "mature"),
        confidence=0.88
    )

    little_locations = locate_in_center_region(
        const.LUMBERJACK_RES_PATH + _get_img_name(resource),
        confidence=0.88
    )

    has_mature = len(mature_locations) > 0
    has_little = len(little_locations) > 0

    if cut_only:
        # Modo Cut-Only: sempre corta (cut)
        if has_mature:
            closest = get_closest_point(mature_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(const.ICON_ACTION_LUMBERJACK_CUT_TREE)
        elif has_little:
            closest = get_closest_point(little_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(const.ICON_ACTION_FARMING_CUT)
        else:
            logger.info("Árvores não encontradas")
    else:
        # Modo normal: alterna entre get e cut
        if has_mature and has_little:
            if toss_coin(0.7):
                closest = get_closest_point(mature_locations)
                if closest:
                    move_and_click(closest.x, closest.y, "right")
                    if not find_icon_and_click(const.ICON_ACTION_LUMBERJACK_GET, confidence=0.93):
                        find_icon_and_click(const.ICON_ACTION_LUMBERJACK_CUT_TREE)
            else:
                closest = get_closest_point(little_locations)
                if closest:
                    move_and_click(closest.x, closest.y, "right")
                    find_icon_and_click(const.ICON_ACTION_FARMING_CUT)
        elif has_mature:
            closest = get_closest_point(mature_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                if not find_icon_and_click(const.ICON_ACTION_LUMBERJACK_GET):
                    find_icon_and_click(const.ICON_ACTION_LUMBERJACK_CUT_TREE)
        elif has_little:
            closest = get_closest_point(little_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(const.ICON_ACTION_FARMING_CUT)
        else:
            logger.info("Árvores não encontradas")

def advanced_herbalist_actions():
    resource = globalState.selectedResource
    cut_only = globalState.cutOnlyMode
    
    seeds_locations = locate_in_center_region(
        const.HERBALIST_RES_PATH + _get_img_name(resource, "seed"),
        confidence=0.85
    )

    resource_locations = locate_in_center_region(
        const.HERBALIST_RES_PATH + _get_img_name(resource),
        confidence=0.85
    )

    has_seeds = len(seeds_locations) > 0
    has_resources = len(resource_locations) > 0

    if cut_only:
        # Modo Cut-Only: sempre usa cut
        if has_seeds:
            closest = get_closest_point(seeds_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(const.ICON_ACTION_HERBALIST_CUT)
        elif has_resources:
            closest = get_closest_point(resource_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(const.ICON_ACTION_HERBALIST_CUT)
        else:
            logger.info("Ervas não encontradas")
    else:
        # Modo normal: alterna entre cut e seeds
        if has_seeds and has_resources:
            if toss_coin(0.66):
                closest = get_closest_point(seeds_locations)
                if closest:
                    move_and_click(closest.x, closest.y, "right")
                    icon = const.ICON_ACTION_HERBALIST_CUT if toss_coin(0.25) and len(seeds_locations) > 1 else const.ICON_ACTION_HERBALIST_SEEDS
                    find_icon_and_click(icon)
            else:
                closest = get_closest_point(resource_locations)
                if closest:
                    move_and_click(closest.x, closest.y, "right")
                    find_icon_and_click(const.ICON_ACTION_HERBALIST_CUT)
        elif has_seeds:
            closest = get_closest_point(seeds_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                icon = const.ICON_ACTION_HERBALIST_SEEDS if toss_coin(0.66) else const.ICON_ACTION_HERBALIST_CUT
                find_icon_and_click(icon)
        elif has_resources:
            closest = get_closest_point(resource_locations)
            if closest:
                move_and_click(closest.x, closest.y, "right")
                find_icon_and_click(const.ICON_ACTION_HERBALIST_CUT)
        else:
            logger.info("Ervas não encontradas")
