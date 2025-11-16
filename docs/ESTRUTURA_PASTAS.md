# Estrutura de Pastas - Wakfu FarmScript v0.3.0

## 📂 Nova Estrutura Organizada

```
wakfu-farmscript/
│
├── 📁 src/                          # Código fonte organizado
│   ├── __init__.py
│   │
│   ├── 📁 core/                     # Núcleo da aplicação
│   │   ├── __init__.py
│   │   ├── state.py                 # Estado global
│   │   └── hotkey_manager.py        # Gerenciamento de hotkeys
│   │
│   ├── 📁 gui/                      # Interface gráfica
│   │   ├── __init__.py
│   │   └── controller.py            # Controlador da GUI
│   │
│   ├── 📁 automation/               # Motor de automação
│   │   ├── __init__.py
│   │   ├── engine.py                # Motor principal
│   │   └── routines.py              # Routines de colheita
│   │
│   └── 📁 utils/                    # Utilitários
│       ├── __init__.py
│       ├── logger.py                # Sistema de logging
│       ├── config.py                # Configurações
│       ├── resource_loader.py       # Carregador de recursos
│       └── helpers.py               # Funções auxiliares
│
├── 📁 img/                          # Recursos de imagem
│   ├── farmer_res/
│   ├── miner_res/
│   ├── herbalist_res/
│   ├── lumberjack_res/
│   ├── fisherman_res/
│   └── icons/
│
├── 📁 docs/                         # Documentação
│   ├── REFATORACAO.md
│   ├── MIGRACAO.md
│   └── ARQUITETURA.md
│
├── 📄 main.py                       # Ponto de entrada principal
├── 📄 constants.py                  # Constantes (raiz para compatibilidade)
├── 📄 start.cmd                     # Script de inicialização
├── 📄 requirements.txt              # Dependências
├── 📄 game_area_config.json         # Configuração de área
│
└── 📁 legacy/                       # Arquivos antigos (opcional)
    ├── FarmScriptGUI_Tkinter.py
    ├── core.py
    ├── hotkeymgr.py
    └── ...
```

## 🎯 Benefícios da Organização

### 1. **Separação Clara de Responsabilidades**

- `src/core/` - Lógica de negócio fundamental
- `src/gui/` - Interface do usuário
- `src/automation/` - Lógica de automação
- `src/utils/` - Ferramentas auxiliares

### 2. **Facilita Navegação**

- Encontre rapidamente o que precisa
- Estrutura lógica e intuitiva
- Reduz confusão com muitos arquivos na raiz

### 3. **Manutenção Simplificada**

- Modificações localizadas
- Menos conflitos de nomes
- Importações organizadas

### 4. **Escalabilidade**

- Fácil adicionar novos módulos
- Estrutura preparada para crescimento
- Padrão profissional

## 📋 Mapeamento: Antigo → Novo

### Arquivos Movidos e Reorganizados

| Arquivo Antigo                | Novo Local                     | Responsabilidade |
| ----------------------------- | ------------------------------ | ---------------- |
| `core.py`                     | `src/core/state.py`            | Estado global    |
| `hotkeymgr.py`                | `src/core/hotkey_manager.py`   | Hotkeys          |
| `logger.py`                   | `src/utils/logger.py`          | Logging          |
| `config.py`                   | `src/utils/config.py`          | Configurações    |
| `resource_loader.py`          | `src/utils/resource_loader.py` | Recursos         |
| `utils.py`                    | `src/utils/helpers.py`         | Helpers          |
| `automation.py`               | `src/automation/engine.py`     | Motor            |
| `routines.py`                 | `src/automation/routines.py`   | Rotinas          |
| `gui_controller.py`           | `src/gui/controller.py`        | Controlador      |
| `FarmScriptGUI_Refactored.py` | `main.py`                      | Entrada          |

### Arquivos Mantidos na Raiz

- `constants.py` - Usado por múltiplos módulos
- `main.py` - Ponto de entrada
- `start.cmd` - Inicializador
- `requirements.txt` - Dependências
- `game_area_config.json` - Configuração

## 🚀 Como Usar

### Inicialização Simples

```bash
start.cmd
```

### Ou Manual

```bash
python main.py
```

## 📦 Importações Atualizadas

### Antes

```python
from logger import logger
from config import game_config
import core
```

### Agora

```python
from src.utils import logger, game_config
from src.core import globalState
```

## 🔄 Compatibilidade

A nova estrutura **mantém compatibilidade** com:

- ✅ Imagens de recursos existentes
- ✅ Configurações de calibração
- ✅ Todas as funcionalidades

## 🧪 Testabilidade

Cada pacote pode ser testado independentemente:

```python
# Testar utils
from src.utils import logger
logger.info("Teste")

# Testar automation
from src.automation import routines
routines.advanced_mining_actions()

# Testar core
from src.core import globalState
print(globalState.selectedJob)
```

## 📈 Vantagens Técnicas

### Organização Modular

- Cada pasta tem um propósito específico
- Imports claros e organizados
- Namespace bem definido

### Manutenção

- Mudanças isoladas por módulo
- Fácil localizar código
- Reduz acoplamento

### Colaboração

- Estrutura padrão da indústria
- Fácil para novos desenvolvedores
- Documentação clara

## 🛠️ Desenvolvimento Futuro

### Fácil Adicionar

- Novos tipos de automação em `src/automation/`
- Novos utilitários em `src/utils/`
- Novas interfaces em `src/gui/`

### Extensibilidade

- Plugins podem ser adicionados como subpastas
- Testes unitários em pasta separada
- Documentação organizada em `docs/`

---

**Versão**: 0.3.0  
**Estrutura**: Organizada em pastas  
**Status**: Pronto para produção ✅
