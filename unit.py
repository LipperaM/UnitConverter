import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x500")
root.title("Conversor de unidades para Fisica")

subTitle = tk.Label(
    root, text="Selecciona el grupo de unidades a convertir:", font=(18))
subTitle.pack(padx=20, pady=20)

notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Masa")
label1 = tk.Label(tab1, text="Conversion de masa")
label1.pack(padx=10, pady=10)

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Longitud")
label2 = tk.Label(tab2, text="Conversion de longitud")
label2.pack(padx=10, pady=10)

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Area")
label3 = tk.Label(tab3, text="Conversion de area")
label3.pack(padx=10, pady=10)

tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Volumen")
label4 = tk.Label(tab4, text="Conversiond de volumen")
label4.pack(padx=10, pady=10)

tab5 = ttk.Frame(notebook)
notebook.add(tab5, text="Tiempo")
label5 = tk.Label(tab5, text="Conversion de tiempo")
label5.pack(padx=10, pady=10)

notebook.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)


root.mainloop()
