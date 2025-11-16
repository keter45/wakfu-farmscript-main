import tkinter as tk
from tkinter import ttk, messagebox
import sys, os, pyautogui as auto
from PIL import ImageGrab, Image, ImageTk
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import constants as const

RESOURCES_MAP = {
    const.JOB_MINER: {
        const.ZONE_ASTRUB: const.ZONE_RESOURCES_MINER_ASTRUB,
        const.ZONE_WILD_ESTATE: const.ZONE_RESOURCES_MINER_WILDESTATE,
        const.ZONE_BRAKMAR: const.ZONE_RESOURCES_MINER_BRAKMAR,
        const.ZONE_BONTA: const.ZONE_RESOURCES_MINER_BONTA,
    },
    const.JOB_FARMER: {
        const.ZONE_ASTRUB: const.ZONE_RESOURCES_FARMER_ASTRUB,
        const.ZONE_AMAKNA: const.ZONE_RESOURCES_FARMER_AMAKNA,
        const.ZONE_SUFOKIA: const.ZONE_RESOURCES_FARMER_SUFOKIA,
    },
    const.JOB_HERBALIST: {
        const.ZONE_ASTRUB: const.ZONE_RESOURCES_HERBALIST_ASTRUB,
        const.ZONE_AMAKNA: const.ZONE_RESOURCES_HERBALIST_AMAKNA,
        const.ZONE_WILD_ESTATE: const.ZONE_RESOURCES_HERBALIST_WILDESTATE,
        const.ZONE_SUFOKIA: const.ZONE_RESOURCES_HERBALIST_SUFOKIA,
    },
    const.JOB_LUMBERJACK: {
        const.ZONE_ASTRUB: const.ZONE_RESOURCES_LUMBERJACK_ASTRUB,
        const.ZONE_AMAKNA: const.ZONE_RESOURCES_LUMBERJACK_AMAKNA,
        const.ZONE_SUFOKIA: const.ZONE_RESOURCES_LUMBERJACK_SUFOKIA,
    },
}

def get_clipboard_image():
    """Pega imagem da area de transferencia (Windows)"""
    try:
        ps_cmd = """
        [void][System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms')
        $img = [System.Windows.Forms.Clipboard]::GetImage()
        if ($img -ne $null) {
            $img.Save($env:TEMP + '\\clipboard_temp.png')
            Write-Output 'success'
        } else {
            Write-Output 'empty'
        }
        """
        result = subprocess.run(['powershell', '-Command', ps_cmd], capture_output=True, text=True)
        
        if 'success' in result.stdout:
            temp_path = os.path.join(os.environ['TEMP'], 'clipboard_temp.png')
            if os.path.exists(temp_path):
                img = Image.open(temp_path)
                img_copy = img.copy()
                return img_copy
        return None
    except Exception as e:
        print(f"Erro ao pegar imagem: {e}")
        return None

