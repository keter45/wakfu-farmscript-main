"""
Sistema de atualização automática do Wakfu FarmScript
Verifica e baixa atualizações do GitHub
"""
import requests
import subprocess
import os
import sys
from src.utils.logger import logger
import constants as const

GITHUB_REPO = "keter45/wakfu-farmscript-main"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
GITHUB_RAW_URL = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main"

class Updater:
    def __init__(self):
        self.current_version = const.VERSION
        self.latest_version = None
        self.update_available = False
        
    def check_for_updates(self):
        """
        Verifica se há atualizações disponíveis no GitHub
        
        Returns:
            tuple: (has_update, latest_version, download_url)
        """
        try:
            logger.info("🔍 Verificando atualizações...")
            
            # Buscar última release do GitHub
            response = requests.get(GITHUB_API_URL, timeout=10)
            
            if response.status_code != 200:
                logger.warning("Não foi possível verificar atualizações")
                return False, None, None
            
            data = response.json()
            self.latest_version = data.get('tag_name', '').replace('v', '')
            
            if not self.latest_version:
                logger.warning("Versão não encontrada no GitHub")
                return False, None, None
            
            # Comparar versões
            if self._is_newer_version(self.latest_version, self.current_version):
                self.update_available = True
                download_url = data.get('zipball_url')
                
                logger.success(f"✨ Nova versão disponível: v{self.latest_version}")
                logger.info(f"   Versão atual: v{self.current_version}")
                
                return True, self.latest_version, download_url
            else:
                logger.success(f"✓ Você está na versão mais recente: v{self.current_version}")
                return False, self.latest_version, None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao verificar atualizações: {e}")
            return False, None, None
        except Exception as e:
            logger.error(f"Erro inesperado: {e}")
            return False, None, None
    
    def _is_newer_version(self, latest, current):
        """
        Compara versões (formato: X.Y.Z)
        
        Returns:
            bool: True se latest > current
        """
        try:
            latest_parts = [int(x) for x in latest.split('.')]
            current_parts = [int(x) for x in current.split('.')]
            
            # Garantir mesmo tamanho
            while len(latest_parts) < 3:
                latest_parts.append(0)
            while len(current_parts) < 3:
                current_parts.append(0)
            
            return latest_parts > current_parts
        except:
            return False
    
    def update_via_git(self):
        """
        Atualiza usando git pull (se for repositório git)
        
        Returns:
            bool: True se atualizou com sucesso
        """
        try:
            # Verificar se é repositório git
            if not os.path.exists('.git'):
                logger.warning("Não é um repositório git. Use atualização manual.")
                return False
            
            logger.info("📥 Baixando atualizações...")
            
            # Verificar mudanças locais
            result = subprocess.run(
                ['git', 'status', '--porcelain'],
                capture_output=True,
                text=True
            )
            
            if result.stdout.strip():
                logger.warning("⚠️  Você tem mudanças locais não commitadas")
                logger.info("As mudanças serão preservadas (stash)")
                
                # Fazer stash das mudanças locais
                subprocess.run(['git', 'stash'], check=True)
            
            # Pull das atualizações
            result = subprocess.run(
                ['git', 'pull', 'origin', 'main'],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                logger.success("✓ Atualização concluída!")
                logger.info("Por favor, reinicie o programa")
                return True
            else:
                logger.error(f"Erro ao atualizar: {result.stderr}")
                return False
                
        except FileNotFoundError:
            logger.error("Git não está instalado")
            logger.info("Baixe em: https://git-scm.com/downloads")
            return False
        except Exception as e:
            logger.error(f"Erro ao atualizar: {e}")
            return False
    
    def get_changelog(self):
        """
        Busca o changelog da última versão
        
        Returns:
            str: Changelog ou None
        """
        try:
            response = requests.get(GITHUB_API_URL, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('body', 'Sem informações de changelog')
            return None
        except:
            return None
    
    def download_and_install_manual(self, download_url):
        """
        Abre o navegador para download manual
        
        Args:
            download_url: URL para download
        """
        import webbrowser
        
        logger.info("🌐 Abrindo navegador para download manual...")
        webbrowser.open(f"https://github.com/{GITHUB_REPO}/releases/latest")
        
        logger.info("\n📋 Instruções para atualização manual:")
        logger.info("1. Baixe o arquivo ZIP da última versão")
        logger.info("2. Extraia em uma nova pasta")
        logger.info("3. Copie suas configurações e imagens:")
        logger.info("   - game_area_config.json")
        logger.info("   - captcha_config.json (se existir)")
        logger.info("   - img/ (suas imagens capturadas)")
        logger.info("4. Execute o instalador novamente\n")

updater = Updater()
