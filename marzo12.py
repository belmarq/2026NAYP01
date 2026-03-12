import tkinter as tk
from tkinter import simpledialog, messagebox

'''
Quiero un programa en python que me solicite un capital inicial, 
una tasa de interés mensual y un número de meses, 
y luego calcule el monto final después de aplicar el interés compuesto mensualmente. 
El programa debe mostrar la ganancia obtenida.
El programa debera ejecutarse en un ambiente grafico tipo awt, no de consola.
'''
class CompoundInterestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Interés Compuesto")
        self.root.geometry("400x200")
        
        tk.Label(root, text="Capital Inicial ($):").pack(pady=5)
        self.capital_entry = tk.Entry(root)
        self.capital_entry.pack()
        
        tk.Label(root, text="Tasa de Interés Mensual (%):").pack(pady=5)
        self.rate_entry = tk.Entry(root)
        self.rate_entry.pack()
        
        tk.Label(root, text="Número de Meses:").pack(pady=5)
        self.months_entry = tk.Entry(root)
        self.months_entry.pack()
        
        tk.Button(root, text="Calcular", command=self.calculate).pack(pady=10)
    
    def calculate(self):
        try:
            capital = float(self.capital_entry.get())
            rate = float(self.rate_entry.get()) / 100
            months = int(self.months_entry.get())
            
            final_amount = capital * ((1 + rate) ** months)
            gain = final_amount - capital
            
            messagebox.showinfo("Resultados", 
                f"Capital Inicial: ${capital:.2f}\n"
                f"Monto Final: ${final_amount:.2f}\n"
                f"Ganancia: ${gain:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompoundInterestCalculator(root)
    root.mainloop()