class ScreenCapture:
    def __init__(self, parent):
        self.parent = parent
        self.captured = None
        
    def start(self):
        self.parent.withdraw()
        
        cap_win = tk.Toplevel(self.parent)
        cap_win.title("Colar Imagem")
        cap_win.geometry("500x300")
        cap_win.attributes('-topmost', True)
        
        main = ttk.Frame(cap_win, padding="20")
        main.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main, text="INSTRUÇÕES DE CAPTURA", font=("Arial", 12, "bold")).pack(pady=10)
        ttk.Label(main, text="1. Copie a imagem do recurso (Ctrl+C no jogo)").pack(pady=5)
        ttk.Label(main, text="2. Pressione Ctrl+V para colar aqui").pack(pady=5)
        ttk.Label(main, text="3. Ou pressione ESC para cancelar").pack(pady=5)
        
        self.info_label = ttk.Label(main, text="Aguardando imagem...", foreground='blue')
        self.info_label.pack(pady=20)
        
        self.cap_win = cap_win
        cap_win.bind('<Control-v>', self.on_paste)
        cap_win.bind('<Escape>', self.on_esc)
        cap_win.focus()
        
    def on_paste(self, event=None):
        """Recebe imagem do Ctrl+V"""
        img = get_clipboard_image()
        
        if img:
            self.info_label.config(text="✓ Imagem recebida!", foreground='green')
            self.cap_win.after(500, lambda: self.show_preview(img))
        else:
            self.info_label.config(text="✗ Nenhuma imagem na área de transferência!", foreground='red')
            
    def on_esc(self, event=None):
        """Cancela captura"""
        self.cap_win.destroy()
        self.parent.deiconify()
        
    def show_preview(self, img):
        """Mostra preview da imagem"""
        prev_win = tk.Toplevel(self.parent)
        prev_win.title("Preview")
        prev_win.geometry("400x400")
        
        main = ttk.Frame(prev_win, padding="10")
        main.pack(fill=tk.BOTH, expand=True)
        
        img_display = img.copy()
        img_display.thumbnail((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img_display)
        lbl = ttk.Label(main, image=photo)
        lbl.image = photo
        lbl.pack(pady=10)
        
        ttk.Label(main, text=f"Tamanho: {img.size[0]}x{img.size[1]}px", foreground='gray').pack()
        
        btn_frame = ttk.Frame(main)
        btn_frame.pack(pady=10)
        
        def confirm():
            self.captured = img
            prev_win.destroy()
            self.cap_win.destroy()
            self.parent.deiconify()
            
        def recapture():
            prev_win.destroy()
            
        ttk.Button(btn_frame, text="Confirmar", command=confirm).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Recapturar", command=recapture).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Cancelar", command=lambda: [prev_win.destroy(), self.cap_win.destroy(), self.parent.deiconify()]).pack(side=tk.LEFT, padx=5)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Calibrador - Copiar e Colar")
        self.root.geometry("700x550")
        self.root.bind('<Control-v>', self.on_ctrl_v)
        
        self.selected_job = None
        self.selected_resource = None
        self.new_image = None
        self.old_image = None
        self.old_image_tk = None
        self.new_image_tk = None
        
        self.create_main_ui()
        
    def create_main_ui(self):
        """Cria interface principal"""
        main = ttk.Frame(self.root, padding="10")
        main.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main, text="Calibrador de Imagens - Ctrl+V", font=("Arial", 12, "bold")).pack(pady=10)
        
        sel_frame = ttk.LabelFrame(main, text="Selecao", padding="10")
        sel_frame.pack(fill=tk.BOTH, pady=10)
        
        ttk.Label(sel_frame, text="Job:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.job_var = tk.StringVar()
        job_cb = ttk.Combobox(sel_frame, textvariable=self.job_var, state='readonly', width=40)
        job_cb['values'] = (const.JOB_FARMER, const.JOB_MINER, const.JOB_HERBALIST, const.JOB_LUMBERJACK)
        job_cb.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        job_cb.bind("<<ComboboxSelected>>", self.on_job_change)
        
        ttk.Label(sel_frame, text="Recurso:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.res_var = tk.StringVar()
        self.res_cb = ttk.Combobox(sel_frame, textvariable=self.res_var, state='readonly', width=40)
        self.res_cb.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        # Opcao para recurso customizado
        ttk.Label(sel_frame, text="Ou novo nome:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.custom_res_var = tk.StringVar()
        custom_entry = ttk.Entry(sel_frame, textvariable=self.custom_res_var, width=42)
        custom_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        info_frame = ttk.LabelFrame(main, text="Como Usar", padding="10")
        info_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        ttk.Label(info_frame, text="1. Selecione Job e Recurso (ou digite novo nome)").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text="2. No jogo, copie a tela (Ctrl+C)").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text="3. Aqui, pressione Ctrl+V para colar").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text="4. Compare a imagem e escolha salvar ou recolar").pack(anchor=tk.W, pady=2)
        ttk.Label(info_frame, text="5. Pressione Ctrl+V novamente para adicionar nova imagem").pack(anchor=tk.W, pady=2)
        
        self.status_label = ttk.Label(main, text="Pressione Ctrl+V para colar uma imagem...", foreground='blue')
        self.status_label.pack(pady=10)
        
    def on_job_change(self, e):
        job = self.job_var.get()
        if job in RESOURCES_MAP:
            all_res = []
            for zone_res in RESOURCES_MAP[job].values():
                all_res.extend(zone_res)
            self.res_cb['values'] = sorted(list(set(all_res)))
            self.res_var.set('')
            self.selected_job = job
        
    def on_ctrl_v(self, event):
        job = self.job_var.get()
        resource = self.res_var.get() or self.custom_res_var.get()
        
        if not job or not resource:
            messagebox.showerror("Erro", "Selecione Job e Recurso (ou digite novo nome)!")
            return
        
        img = get_clipboard_image()
        if not img:
            messagebox.showerror("Erro", "Nenhuma imagem na area de transferencia!")
            return
        
        self.new_image = img
        self.selected_job = job
        self.selected_resource = resource
        
        path_map = {
            const.JOB_FARMER: const.FARMER_RES_PATH,
            const.JOB_MINER: const.MINER_RES_PATH,
            const.JOB_HERBALIST: const.HERBALIST_RES_PATH,
            const.JOB_LUMBERJACK: const.LUMBERJACK_RES_PATH,
        }
        folder = path_map[self.selected_job]
        filepath = os.path.join(folder, self.selected_resource.replace(" ", "-") + ".png")
        
        self.old_image = None
        if os.path.exists(filepath):
            try:
                self.old_image = Image.open(filepath)
            except:
                pass
        
        self.show_comparison()
        
    def show_comparison(self):
        comp_win = tk.Toplevel(self.root)
        comp_win.title("Comparar Imagens")
        comp_win.geometry("900x550")
        comp_win.attributes('-topmost', True)
        
        main = ttk.Frame(comp_win, padding="10")
        main.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main, text=f"Imagem: {self.selected_resource}", font=("Arial", 11, "bold")).pack(pady=10)
        
        img_frame = ttk.Frame(main)
        img_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        old_frame = ttk.LabelFrame(img_frame, text="IMAGEM ANTIGA", padding="5")
        old_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        if self.old_image:
            old_display = self.old_image.copy()
            old_display.thumbnail((350, 350), Image.Resampling.LANCZOS)
            self.old_image_tk = ImageTk.PhotoImage(old_display)
            old_lbl = ttk.Label(old_frame, image=self.old_image_tk, background='lightgray')
            old_lbl.pack(fill=tk.BOTH, expand=True)
            ttk.Label(old_frame, text=f"{self.old_image.size[0]}x{self.old_image.size[1]}px", foreground='gray').pack(pady=5)
        else:
            ttk.Label(old_frame, text="(Nenhuma imagem anterior)", foreground='gray', font=("Arial", 10)).pack(pady=100)
        
        new_frame = ttk.LabelFrame(img_frame, text="IMAGEM NOVA", padding="5")
        new_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        new_display = self.new_image.copy()
        new_display.thumbnail((350, 350), Image.Resampling.LANCZOS)
        self.new_image_tk = ImageTk.PhotoImage(new_display)
        new_lbl = ttk.Label(new_frame, image=self.new_image_tk, background='lightgray')
        new_lbl.pack(fill=tk.BOTH, expand=True)
        ttk.Label(new_frame, text=f"{self.new_image.size[0]}x{self.new_image.size[1]}px", foreground='gray').pack(pady=5)
        
        btn_frame = ttk.Frame(main)
        btn_frame.pack(fill=tk.X, pady=10)
        
        def salvar():
            path_map = {
                const.JOB_FARMER: const.FARMER_RES_PATH,
                const.JOB_MINER: const.MINER_RES_PATH,
                const.JOB_HERBALIST: const.HERBALIST_RES_PATH,
                const.JOB_LUMBERJACK: const.LUMBERJACK_RES_PATH,
            }
            folder = path_map[self.selected_job]
            filepath = os.path.join(folder, self.selected_resource.replace(" ", "-") + ".png")
            
            try:
                self.new_image.save(filepath)
                comp_win.destroy()
                self.status_label.config(text=f"✓ Salvo: {self.selected_resource}", foreground='green')
                messagebox.showinfo("Sucesso", f"Imagem salva:\n{filepath}")
                self.new_image = None
                self.custom_res_var.set('')
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar:\n{e}")
        
        def recolar():
            comp_win.destroy()
            self.status_label.config(text="Pressione Ctrl+V novamente...", foreground='blue')
        
        def descartar():
            comp_win.destroy()
            self.new_image = None
            self.status_label.config(text="Descartado. Pressione Ctrl+V novamente...", foreground='orange')
        
        ttk.Button(btn_frame, text="Salvar", command=salvar, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Recolar (Ctrl+V)", command=recolar, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Descartar", command=descartar, width=15).pack(side=tk.LEFT, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
