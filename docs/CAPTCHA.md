# Sistema de Detecção de Captcha - Wakfu

## 📋 Visão Geral

Este sistema detecta e resolve automaticamente o captcha de verificação do Wakfu que aparece periodicamente.

### Como Funciona

O captcha consiste em:

- **Grid do Jogador** (esquerda/cima): 8 posições numeradas de 1 a 8
- **Grid do Gato** (direita/baixo): Tiles com padrões (X, vazio, ou padrão correto)
- **Objetivo**: Clicar nos números do grid do jogador que correspondem às posições com padrão no grid do gato

## 🎯 Status de Implementação

### ✅ Implementado

- [x] Estrutura base do detector (`captcha_detector.py`)
- [x] Calibrador de captcha (`calibrator_captcha.py`)
- [x] Integração com motor de automação
- [x] Sistema de logging de padrões detectados

### 🚧 Em Desenvolvimento

- [ ] Detecção automática do gato (template matching)
- [ ] Reconhecimento de padrões de tiles (X, vazio, padrão)
- [ ] Identificação de números 1-8 com animação
- [ ] Cálculo e execução da solução

## 🛠️ Como Calibrar

1. **Acione o captcha no jogo** (espere aparecer naturalmente)

2. **Execute o calibrador**:

   ```bash
   python calibrator_captcha.py
   ```

3. **Siga o menu**:

   - Opção 1: Capturar imagem do gato branco
   - Opção 2: Capturar padrões de tiles (X, vazio, padrões)
   - Opção 3: Capturar números 1-8
   - Opção 4: Calibrar regiões dos grids
   - Opção 5: Fazer tudo automaticamente

4. **Arquivos gerados**:
   - `img/captcha/cat.png` - Referência do gato
   - `img/captcha/x_pattern.png` - Padrão X
   - `img/captcha/empty_pattern.png` - Tile vazio
   - `img/captcha/pattern1.png` - Padrão correto (bolhas)
   - `img/captcha/number_1.png` até `number_8.png` - Números
   - `captcha_config.json` - Regiões dos grids

## 🔍 Como Funciona a Detecção

### 1. Detecção do Evento

```python
captcha_detector.detect_captcha_event()
```

- Procura pelo gato branco na tela
- Verifica padrão de grid característico

### 2. Análise do Grid do Gato

```python
captcha_detector.analyze_cat_grid()
```

- Identifica cada tile do grid
- Classifica como: X, vazio, ou padrão
- Retorna lista de posições com padrão correto

### 3. Análise do Grid do Jogador

```python
captcha_detector.analyze_player_grid()
```

- Captura múltiplos frames de cada posição
- Usa template matching para identificar números 1-8
- Retorna mapeamento {posição: número}

### 4. Cálculo da Solução

```python
captcha_detector.calculate_solution(cat_patterns, player_numbers)
```

- Mapeia posições com padrão para números correspondentes
- Retorna lista de números a clicar

### 5. Execução

- Clica nos números calculados
- Log completo da solução

## 📊 Exemplo de Log

```
[12:34:56] ⚠️  CAPTCHA DETECTADO! Pausando automação...
[12:34:56] 🔍 Analisando grid do gato...
[12:34:57] Tiles com padrão encontrados: [0, 4, 7]
[12:34:57] 🔍 Analisando grid do jogador...
[12:34:58] Números identificados: {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8}
[12:34:58] ✓ Solução calculada: Clicar nos números [1, 5, 8]
[12:34:58] 📋 LOG SOLUÇÃO: Padrões=[0, 4, 7], Números={...}, Resposta=[1, 5, 8]
[12:34:59] ✓ Captcha resolvido!
```

## 🎮 Integração com Automação

O detector está integrado ao motor principal:

- Verifica captcha a cada ciclo de colheita
- Pausa automação quando detectado
- Resolve e retoma automação

## ⚙️ Próximos Passos

1. **Calibrar com captcha real**: Execute `calibrator_captcha.py`
2. **Testar detecção**: Implementar `detect_captcha_event()`
3. **Treinar reconhecimento**: Capturar múltiplas variações de números
4. **Ajustar confiança**: Tunar thresholds de detecção
5. **Teste completo**: Validar em condições reais

## 🐛 Troubleshooting

### Captcha não detectado

- Recalibrar imagem do gato: `calibrator_captcha.py` → Opção 1
- Verificar confiança de detecção (padrão: 0.75)

### Números não reconhecidos

- Capturar mais amostras em diferentes frames da animação
- Aumentar número de tentativas de matching

### Solução incorreta

- Verificar mapeamento de posições grid gato ↔ grid jogador
- Recalibrar regiões dos grids

## 📝 Notas Técnicas

- **Animação de números**: Sistema captura múltiplos frames
- **Posições aleatórias**: Grid é recalibrado a cada detecção
- **Fallback**: Se confiança baixa, sistema tenta eliminação por tentativa
