import tkinter as tk
from tkinter import font
from config import constantes as cons
from utils import util_ventana

class FormularioCalculadora(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widget()

    def config_window(self):
        self.title("Calculadora")
        self.configure(bg=cons.COLOR_FONDO_DARK)
        self.attributes('-alpha', 0.96)
        w,h = 350, 570
        util_ventana.centrar_ventana(self, w,h)
        self.resizable(width=False, height=False)

    def construir_widget(self):

        tk.Button(self, text="Conversor", command=self.abrir_conversor,
                  bg=cons.COLOR_BOTONES_ESPECIALES_DARK, fg=cons.COLOR_TEXTO_DARK, borderwidth=0, highlightthickness=0,
                  font=('Arial', 10, 'bold'), relief=tk.FLAT).grid(row=0, column=0, padx=5, pady=10)

        self.operation_label = tk.Label(self, text="", font=('Arial', 16), 
            fg=cons.COLOR_TEXTO_DARK, bg = cons.COLOR_FONDO_DARK, justify = 'right')
        self.operation_label.grid(row=0, column=3, padx=5, pady=10)

        self.entry = tk.Entry(self, width=12, font=(
            'Arial', 36), bd=0, fg=cons.COLOR_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK, justify='right', insertwidth=0 )
        self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        #Lista de botones

        buttons = [
            'C', '%', '<', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row_val = 2 
        col_val = 0

        roboto_font = font.Font( family='Roboto', size =16)

        for button in buttons:
            if button in ['=', '*', '/', '-', '+', 'C', '<', '%']:
                color_fondo = cons.COLOR_BOTONES_ESPECIALES_DARK
                button_font = font.Font(size=16, weight='bold')
            else:
                color_fondo = cons.COLOR_BOTONES_DARK
                button_font = roboto_font


            if button == '=':
                tk.Button(self, text=button, width=12, height=2, command=lambda b=button: self.on_button_click(b),
                    bg=color_fondo, fg=cons.COLOR_TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5, 
                    borderwidth=0, highlightthickness=0, overrelief='flat').grid(row=row_val, column=col_val, columnspan=2, pady=5)
                col_val += 1
            else:
                tk.Button(self, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b),
                    bg=color_fondo, fg= cons.COLOR_TEXTO_DARK, 
                    relief=tk.FLAT, font=button_font, padx=5, pady=5, 
                    borderwidth=0, highlightthickness=0, overrelief='flat').grid(row=row_val, column=col_val, pady=5)
                col_val += 1

            if col_val > 3:
                col_val = 0
                row_val +=1

    def on_button_click(self, value):
        if len(self.entry.get()) >= 15 and value not in ['=', 'C', '<']:
            return

        if value == '=':
            try:
                expression = self.entry.get().replace('%', '/100')
                result = "{:.10g}".format(eval(expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                operation = expression + " ="

                if len(operation) > 5:
                    operation = "..." + operation[-5:]

                self.operation_label.config(text=operation)
                
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "ERROR")
                self.operation_label.config(text='')
        
        elif value == 'C':
            self.entry.delete(0, tk.END)
            self.operation_label.config(text='') 

        elif value == '<':
            current_text = self.entry.get()
            if current_text:
                new_text = current_text[:-1]
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)
                self.operation_label.config(text=new_text + " ")

        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)
            if value == '=':
                self.operation_label.config(text='')

    def abrir_conversor(self):
        self.destroy()
        FormularioConversor()

class FormularioConversor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.construir_widget()

    def config_window(self):
        self.title("Conversor Temp")
        self.configure(bg=cons.COLOR_FONDO_DARK)
        w,h = 250, 300
        util_ventana.centrar_ventana(self, w, h)
        self.resizable(width=False, height=False)

    def construir_widget(self):
        button_font = font.Font(size=12, weight='bold')
        # Botón para volver a la calculadora
        tk.Button(self, text="← Calculadora", command=self.abrir_calculadora, borderwidth=0, highlightthickness=0,
                  bg=cons.COLOR_BOTONES_ESPECIALES_DARK, fg=cons.COLOR_TEXTO_DARK, font=button_font,  justify='center',
                  relief=tk.FLAT).grid(row=3, column=0, padx=10, pady=10)
        
        # Etiqueta de resultado
        self.label_resultado = tk.Label(self, text="", font=('Arial', 18),
                                       bg=cons.COLOR_FONDO_DARK, fg=cons.COLOR_TEXTO_DARK)
        self.label_resultado.grid(row=0, column=0, columnspan=2, pady=30)

        # Entrada de valor
        self.entry_temp = tk.Entry(self, font=('Arial', 24), width=10, justify='center')
        self.entry_temp.grid(row=1, column=0, columnspan=2, pady=20, padx=20 )

        # Botones de conversión
        tk.Button(self, text="C° a F°", width=10, command=self.c_to_f, borderwidth=0, highlightthickness=0,
                  bg=cons.COLOR_BOTONES_DARK, fg=cons.COLOR_TEXTO_DARK).grid(row=2, column=0, pady=10)
        
        tk.Button(self, text="F° a C°", width=10, command=self.f_to_c, borderwidth=0, highlightthickness=0,
                  bg=cons.COLOR_BOTONES_DARK, fg=cons.COLOR_TEXTO_DARK).grid(row=2, column=1, pady=10)

    def c_to_f(self):
        try:
            c = float(self.entry_temp.get())
            res = (c * 9/5) + 32
            self.label_resultado.config(text=f"{res:.2f} F°")
        except: self.label_resultado.config(text="Error")

    def f_to_c(self):
        try:
            f = float(self.entry_temp.get())
            res = (f - 32) * 5/9
            self.label_resultado.config(text=f"{res:.2f} C°")
        except: self.label_resultado.config(text="Error")

    def abrir_calculadora(self):
        self.destroy()
        FormularioCalculadora()