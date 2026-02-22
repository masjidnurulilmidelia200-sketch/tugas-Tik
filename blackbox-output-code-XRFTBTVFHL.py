import tkinter as tk
import random

class KuisMatematika:
    def __init__(self, root):
        self.root = root
        self.root.title("Kuis Matematika Interaktif")
        self.root.geometry("400x300")
        
        self.pertanyaan = []
        self.jawaban_benar = []
        self.skor = 0
        self.indeks_pertanyaan = 0
        
        # Generate 10 pertanyaan acak
        self.generate_pertanyaan()
        
        # Label untuk pertanyaan
        self.label_pertanyaan = tk.Label(root, text="", font=("Arial", 14))
        self.label_pertanyaan.pack(pady=20)
        
        # Entry untuk jawaban
        self.entry_jawaban = tk.Entry(root, font=("Arial", 14))
        self.entry_jawaban.pack(pady=10)
        
        # Tombol submit
        self.tombol_submit = tk.Button(root, text="Jawab", command=self.cek_jawaban, font=("Arial", 12))
        self.tombol_submit.pack(pady=10)
        
        # Label untuk skor
        self.label_skor = tk.Label(root, text=f"Skor: {self.skor}/10", font=("Arial", 12))
        self.label_skor.pack(pady=10)
        
        # Mulai kuis
        self.tampilkan_pertanyaan()
    
    def generate_pertanyaan(self):
        operasi = ['+', '-', '*', '/']
        for _ in range(10):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(operasi)
            if op == '/':
                # Pastikan pembagian bulat
                a = a * b
            pertanyaan = f"{a} {op} {b} = ?"
            if op == '+':
                jawaban = a + b
            elif op == '-':
                jawaban = a - b
            elif op == '*':
                jawaban = a * b
            elif op == '/':
                jawaban = a // b
            self.pertanyaan.append(pertanyaan)
            self.jawaban_benar.append(jawaban)
    
    def tampilkan_pertanyaan(self):
        if self.indeks_pertanyaan < len(self.pertanyaan):
            self.label_pertanyaan.config(text=self.pertanyaan[self.indeks_pertanyaan])
            self.entry_jawaban.delete(0, tk.END)
        else:
            self.label_pertanyaan.config(text=f"Kuis selesai! Skor akhir: {self.skor}/10")
            self.entry_jawaban.config(state='disabled')
            self.tombol_submit.config(state='disabled')
    
    def cek_jawaban(self):
        try:
            jawaban_user = int(self.entry_jawaban.get())
            if jawaban_user == self.jawaban_benar[self.indeks_pertanyaan]:
                self.skor += 1
                self.label_skor.config(text=f"Skor: {self.skor}/10")
            self.indeks_pertanyaan += 1
            self.tampilkan_pertanyaan()
        except ValueError:
            tk.messagebox.showerror("Error", "Masukkan angka yang valid!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KuisMatematika(root)
    root.mainloop()