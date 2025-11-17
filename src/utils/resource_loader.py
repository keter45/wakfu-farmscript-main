"""
Gerenciador de recursos - carrega recursos dinamicamente das pastas
"""
import os
import constants as const

class ResourceLoader:
    PATH_MAP = {
        const.JOB_FARMER: const.FARMER_RES_PATH,
        const.JOB_MINER: const.MINER_RES_PATH,
        const.JOB_HERBALIST: const.HERBALIST_RES_PATH,
        const.JOB_LUMBERJACK: const.LUMBERJACK_RES_PATH,
    }
    
    @staticmethod
    def get_resources_for_job(job):
        # Se for Farmer, usar lista com níveis
        if job == const.JOB_FARMER:
            resources_with_status = []
            for level, name in const.FARMER_RESOURCES:
                # Verificar se existe imagem
                folder = ResourceLoader.PATH_MAP.get(job, "")
                img_path = os.path.join(folder, name.replace(" ", "-") + ".png")
                seed_path = os.path.join(folder, name.replace(" ", "-") + "-seed.png")
                
                # Marcar com ✓ se existir, ✗ se não existir
                if os.path.exists(img_path) or os.path.exists(seed_path):
                    status = "✓"
                else:
                    status = "✗"
                
                resources_with_status.append(f"{level} - {name} {status}")
            return resources_with_status
        
        if job not in ResourceLoader.PATH_MAP:
            return []
        
        folder = ResourceLoader.PATH_MAP[job]
        if not os.path.exists(folder):
            return []
        
        resources = []
        try:
            for file in os.listdir(folder):
                if file.endswith('.png') and not file.endswith('-seed.png') and not file.endswith('-mature.png'):
                    resource_name = file[:-4].replace('-', ' ')
                    resources.append(f"{resource_name} ✓")
        except Exception as e:
            print(f"Erro ao listar recursos: {e}")
        
        return sorted(resources)
    
    @staticmethod
    def get_resource_image_path(job, resource_name, subcategory=""):
        # Remover status ✓ ou ✗ se presente
        if " ✓" in resource_name:
            resource_name = resource_name.replace(" ✓", "")
        if " ✗" in resource_name:
            resource_name = resource_name.replace(" ✗", "")
        
        # Se vier com formato "lvl - nome", extrair apenas o nome
        if " - " in resource_name:
            resource_name = resource_name.split(" - ", 1)[1]
        
        if job not in ResourceLoader.PATH_MAP:
            return None
        
        folder = ResourceLoader.PATH_MAP[job]
        suffix = f"-{subcategory}" if subcategory else ""
        img_path = os.path.join(folder, resource_name.replace(" ", "-") + suffix + ".png")
        return img_path

resource_loader = ResourceLoader()
