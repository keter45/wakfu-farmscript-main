"""
Gerenciamento de hotkeys
"""
from pynput import keyboard

def doNothing():
    pass

F_KEYS = [
    "Key.f1", "Key.f2", "Key.f3", "Key.f4", "Key.f5",
    "Key.f6", "Key.f7", "Key.f8", "Key.f9", "Key.f10",
]

initialKeyBindings = {key: doNothing for key in F_KEYS}

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class HotkeyManager(metaclass=Singleton):
    def __init__(self):
        self.isActive = False
        self._bindings = initialKeyBindings.copy()
    
    def setBinding(self, key, callback: callable):
        self._bindings[key] = callback
    
    def clearBinding(self, key):
        self._bindings[key] = doNothing
    
    def isBound(self, key):
        return not (self._bindings[key] is doNothing)
    
    def runHotkeyCallback(self, key):
        try:
            srtKey = str(key)
            if srtKey in F_KEYS:
                self._bindings.get(srtKey)()
        except:
            print("ERROR: Run Hotkey callback failed")

class HotkeyListener(metaclass=Singleton):
    def __init__(self, hkCallback: callable):
        self.hkCallback = hkCallback
        self.listener = None
        self.isActive = False
    
    def startScript(self):
        if not self.isActive:
            self.listener = keyboard.Listener(on_release=self.hkCallback)
            self.listener.start()
            self.isActive = True
    
    def stopScript(self):
        if self.isActive:
            self.listener.stop()
            self.listener = None
            self.isActive = False

globalHotkeyManager = HotkeyManager()
hotkeyListener = HotkeyListener(globalHotkeyManager.runHotkeyCallback)
