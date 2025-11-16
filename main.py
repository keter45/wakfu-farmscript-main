#!/usr/bin/env python3
"""
Wakfu FarmScript - Interface Gráfica Organizada
"""
import tkinter as tk
from tkinter import ttk
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import constants as const
from src.utils.logger import logger
from src.gui.controller import gui_controller

class FarmScriptGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{const.PROJECT_NAME} {const.VERSION}")
        self.root.geometry("500x480")
        self.root.resizable(False, False)
        
        self._setup_style()
        self._create_widgets()
        self._initialize_defaults()
        
    def _setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        self.root.configure(bg='#1e1e1e')
    
    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        self._create_job_zone_frame(main_frame)
        self._create_resource_frame(main_frame)
        self._create_hotkey_frame(main_frame)
        self._create_delay_frame(main_frame)
        self._create_control_frame(main_frame)
    
    def _create_job_zone_frame(self, parent):
        frame = ttk.LabelFrame(parent, text=const.GUI_FRAME_SELECTJOBANDZONE_TEXT, padding="10")
        frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        ttk.Label(frame, text="Profissão:").pack(side=tk.LEFT, padx=5)
        
        self.job_var = tk.StringVar(value=const.JOB_FARMER)
        job_combo = ttk.Combobox(frame, textvariable=self.job_var, state='readonly', width=15)
        job_combo['values'] = (
            const.JOB_MINER, const.JOB_LUMBERJACK, const.JOB_FARMER,
            const.JOB_FISHERMAN, const.JOB_HERBALIST, const.JOB_TRAPPER,
        )
        job_combo.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
        job_combo.bind("<<ComboboxSelected>>", self._on_job_changed)
        
        ttk.Label(frame, text="Zona:").pack(side=tk.LEFT, padx=5)
        
        self.zone_var = tk.StringVar()
        self.zone_combo = ttk.Combobox(frame, textvariable=self.zone_var, state='readonly', width=15)
        self.zone_combo['values'] = (
            const.ZONE_ASTRUB, const.ZONE_AMAKNA, const.ZONE_BRAKMAR,
            const.ZONE_WILD_ESTATE, const.ZONE_SUFOKIA, const.ZONE_BONTA,
        )
        self.zone_combo.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
        self.zone_combo.bind("<<ComboboxSelected>>", self._on_zone_changed)
    
    def _create_resource_frame(self, parent):
        frame = ttk.LabelFrame(parent, text=const.GUI_FRAME_SELECTRESOURCE_TEXT, padding="10")
        frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        resource_subframe = ttk.Frame(frame)
        resource_subframe.pack(fill=tk.BOTH, expand=True, padx=5)
        
        self.resource_var = tk.StringVar()
        self.resource_combo = ttk.Combobox(resource_subframe, textvariable=self.resource_var, state='readonly')
        self.resource_combo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.resource_combo.bind("<<ComboboxSelected>>", self._on_resource_changed)
        
        refresh_btn = ttk.Button(resource_subframe, text="🔄", command=self._refresh_resources, width=3)
        refresh_btn.pack(side=tk.LEFT, padx=5)
    
    def _create_hotkey_frame(self, parent):
        frame = ttk.LabelFrame(parent, text=const.GUI_FRAME_ASSIGNAKEY, padding="10")
        frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.key_var = tk.StringVar(value=const.KEY_STR_F2)
        key_combo = ttk.Combobox(frame, textvariable=self.key_var, state='readonly')
        key_combo['values'] = (
            const.KEY_STR_F1, const.KEY_STR_F2, const.KEY_STR_F3,
            const.KEY_STR_F4, const.KEY_STR_F5, const.KEY_STR_F6, const.KEY_STR_F7,
        )
        key_combo.pack(fill=tk.BOTH, expand=True, padx=5)
        key_combo.bind("<<ComboboxSelected>>", self._on_key_changed)
    
    def _create_delay_frame(self, parent):
        frame = ttk.LabelFrame(parent, text="Configurações de Tempo", padding="10")
        frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Primeira linha: Delay
        delay_frame = ttk.Frame(frame)
        delay_frame.pack(fill=tk.X, pady=2)
        
        ttk.Label(delay_frame, text="Delay após colheita (seg):").pack(side=tk.LEFT, padx=5)
        
        self.delay_var = tk.StringVar(value="15")
        delay_spin = ttk.Spinbox(delay_frame, from_=1, to=300, textvariable=self.delay_var, width=5)
        delay_spin.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(delay_frame, text="(Aguarda barra + delay)", foreground='gray').pack(side=tk.LEFT, padx=5)
        
        # Segunda linha: Modo Cut-Only
        mode_frame = ttk.Frame(frame)
        mode_frame.pack(fill=tk.X, pady=2)
        
        self.cut_only_var = tk.BooleanVar(value=False)
        cut_only_check = ttk.Checkbutton(
            mode_frame, 
            text="Modo Cut-Only (sempre corta, nunca planta)", 
            variable=self.cut_only_var,
            command=self._on_cut_only_changed
        )
        cut_only_check.pack(side=tk.LEFT, padx=5)
    
    def _create_control_frame(self, parent):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.status_label = ttk.Label(frame, text=const.STATUS_WAITING, foreground='black')
        self.status_label.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
        
        self.start_btn = ttk.Button(frame, text=const.GUI_BUTTON_START_TEXT, command=self._on_start)
        self.start_btn.pack(side=tk.LEFT, padx=2)
        
        self.stop_btn = ttk.Button(frame, text=const.GUI_BUTTON_STOP_TEXT, command=self._on_stop, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=2)
        
        calibrate_btn = ttk.Button(frame, text="📷 Calibrar", command=self._on_calibrate)
        calibrate_btn.pack(side=tk.LEFT, padx=2)
    
    def _initialize_defaults(self):
        self._on_job_changed(None)
    
    def _on_job_changed(self, event):
        job = self.job_var.get()
        gui_controller.select_job(job)
        self._update_resources()
    
    def _on_zone_changed(self, event):
        zone = self.zone_var.get()
        gui_controller.select_zone(zone)
        self._update_resources()
    
    def _on_resource_changed(self, event):
        resource = self.resource_var.get()
        gui_controller.select_resource(resource)
    
    def _on_key_changed(self, event):
        key = self.key_var.get()
        gui_controller.select_key(key)
    
    def _on_cut_only_changed(self):
        cut_only = self.cut_only_var.get()
        gui_controller.set_cut_only_mode(cut_only)
    
    def _update_resources(self):
        job = self.job_var.get()
        if not job:
            return
        
        resources = gui_controller.get_resources_for_job(job)
        self.resource_combo['values'] = resources
        self.resource_var.set('')
    
    def _refresh_resources(self):
        self._update_resources()
    
    def _on_start(self):
        delay = self.delay_var.get()
        
        if gui_controller.start_automation(delay):
            self.status_label.config(text=const.STATUS_ACTIVE, foreground='green')
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self._disable_controls()
    
    def _on_stop(self):
        gui_controller.stop_automation()
        self.status_label.config(text=const.STATUS_STOPPED, foreground='red')
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self._enable_controls()
    
    def _on_calibrate(self):
        gui_controller.open_calibrator()
    
    def _disable_controls(self):
        for child in self.root.winfo_children():
            self._set_widget_state(child, tk.DISABLED)
    
    def _enable_controls(self):
        for child in self.root.winfo_children():
            self._set_widget_state(child, 'readonly')
    
    def _set_widget_state(self, widget, state):
        if isinstance(widget, ttk.Combobox):
            widget.config(state=state)
        for child in widget.winfo_children():
            self._set_widget_state(child, state)

def main():
    logger.info(f"Iniciando {const.PROJECT_NAME} {const.VERSION}")
    root = tk.Tk()
    app = FarmScriptGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
