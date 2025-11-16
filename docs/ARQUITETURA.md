# Arquitetura do Wakfu FarmScript Refatorado

## 📐 Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                    FarmScriptGUI_Refactored.py              │
│                    (Interface do Usuário)                    │
│  - Widgets Tkinter                                           │
│  - Eventos de UI                                             │
│  - Exibição de status                                        │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   │ usa
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                    gui_controller.py                         │
│                    (Controlador)                             │
│  - Validações                                                │
│  - Orquestração                                              │
│  - Gerenciamento de estado                                   │
└──────┬──────────┬──────────┬───────────┬───────────────────┘
       │          │          │           │
       │          │          │           │
       ▼          ▼          ▼           ▼
   ┌────────┐ ┌─────────┐ ┌──────┐  ┌──────────┐
   │logger.py│ │resource_│ │auto- │  │  core.py │
   │         │ │loader.py│ │mation│  │          │
   └────────┘ └─────────┘ │.py   │  └──────────┘
                           └──┬───┘
                              │
                              │ usa
                              ▼
                     ┌─────────────────┐
                     │  routines.py    │
                     │  (Colheita)     │
                     └────────┬────────┘
                              │
                              │ usa
                              ▼
                     ┌─────────────────┐
                     │    utils.py     │
                     │  (Utilitários)  │
                     └────────┬────────┘
                              │
                              │ usa
                              ▼
                     ┌─────────────────┐
                     │   config.py     │
                     │ (Configurações) │
                     └─────────────────┘
```

## 🎯 Responsabilidades dos Módulos

### 🖼️ Camada de Apresentação

#### `FarmScriptGUI_Refactored.py`
**Responsabilidade**: Interface visual
- Criação de widgets
- Bindings de eventos
- Atualização visual de status
- **NÃO** contém lógica de negócio

### 🎮 Camada de Controle

#### `gui_controller.py`
**Responsabilidade**: Orquestração
- Validação de inputs
- Coordenação entre módulos
- Gerenciamento de estado global
- Comunicação com automação

### ⚙️ Camada de Negócio

#### `automation.py`
**Responsabilidade**: Motor de automação
- Ciclo de colheita
- Gerenciamento de estado (ativo/inativo)
- Coordenação de tempo (delays)
- Execução de routines

#### `routines.py`
**Responsabilidade**: Lógica de colheita
- Detecção de recursos na tela
- Decisões de colheita
- Execução de ações específicas por profissão

### 🔧 Camada de Utilidades

#### `utils.py`
**Responsabilidade**: Funções auxiliares
- Cálculo de pontos mais próximos
- Movimentação e cliques
- Busca de ícones
- Funções genéricas reutilizáveis

#### `logger.py`
**Responsabilidade**: Sistema de logs
- Formatação de mensagens
- Timestamp automático
- Níveis de severidade
- Output estruturado

#### `resource_loader.py`
**Responsabilidade**: Carregamento de recursos
- Leitura dinâmica de pastas
- Mapeamento de profissões
- Paths de imagens

#### `config.py`
**Responsabilidade**: Configurações
- Carregamento de config JSON
- Dimensões do jogo
- Fallbacks seguros

### 🏗️ Camada Base

#### `constants.py`
**Responsabilidade**: Constantes
- Jobs, zonas, recursos
- Paths de arquivos
- Ícones de ações

#### `core.py`
**Responsabilidade**: Estado global (legado)
- GlobalState
- HotkeyManager integration

#### `hotkeymgr.py`
**Responsabilidade**: Gerenciamento de hotkeys (legado)
- Listener de teclado
- Bindings de teclas

## 🔄 Fluxo de Dados

### Inicialização
```
Usuario → GUI → Controller → Validação → Configuração
```

### Execução
```
Hotkey Pressionada → Toggle Automação → Loop de Colheita
                                              ↓
                                         Busca Recurso
                                              ↓
                                         Executa Routine
                                              ↓
                                          Aguarda Delay
                                              ↓
                                         Volta ao Loop
```

### Log de Feedback
```
Ação → Logger → Console com Timestamp
```

## 📦 Dependências entre Módulos

```
FarmScriptGUI_Refactored.py
  └── gui_controller.py
       ├── logger.py
       ├── resource_loader.py
       │    └── constants.py
       ├── automation.py
       │    ├── logger.py
       │    ├── resource_loader.py
       │    └── routines.py
       │         ├── utils.py
       │         │    ├── config.py
       │         │    ├── logger.py
       │         │    └── constants.py
       │         ├── logger.py
       │         └── constants.py
       └── core.py
            └── hotkeymgr.py
```

## 🎨 Padrões de Design Aplicados

### 1. **MVC (Model-View-Controller)**
- **View**: FarmScriptGUI_Refactored.py
- **Controller**: gui_controller.py
- **Model**: core.py, automation.py

### 2. **Singleton**
- HotkeyManager
- HotkeyListener
- Instâncias globais (logger, resource_loader, etc.)

### 3. **Facade**
- gui_controller.py esconde complexidade dos módulos internos
- utils.py simplifica operações complexas

### 4. **Strategy**
- routines.py: diferentes estratégias por profissão
- Seleção dinâmica de ícones por recurso

### 5. **Dependency Injection**
- automation_engine recebe configurações
- Módulos independentes facilmente testáveis

## 🔐 Princípios SOLID

### Single Responsibility (SRP)
✅ Cada módulo tem uma única responsabilidade clara

### Open/Closed (OCP)
✅ Fácil adicionar novas profissões sem modificar código existente

### Liskov Substitution (LSP)
✅ Módulos podem ser substituídos por versões melhoradas

### Interface Segregation (ISP)
✅ Interfaces mínimas entre módulos

### Dependency Inversion (DIP)
✅ Dependências em abstrações (logger, resource_loader)

## 📈 Vantagens da Arquitetura

### Testabilidade
- Cada módulo pode ser testado isoladamente
- Mocks fáceis de criar

### Manutenibilidade
- Mudanças localizadas em módulos específicos
- Fácil encontrar código relacionado

### Escalabilidade
- Novos recursos sem afetar existentes
- Estrutura preparada para crescimento

### Legibilidade
- Código organizado logicamente
- Responsabilidades claras

---

**Conclusão**: Arquitetura modular, testável e escalável seguindo melhores práticas de engenharia de software.
