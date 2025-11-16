"""
Controlador da interface gráfica
"""
import threading
import subprocess
from tkinter import messagebox
import constants as const
from src.utils.logger import logger
from src.utils.resource_loader import resource_loader
from src.automation.engine import automation_engine
from src.core import globalState, globalHotkeyManager, hotkeyListener

class GUIController:
    def __init__(self):
        self.selected_job = None
        self.selected_zone = None
        self.selected_resource = None
        self.selected_key = const.KEY_STR_F2
        self.is_running = False
        self.automation_thread = None
    
    def select_job(self, job):
        self.selected_job = job
        logger.info(f"Profissão selecionada: {job}")
    
    def select_zone(self, zone):
        self.selected_zone = zone
        logger.info(f"Zona selecionada: {zone}")
    
    def select_resource(self, resource):
        self.selected_resource = resource
        logger.info(f"Recurso selecionado: {resource}")
    
    def select_key(self, key):
        self.selected_key = key
        logger.info(f"Hotkey selecionada: {key}")
    
    def set_cut_only_mode(self, enabled):
        globalState.cutOnlyMode = enabled
        mode_text = "ATIVADO" if enabled else "DESATIVADO"
        logger.info(f"Modo Cut-Only: {mode_text}")
    
    def get_resources_for_job(self, job):
        return resource_loader.get_resources_for_job(job)
    
    def validate_start(self, delay):
        if not self.selected_job:
            messagebox.showerror("Erro", "Selecione uma profissão!")
            return False
        
        if not self.selected_resource:
            messagebox.showerror("Erro", "Selecione um recurso!")
            return False
        
        if not self.selected_key:
            messagebox.showerror("Erro", "Selecione uma hotkey!")
            return False
        
        try:
            delay_value = float(delay)
            if delay_value < 1 or delay_value > 300:
                messagebox.showerror("Erro", "Delay deve estar entre 1 e 300 segundos!")
                return False
        except ValueError:
            messagebox.showerror("Erro", "Delay inválido! Digite um número.")
            return False
        
        return True
    
    def start_automation(self, delay):
        if not self.validate_start(delay):
            return False
        
        self.is_running = True
        
        try:
            globalState.selectedJob = self.selected_job
            globalState.selectedZone = self.selected_zone
            globalState.selectedResource = self.selected_resource
            globalState.selectedKey = self.selected_key
            globalState.status = const.STATUS_ACTIVE
            
            logger.info("=" * 60)
            logger.info("CONFIGURAÇÕES:")
            logger.info(f"   Profissão: {self.selected_job}")
            logger.info(f"   Zona: {self.selected_zone}")
            logger.info(f"   Recurso: {self.selected_resource}")
            logger.info(f"   Hotkey: {self.selected_key}")
            logger.info(f"   Delay: {delay} segundos")
            logger.info("=" * 60)
            
            automation_engine.configure(self.selected_job, self.selected_resource, float(delay))
            automation_engine.start()
            
            def toggle_callback():
                automation_engine.toggle()
            
            globalHotkeyManager.setBinding(self.selected_key, toggle_callback)
            hotkeyListener.startScript()
            
            if not self.automation_thread or not self.automation_thread.is_alive():
                self.automation_thread = threading.Thread(
                    target=automation_engine.run,
                    daemon=True
                )
                self.automation_thread.start()
            
            logger.success(f"✓ Script iniciado! Pressione {self.selected_key} para ATIVAR/DESATIVAR")
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao iniciar automação: {e}")
            import traceback
            traceback.print_exc()
            messagebox.showerror("Erro", f"Erro ao iniciar automação:\n{e}")
            self.stop_automation()
            return False
    
    def stop_automation(self):
        self.is_running = False
        automation_engine.stop()
        
        try:
            hotkeyListener.stopScript()
            globalHotkeyManager.clearBinding(self.selected_key)
        except Exception as e:
            logger.error(f"Erro ao parar automação: {e}")
        
        logger.info("Automação parada!")
    
    def open_calibrator(self):
        try:
            subprocess.Popen(['python', 'calibrator.py'])
            logger.info("Calibrador aberto!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir calibrador:\n{e}")
            logger.error(f"Erro ao abrir calibrador: {e}")

gui_controller = GUIController()
