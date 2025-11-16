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
                    resources.append(resource_name)
        except Exception as e:
            print(f"Erro ao listar recursos: {e}")
        
        return sorted(resources)
    
    @staticmethod
    def get_resource_image_path(job, resource_name, subcategory=""):
        if job not in ResourceLoader.PATH_MAP:
            return None
        
        folder = ResourceLoader.PATH_MAP[job]
        suffix = f"-{subcategory}" if subcategory else ""
        img_path = os.path.join(folder, resource_name.replace(" ", "-") + suffix + ".png")
        return img_path

resource_loader = ResourceLoader()
