import tkinter as tk

def calculadora():
    try:
        resultado = eval(entry.get())
        resultado_label.config(text="Resultado: "+str(resultado))
    except Exception as e:
        resultado_label.config(text="Error en la entrada")

def clear():
    entry.delete(0,tk.END)
    resultado_label.config(text="")

ventana = tk.Tk()
ventana.title("Calculadora Diseña simple")

entry = tk.Entry(ventana,width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, pady=10)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in botones:
    if text == '=':
        tk.Button(ventana, text=text, width=10, height=2, command=calculadora).grid(row=row, column=col, pady=5)
    elif text == 'C':
        tk.Button(ventana, text=text, width=10, height=2, command=clear).grid(row=row, column=col, pady=5)
    else:
        tk.Button(ventana, text=text, width=10, height=2, command=lambda t=text: entry.insert(tk.END, t)).grid(row=row, column=col, pady=5)

resultado_label = tk.Label(ventana, text="", font=('Arial', 12))
resultado_label.grid(row=6, column=0, columnspan=4, pady=10)

ventana.mainloop()