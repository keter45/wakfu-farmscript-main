"""
Estado global da aplicação
"""
import constants as const

class GlobalState:
    def __init__(self):
        self.selectedJob = None
        self.selectedResource = None
        self.selectedKey = None
        self.status = const.STATUS_WAITING
        self.isKeyComboEnabled = True
        self.isStartButtonEnabled = True
        self.isStopButtonEnabled = False
        self.isResourceComboEnabled = False
        self.cutOnlyMode = False  # Modo que só usa Cut, sem Harvest

globalState = GlobalState()
