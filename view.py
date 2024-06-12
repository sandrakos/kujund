import tkinter as tk
from tkinter import messagebox

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Püramiidi Kalkulaator")

        self.base_length_label = tk.Label(root, text="Põhja pikkus (a):")
        self.base_length_label.pack()
        self.base_length_entry = tk.Entry(root)
        self.base_length_entry.pack()

        self.height_label = tk.Label(root, text="Kõrgus (h):")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        self.calculate_button = tk.Button(root, text="Arvuta", command=None)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def set_calculate_button_command(self, command):
        self.calculate_button.config(command=command)

    def get_base_length(self):
        try:
            return float(self.base_length_entry.get())
        except ValueError:
            messagebox.showerror("Viga", "Palun sisestage korrektne põhja pikkus!")
            return None

    def get_height(self):
        try:
            return float(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Viga", "Palun sisestage korrektne kõrgus!")
            return None

    def display_results(self, base_area, volume, lateral_surface_area, surface_area):
        result_text = (
            f"Põhja pindala: {base_area}\n"
            f"Ruumala: {volume}\n"
            f"Külgede pindala: {lateral_surface_area}\n"
            f"Kogupindala: {surface_area}"
        )
        self.result_label.config(text=result_text)
