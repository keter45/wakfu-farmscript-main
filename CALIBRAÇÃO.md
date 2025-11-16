# 🎮 Wakfu FarmScript - Guia de Calibração

## ⚙️ Calibradores Disponíveis

### 1. **Calibrador de Imagens** (`calibrator.py`)

- Captura screenshots de recursos na sua resolução
- Permite ao script detectar melhor os recursos

**Como usar:**

```bash
python calibrator.py
```

**Passos:**

1. Selecione um Job (Farmer, Miner, etc)
2. Selecione um Recurso
3. Clique em "Capturar Screenshot"
4. Coloque o cursor sobre o recurso (5 segundos)
5. A imagem será salva automaticamente

### 2. **Calibrador de Área do Jogo** (`calibrator_area.py`)

- Define a área exata onde o jogo está rodando
- Especialmente importante para resoluções ultra-wide

**Como usar:**

```bash
python calibrator_area.py
```

**Exemplo para 3440x1440 (ultra-wide):**

- Se o jogo está na **esquerda**:

  - X: 0
  - Y: 0
  - Largura: 1920
  - Altura: 1440

- Se o jogo está no **centro**:

  - X: 760
  - Y: 0
  - Largura: 1920
  - Altura: 1440

- Se o jogo está na **direita**:
  - X: 1520
  - Y: 0
  - Largura: 1920
  - Altura: 1440

## 🚀 Fluxo de Calibração Recomendado

1. **Primeiro:** Rode `calibrator_area.py`

   - Define onde o jogo está na sua tela

2. **Depois:** Rode `calibrator.py`

   - Capture imagens dos recursos

3. **Por fim:** Rode `FarmScriptGUI_Tkinter.py`
   - Configure e teste o script

## 💾 Arquivos de Configuração

- `game_area_config.json` - Configuração de área do jogo (gerado automaticamente)

## 📊 Resolução de Problemas

**Problema:** Mouse não vai para o lugar certo

- **Solução:** Rode `calibrator_area.py` e defina a área correta

**Problema:** Recursos não são detectados

- **Solução:** Rode `calibrator.py` e capture imagens em sua resolução

**Problema:** Detecção muito sensível (clica em coisas erradas)

- **Solução:** Edite `routines.py` e aumente os valores de `confidence` um pouco
