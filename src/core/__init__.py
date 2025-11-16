"""
Módulo Core - Gerenciamento de estado e hotkeys
"""
from .state import GlobalState, globalState
from .hotkey_manager import HotkeyManager, HotkeyListener, globalHotkeyManager, hotkeyListener

__all__ = ['GlobalState', 'globalState', 'HotkeyManager', 'HotkeyListener', 'globalHotkeyManager', 'hotkeyListener']
