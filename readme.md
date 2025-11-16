# 🎮 Wakfu FarmScript v0.3.0

Bot de automação para farming no jogo Wakfu - **Versão Organizada e Refatorada**

## ✨ Novidades da v0.3.0

- 📁 **Código organizado em pastas** - Estrutura profissional e modular
- 🔧 **Separação de responsabilidades** - Cada módulo com função específica
- 📊 **Sistema de logging melhorado** - Feedback detalhado com timestamp
- 🎯 **Código reduzido em 40%** - Eliminação de redundâncias
- 📚 **Documentação completa** - Guias de arquitetura e migração

## 🚀 Início Rápido

### Instalação

1. Clone ou baixe o projeto
2. Instale as dependências:

```bash
INSTALAR.cmd
```

### Execução

```bash
start.cmd
```

Ou manualmente:

```bash
python main.py
```

## 📂 Estrutura Organizada e Limpa

```
wakfu-farmscript/
├── src/                # Código fonte modular
│   ├── core/           # Estado global e hotkeys
│   ├── gui/            # Interface gráfica
│   ├── automation/     # Motor de automação e routines
│   └── utils/          # Utilitários (logger, config, helpers)
├── legacy/             # Versões antigas (referência)
├── docs/               # Documentação completa
├── img/                # Recursos de imagem
├── main.py             # Ponto de entrada
├── start.cmd           # Inicializador
└── constants.py        # Constantes compartilhadas
```

📖 [Ver estrutura detalhada](docs/ESTRUTURA_PASTAS.md)  
📦 [Arquivos antigos](legacy/README.md) (opcional)

## 🎯 Funcionalidades

### Profissões Suportadas

- ⛏️ **Minerador** (Miner) - 95% precisão
- 🌾 **Fazendeiro** (Farmer) - 70% precisão
- 🌿 **Herborista** (Herbalist) - 65% precisão
- 🪓 **Lenhador** (Lumberjack) - 85% precisão
- 🎣 **Pescador** (Fisherman) - 50% precisão
- 🪤 **Caçador** (Trapper) - 100% (cliques automáticos)

### Recursos Principais

- ✅ Detecção automática de recursos na tela
- ✅ Seleção inteligente do ponto mais próximo
- ✅ Sistema de sementes e recursos maduros
- ✅ Delay configurável entre colheitas
- ✅ Toggle via hotkey (F1-F7)
- ✅ Calibrador de recursos integrado

## 📖 Como Funciona

O script usa **detecção de objetos** ([Object Detection](https://www.mathworks.com/discovery/object-detection.html)):

1. Captura screenshot da tela
2. Procura pela imagem do recurso
3. Clica no recurso detectado
4. Clica no ícone de colheita
5. Aguarda delay configurável
6. Repete o processo

**Simples, eficiente e semi-automático!**

## 🎮 Como Usar

1. **Selecione a profissão** e zona desejada
2. **Escolha o recurso** que deseja coletar
3. **Configure a hotkey** (F1-F7)
4. **Ajuste o delay** após colheita (1-300s)
5. **Clique em Start**
6. **Pressione a hotkey no jogo** para ATIVAR/DESATIVAR

## 🔧 Calibração de Recursos

Para adicionar novos recursos:

1. Clique em **📷 Calibrar**
2. Selecione a profissão
3. Capture a imagem do recurso na tela
4. O recurso aparecerá automaticamente na lista

## 📊 Sistema de Logs Melhorado

```
[14:32:15.123] INFO: Profissão selecionada: Farmer
[14:32:16.456] SEARCH: Procurando recurso...
[14:32:17.789] SUCCESS: Colheita concluída!
[14:32:20.012] INFO: Aguardando: 12s restantes
```

**Níveis de log disponíveis:**

- `INFO` - Informações gerais
- `SUCCESS` - Operações bem-sucedidas
- `WARNING` - Avisos importantes
- `ERROR` - Erros críticos
- `DEBUG` - Informações de depuração
- `SEARCH` - Busca de recursos
- `ACTION` - Ações executadas

## 📚 Documentação Completa

- 📖 [Estrutura de Pastas](docs/ESTRUTURA_PASTAS.md) - Organização do código
- 🏗️ [Arquitetura](docs/ARQUITETURA.md) - Diagrama e padrões aplicados
- 🔄 [Refatoração](docs/REFATORACAO.md) - Melhorias implementadas
- 📋 [Migração](docs/MIGRACAO.md) - Guia de migração de versões

## 🔄 Mudanças da v0.2 para v0.3

### ✅ Melhorias Implementadas

- Código organizado em pastas modulares `src/`
- Imports limpos e organizados
- Sistema de logging profissional
- Separação clara de responsabilidades
- Documentação expandida e detalhada
- Redução de ~40% no código duplicado

### 🏗️ Nova Arquitetura

- `src/core/` - Estado global e gerenciamento de hotkeys
- `src/gui/` - Interface gráfica e controller
- `src/automation/` - Motor de automação e routines
- `src/utils/` - Ferramentas auxiliares reutilizáveis

### 📦 Compatibilidade Total

- ✅ Mantém todas as funcionalidades anteriores
- ✅ Imagens de recursos existentes funcionam normalmente
- ✅ Configurações preservadas

## 🛠️ Requisitos

- **Python 3.8+**
- **pyautogui** - Automação de mouse/teclado
- **pynput** - Detecção de hotkeys
- **tkinter** - Interface gráfica (geralmente incluído)
- **Pillow** - Processamento de imagens

Instale automaticamente com:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuração Avançada

### Calibração de Área do Jogo

Se o jogo não estiver em tela cheia:

```bash
python calibrator_area.py
```

### Ajuste de Delay

Configure o tempo entre colheitas:

- **Mínimo**: 1 segundo
- **Máximo**: 300 segundos
- **Recomendado**: 10-20 segundos

## 🐛 Solução de Problemas

### Script não inicia

✅ Verifique se Python 3.8+ está instalado  
✅ Execute `INSTALAR.cmd` para instalar dependências  
✅ Verifique se não há erros no console

### Recurso não detectado

✅ Use o calibrador para capturar o recurso novamente  
✅ Certifique-se de que a imagem está na pasta correta  
✅ Ajuste a confiança de detecção se necessário

### Hotkey não responde

✅ Certifique-se de que o status está "Active" (verde)  
✅ Pressione a hotkey configurada para ativar/desativar  
✅ Verifique se outra aplicação não está usando a mesma tecla

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Áreas de interesse:

- 🆕 Novos recursos e profissões
- 🎯 Melhorias na detecção
- ⚡ Otimizações de performance
- 🧪 Testes automatizados
- 📝 Melhorias na documentação

## ⚠️ Aviso Importante

**Este projeto é para fins educacionais.**

Use por sua própria conta e risco. O uso de automação pode violar os termos de serviço do jogo. Não nos responsabilizamos por suspensões ou banimentos.

**Farmscript ≠ Bot AFK**  
Esta ferramenta requer interação do jogador e não foi projetada para farming AFK, que prejudicaria a economia do jogo.

## 📜 Licença

Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

Obrigado a todos que contribuíram e testaram o projeto!

---

**Versão**: 0.3.0  
**Status**: Estável ✅  
**Última Atualização**: Novembro 2025  
**Python**: 3.8+
