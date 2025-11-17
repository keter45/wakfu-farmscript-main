"""
Motor de automação - gerencia o ciclo de colheita
"""
import time
import pyautogui
from pyautogui import ImageNotFoundException
from src.utils.logger import logger
from src.utils.resource_loader import resource_loader
import constants as const
from src.automation import routines
from src.automation.captcha_detector import captcha_detector

class AutomationEngine:
    def __init__(self):
        self.is_running = False
        self.is_active = False
        self.job = None
        self.resource = None
        self.delay_seconds = 15
    
    def configure(self, job, resource, delay_seconds):
        self.job = job
        self.resource = resource
        self.delay_seconds = delay_seconds
        logger.info(f"Configuração: {job} | {resource} | {delay_seconds}s delay")
    
    def toggle(self):
        self.is_active = not self.is_active
        status = "ATIVADO" if self.is_active else "DESATIVADO"
        logger.info(f"🔄 Automação {status}!")
    
    def run(self):
        logger.info(f"Motor iniciado para {self.job} - {self.resource}")
        logger.info(f"Aguardando ativação via hotkey...")
        
        while self.is_running:
            time.sleep(0.2)
            
            if not self.is_active:
                continue
            
            try:
                # Verificar captcha antes de executar colheita
                if captcha_detector.detect_captcha_event():
                    logger.warning("⚠️  CAPTCHA DETECTADO! Pausando automação...")
                    self.is_active = False
                    captcha_detector.solve_captcha()
                    continue
                
                logger.action(f"Executando colheita de {self.resource}...")
                
                success = self._execute_harvest_routine()
                
                if success:
                    logger.success(f"Colheita concluída! Aguardando {self.delay_seconds}s...")
                    self._wait_with_feedback(self.delay_seconds)
                    logger.info("Ciclo completo!")
                else:
                    logger.info("Aguardando próxima tentativa...")
                    time.sleep(2)
            
            except Exception as e:
                logger.error(f"Erro no loop: {e}")
                import traceback
                traceback.print_exc()
                time.sleep(1.0)
    
    def _execute_harvest_routine(self):
        routine_map = {
            const.JOB_MINER: routines.advanced_mining_actions,
            const.JOB_FARMER: routines.advanced_farming_actions,
            const.JOB_HERBALIST: routines.advanced_herbalist_actions,
            const.JOB_LUMBERJACK: routines.advanced_lumberjack_actions,
            const.JOB_FISHERMAN: routines.advanced_fisherman_actions,
        }
        
        routine = routine_map.get(self.job)
        if routine:
            result = routine()
            return result if result is not None else True
        return False
    
    def _wait_with_feedback(self, seconds):
        for i in range(int(seconds)):
            if not self.is_running:
                break
            time.sleep(1)
            if (i + 1) % 3 == 0 or (i + 1) == int(seconds):
                remaining = int(seconds) - i - 1
                if remaining > 0:
                    logger.info(f"Aguardando: {remaining}s restantes")
    
    def start(self):
        self.is_running = True
    
    def stop(self):
        self.is_running = False
        self.is_active = False

automation_engine = AutomationEngine()
