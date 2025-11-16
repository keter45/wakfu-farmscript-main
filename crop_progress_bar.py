#!/usr/bin/env python3
"""
Script interativo para fazer crop da barra de progresso
Instruções:
1. Selecione uma imagem capturada
2. Use as setas para ajustar o crop
3. Pressione ENTER para salvar
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ProgressBarCropper:
    def __init__(self, root):
        self.root = root
        self.root.title("Crop da Barra de Progresso")
        self.root.geometry("800x600")
        
        self.image = None
        self.image_tk = None
        self.crop_area = None
        
        self.x = 0
        self.y = 0
        self.width = 500
        self.height = 50
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame superior
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(top_frame, text="Selecionar Imagem", command=self.load_image).pack(side=tk.LEFT, padx=5)
        tk.Button(top_frame, text="Salvar Crop", command=self.save_crop).pack(side=tk.LEFT, padx=5)
        
        # Frame da imagem
        self.image_frame = tk.Label(self.root, bg='gray')
        self.image_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.image_frame.bind("<Button-1>", self.on_image_click)
        
        # Frame inferior (controles)
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(bottom_frame, text="X:").pack(side=tk.LEFT, padx=5)
        self.x_entry = tk.Entry(bottom_frame, width=5)
        self.x_entry.pack(side=tk.LEFT, padx=5)
        self.x_entry.bind("<Return>", lambda e: self.update_from_entries())
        
        tk.Label(bottom_frame, text="Y:").pack(side=tk.LEFT, padx=5)
        self.y_entry = tk.Entry(bottom_frame, width=5)
        self.y_entry.pack(side=tk.LEFT, padx=5)
        self.y_entry.bind("<Return>", lambda e: self.update_from_entries())
        
        tk.Label(bottom_frame, text="W:").pack(side=tk.LEFT, padx=5)
        self.w_entry = tk.Entry(bottom_frame, width=5)
        self.w_entry.pack(side=tk.LEFT, padx=5)
        self.w_entry.bind("<Return>", lambda e: self.update_from_entries())
        
        tk.Label(bottom_frame, text="H:").pack(side=tk.LEFT, padx=5)
        self.h_entry = tk.Entry(bottom_frame, width=5)
        self.h_entry.pack(side=tk.LEFT, padx=5)
        self.h_entry.bind("<Return>", lambda e: self.update_from_entries())
        
        self.root.bind("<Up>", lambda e: self.adjust_y(-10))
        self.root.bind("<Down>", lambda e: self.adjust_y(10))
        self.root.bind("<Left>", lambda e: self.adjust_x(-10))
        self.root.bind("<Right>", lambda e: self.adjust_x(10))
        
        self.info_label = tk.Label(self.root, text="Selecione uma imagem para começar")
        self.info_label.pack(pady=5)
        
    def load_image(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            initialdir="img"
        )
        if not filepath:
            return
        
        self.image = Image.open(filepath)
        self.image_path = filepath
        self.display_image()
        self.info_label.config(text=f"Imagem: {os.path.basename(filepath)} - {self.image.size}")
        
    def display_image(self):
        if not self.image:
            return
        
        # Criar cópia com retângulo de crop desenhado
        display = self.image.copy()
        from PIL import ImageDraw
        draw = ImageDraw.Draw(display)
        draw.rectangle(
            [(self.x, self.y), (self.x + self.width, self.y + self.height)],
            outline='red',
            width=3
        )
        
        # Redimensionar para caber na tela
        max_width = 700
        max_height = 400
        display.thumbnail((max_width, max_height))
        
        self.image_tk = ImageTk.PhotoImage(display)
        self.image_frame.config(image=self.image_tk)
        
        # Atualizar entries
        self.x_entry.delete(0, tk.END)
        self.x_entry.insert(0, str(self.x))
        self.y_entry.delete(0, tk.END)
        self.y_entry.insert(0, str(self.y))
        self.w_entry.delete(0, tk.END)
        self.w_entry.insert(0, str(self.width))
        self.h_entry.delete(0, tk.END)
        self.h_entry.insert(0, str(self.height))
        
    def adjust_x(self, delta):
        self.x = max(0, self.x + delta)
        self.display_image()
        
    def adjust_y(self, delta):
        self.y = max(0, self.y + delta)
        self.display_image()
        
    def on_image_click(self, event):
        # Usar clique como ponto de início do crop
        self.x = max(0, event.x - self.width // 2)
        self.y = max(0, event.y - self.height // 2)
        self.display_image()
        
    def update_from_entries(self):
        try:
            self.x = int(self.x_entry.get())
            self.y = int(self.y_entry.get())
            self.width = int(self.w_entry.get())
            self.height = int(self.h_entry.get())
            self.display_image()
        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos")
        
    def save_crop(self):
        if not self.image:
            messagebox.showerror("Erro", "Selecione uma imagem primeiro")
            return
        
        # Fazer crop
        cropped = self.image.crop((
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height
        ))
        
        # Salvar
        output_path = "img/progress_bar.png"
        cropped.save(output_path)
        messagebox.showinfo("Sucesso", f"Barra salva em:\n{output_path}\nResolução: {cropped.size}")
        print(f"✓ Barra de progresso salva: {output_path}")
        print(f"  Dimensões: {cropped.size}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarCropper(root)
    root.mainloop()
