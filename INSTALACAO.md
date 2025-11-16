# 🚀 Wakfu FarmScript - Instalação

## ⚙️ Requisitos

- **Windows 7+** (ou Linux/Mac com Python 3.9+)
- **Python 3.9+** (Recomendado Python 3.14)
- Conexão com Internet para baixar dependências

## 📥 Instalação Rápida

### Opção 1: Instalador em Python (Recomendado)

```bash
python instalar.py
```

- Menu interativo
- Verifica versão do Python
- Instala todas as dependências automaticamente

### Opção 2: Instalador em Batch (Windows)

```bash
INSTALAR.cmd
```

- Simples e direto
- Só clique e aguarde

### Opção 3: Manual

```bash
python -m pip install -r requirements.txt
```

## 🎮 Como Usar

1. **Inicie o programa:**

   ```bash
   python FarmScriptGUI_Tkinter.py
   ```

2. **Configure a automação:**

   - Selecione a **Profissão** (padrão: Farmer)
   - Selecione a **Zona**
   - Selecione o **Recurso** a colher
   - Selecione a **Hotkey** (padrão: F2)
   - Ajuste o **Delay** (padrão: 90s)

3. **Calibre as imagens:**

   - Clique em **📷 Calibrar**
   - Use `Ctrl+V` para colar screenshots do jogo
   - Salve as imagens dos recursos

4. **Inicie a automação:**
   - Clique em **Start**
   - Pressione a hotkey no jogo para ativar
   - Pressione novamente para desativar

## 📋 Estrutura de Pastas

```
wakfu-farmscript/
├── FarmScriptGUI_Tkinter.py    # Menu principal
├── calibrator.py                # Ferramenta de calibração
├── core.py                       # Lógica principal
├── routines.py                   # Rotinas de automação
├── constants.py                  # Constantes
├── instalar.py                   # Instalador Python
├── INSTALAR.cmd                  # Instalador Batch
├── img/                          # Imagens dos recursos
│   ├── farmer_res/
│   ├── miner_res/
│   ├── herbalist_res/
│   └── lumberjack_res/
└── requirements.txt              # Dependências

```

## 🔧 Dependências Principais

- **PyAutoGUI** - Controle do mouse e teclado
- **PIL/Pillow** - Processamento de imagens
- **OpenCV** - Detecção de imagens
- **pynput** - Listener de hotkeys
- **Tkinter** - Interface gráfica (incluído no Python)

## ⚠️ Solução de Problemas

### "Python não foi encontrado"

1. Baixe Python em: https://www.python.org/downloads/
2. **IMPORTANTE:** Marque "Add Python to PATH" na instalação
3. Reinicie o CMD/PowerShell

### "Erro ao instalar dependências"

1. Atualize o pip: `python -m pip install --upgrade pip`
2. Tente novamente: `python instalar.py`
3. Se persistir, instale manualmente: `pip install requirements.txt`

### "Imagem não detectada"

1. Use o **Calibrador** (botão 📷)
2. Capture imagens bem nítidas
3. Verifique a resolução (deve ser igual em todas)

### "Automação não começa"

1. Verifique se a hotkey está configurada
2. Certifique-se que a janela do jogo está focada
3. Verifique os logs no console

## 📞 Suporte

- Verifique o arquivo `CALIBRAÇÃO.md` para detalhes sobre calibração
- Consulte o console para logs e mensagens de erro
- Ajuste o delay se a detecção for lenta

---

**Versão:** 2.0
**Compatível com:** Python 3.9+
**Última atualização:** Novembro 2025
