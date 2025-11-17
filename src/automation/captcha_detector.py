"""
Detector de Captcha do Wakfu
Identifica e resolve o desafio de verificação do jogo
"""
import pyautogui as auto
import time
from src.utils.logger import logger
from src.utils.config import game_config

class CaptchaDetector:
    def __init__(self):
        self.is_active = False
        self.captcha_detected = False
        
        # Padrões conhecidos
        self.cat_pattern = None  # Imagem do gato branco
        self.x_pattern = None     # Padrão do X
        self.empty_pattern = None # Tile vazio
        
        # Posições relativas (serão calibradas)
        self.player_grid_region = None  # Região 1-8 (lado esquerdo)
        self.cat_grid_region = None     # Região com respostas (lado direito)
        
    def detect_captcha_event(self):
        """
        Detecta se o captcha está ativo na tela
        Procura pelo gato branco característico
        """
        try:
            # TODO: Criar imagem de referência do gato
            # cat_location = auto.locateOnScreen('img/captcha/cat.png', confidence=0.75)
            
            # Por enquanto, detecção manual via região específica
            # Verificar se há um padrão de grid característico
            
            logger.debug("Verificando presença de captcha...")
            return False  # Placeholder
            
        except Exception as e:
            logger.error(f"Erro ao detectar captcha: {e}")
            return False
    
    def analyze_cat_grid(self):
        """
        Analisa o grid do lado do gato (direita/baixo)
        Identifica quais tiles têm o padrão correto (não X, não vazio)
        
        Returns:
            list: Índices dos tiles com padrão correto
        """
        pattern_tiles = []
        
        try:
            logger.info("🔍 Analisando grid do gato...")
            
            # TODO: Implementar detecção de cada tile
            # Grid típico seria algo como 3x3 ou similar
            # Para cada posição, verificar:
            # - Se tem X -> ignorar
            # - Se está vazio -> ignorar  
            # - Se tem padrão -> adicionar à lista
            
            # Exemplo de estrutura:
            # for i in range(9):  # Se for grid 3x3
            #     tile_region = self._get_cat_tile_region(i)
            #     if self._has_pattern(tile_region):
            #         pattern_tiles.append(i)
            
            logger.info(f"Tiles com padrão encontrados: {pattern_tiles}")
            return pattern_tiles
            
        except Exception as e:
            logger.error(f"Erro ao analisar grid do gato: {e}")
            return []
    
    def analyze_player_grid(self):
        """
        Analisa o grid do lado do jogador (esquerda/cima)
        Tenta identificar os números 1-8 mesmo com animação
        
        Returns:
            dict: Mapeamento {posição_visual: número}
        """
        number_map = {}
        
        try:
            logger.info("🔍 Analisando grid do jogador...")
            
            # Estratégia: Capturar múltiplos frames e usar OCR ou template matching
            # Como os números estão animados, precisamos:
            # 1. Capturar várias imagens do mesmo tile
            # 2. Comparar com templates dos números 1-8
            # 3. Escolher o match com maior confiança
            
            # TODO: Implementar detecção robusta
            # for position in range(8):
            #     tile_region = self._get_player_tile_region(position)
            #     number = self._identify_number(tile_region)
            #     number_map[position] = number
            
            logger.info(f"Números identificados: {number_map}")
            return number_map
            
        except Exception as e:
            logger.error(f"Erro ao analisar grid do jogador: {e}")
            return {}
    
    def calculate_solution(self, cat_patterns, player_numbers):
        """
        Calcula quais números do grid do jogador correspondem aos padrões do gato
        
        Args:
            cat_patterns: Lista de índices com padrão no grid do gato
            player_numbers: Dict mapeando posição visual -> número
            
        Returns:
            list: Números que devem ser clicados
        """
        try:
            # A lógica depende de como os grids se correspondem
            # Assumindo que a posição no grid do gato mapeia diretamente:
            
            solution = []
            for pattern_pos in cat_patterns:
                # Encontrar qual número está nessa posição
                if pattern_pos in player_numbers:
                    solution.append(player_numbers[pattern_pos])
            
            logger.success(f"✓ Solução calculada: Clicar nos números {solution}")
            return solution
            
        except Exception as e:
            logger.error(f"Erro ao calcular solução: {e}")
            return []
    
    def solve_captcha(self):
        """
        Pipeline completo para resolver o captcha
        """
        try:
            if not self.detect_captcha_event():
                return False
            
            logger.info("="*60)
            logger.info("🎯 CAPTCHA DETECTADO! Iniciando resolução...")
            logger.info("="*60)
            
            # Passo 1: Analisar grid do gato (resposta)
            cat_patterns = self.analyze_cat_grid()
            if not cat_patterns:
                logger.warning("Nenhum padrão encontrado no grid do gato")
                return False
            
            # Passo 2: Analisar grid do jogador (números)
            player_numbers = self.analyze_player_grid()
            if not player_numbers:
                logger.warning("Não foi possível identificar os números")
                return False
            
            # Passo 3: Calcular solução
            solution = self.calculate_solution(cat_patterns, player_numbers)
            if not solution:
                logger.warning("Não foi possível calcular a solução")
                return False
            
            # Passo 4: Executar solução (clicar nos números)
            logger.info(f"📋 LOG SOLUÇÃO: Padrões={cat_patterns}, Números={player_numbers}, Resposta={solution}")
            
            # TODO: Implementar cliques
            # self._click_numbers(solution)
            
            logger.success("✓ Captcha resolvido!")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao resolver captcha: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _get_cat_tile_region(self, index):
        """Retorna região de um tile específico no grid do gato"""
        # TODO: Calcular baseado em calibração
        pass
    
    def _get_player_tile_region(self, index):
        """Retorna região de um tile específico no grid do jogador"""
        # TODO: Calcular baseado em calibração
        pass
    
    def _has_pattern(self, region):
        """Verifica se um tile tem o padrão (não X, não vazio)"""
        # TODO: Implementar detecção
        pass
    
    def _identify_number(self, region):
        """
        Identifica o número em um tile (1-8) usando múltiplos frames de referência
        
        Args:
            region: Tupla (x, y, width, height) da região do tile
            
        Returns:
            int: Número identificado (1-8) ou None se não conseguir
        """
        import os
        import pyautogui as auto
        
        try:
            # Capturar screenshot da região atual
            current_tile = auto.screenshot(region=region)
            
            best_match = None
            best_confidence = 0.0
            
            # Tentar match com cada número (1-8)
            for num in range(1, 9):
                # Verificar se tem pasta com múltiplos frames
                num_folder = f'img/captcha/number_{num}'
                
                if os.path.exists(num_folder):
                    # Usar múltiplos frames
                    frames = [f for f in os.listdir(num_folder) if f.endswith('.png')]
                    
                    for frame_file in frames:
                        frame_path = os.path.join(num_folder, frame_file)
                        try:
                            # Template matching
                            result = auto.locate(frame_path, current_tile, confidence=0.6)
                            if result:
                                confidence = 0.8  # Encontrou match
                                if confidence > best_confidence:
                                    best_confidence = confidence
                                    best_match = num
                        except:
                            continue
                else:
                    # Fallback: tentar arquivo único
                    frame_path = f'img/captcha/number_{num}_best.png'
                    if os.path.exists(frame_path):
                        try:
                            result = auto.locate(frame_path, current_tile, confidence=0.6)
                            if result:
                                confidence = 0.7
                                if confidence > best_confidence:
                                    best_confidence = confidence
                                    best_match = num
                        except:
                            continue
            
            if best_match and best_confidence > 0.6:
                logger.debug(f"Número identificado: {best_match} (confiança: {best_confidence:.2f})")
                return best_match
            else:
                logger.warning(f"Número não identificado (melhor: {best_match}, conf: {best_confidence:.2f})")
                return None
                
        except Exception as e:
            logger.error(f"Erro ao identificar número: {e}")
            return None

captcha_detector = CaptchaDetector()
