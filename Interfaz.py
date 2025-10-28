import tkinter as tk
import ttkbootstrap as ttk
import Algoritmos as Algs

class ventana_lru:
    def __init__(self):
        self.root = ttk.Window(themename="minty")
        self.root.title("LRU")
        self.root.geometry("500x400")

        # Variables de control
        self.marcos = tk.IntVar(value=0)
        self.array_pg = []
        self.alg = tk.StringVar(value="LRU")

        self.label_datos = ttk.Label(self.root, bootstyle="info", anchor="center", text="Ingrese los datos: ")
        self.label_datos.place(x=100, y=50, width=120, height=30)

        self.txt_marcos = ttk.Label(self.root, text="Marcos: ")
        self.txt_marcos.place(x=125, y= 105)
        self.entry_marcos = ttk.Entry(self.root, bootstyle="info", textvariable=self.marcos)
        self.entry_marcos.place(x=250, y=100, width=100, height=30)

        self.txt_nums = ttk.Label(self.root, text="Números de pagina: ")
        self.txt_nums.place(x=125, y=145)
        self.entry_nums = ttk.Entry(self.root, bootstyle="info")
        self.entry_nums.place(x=250, y=145, width=100, height=30)
        self.boton_guardar = tk.Button(self.root, text="Guardar en Array", command=lambda: guardar_datos(self))
        self.boton_guardar.place(x=360, y=145, width=100, height=30)
        self.label_array = ttk.Label(self.root, text="Datos guardados")
        self.label_array.place(x=220, y=190)

        self.boton_alg_LRU = ttk.Button(self.root, text="Probar con Algoritmo LRU", command=lambda: envio_algs(self))
        self.boton_alg_LRU.place(x=180, y=240, width=200, height=30)

        self.txt_resultado = ttk.Label(self.root, text="No. de Fallos: ")
        self.txt_resultado.place(x=200, y=280)
        self.label_fallos = ttk.Label(self.root, text="Fallos")
        self.label_fallos.place(x=290, y=280)


class ventana_bit_referencia:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")
        self.root.title("Bit de Referencia")
        self.root.geometry("500x400")

        # Variables de control
        self.marcos = tk.IntVar(value=0)
        self.array_pg = []
        self.alg = tk.StringVar(value="bit")

        self.label_datos = ttk.Label(self.root, bootstyle="info", anchor="center", text="Ingrese los datos: ")
        self.label_datos.place(x=100, y=50, width=120, height=30)

        self.txt_marcos = ttk.Label(self.root, text="Marcos: ")
        self.txt_marcos.place(x=125, y= 105)
        self.entry_marcos = ttk.Entry(self.root, bootstyle="info", textvariable=self.marcos)
        self.entry_marcos.place(x=250, y=100, width=100, height=30)

        self.txt_nums = ttk.Label(self.root, text="Números de pagina: ")
        self.txt_nums.place(x=125, y=145)
        self.entry_nums = ttk.Entry(self.root, bootstyle="info")
        self.entry_nums.place(x=250, y=145, width=100, height=30)
        self.boton_guardar = tk.Button(self.root, text="Guardar en Array", command=lambda: guardar_datos(self))
        self.boton_guardar.place(x=360, y=145, width=100, height=30)
        self.label_array = ttk.Label(self.root, text="Datos guardados")
        self.label_array.place(x=220, y=190)

        self.boton_alg_bit = ttk.Button(self.root, text="Probar con Algoritmo Bit de referencia", command=lambda: envio_algs(self))
        self.boton_alg_bit.place(x=130, y=240, width=250, height=30)

        self.txt_resultado = ttk.Label(self.root, text="No. de Fallos: ")
        self.txt_resultado.place(x=200, y=280)
        self.label_fallos = ttk.Label(self.root, text="Fallos")
        self.label_fallos.place(x=290, y=280)


class ventana_optimo:
    def __init__(self):
        self.root = ttk.Window(themename="cosmo")
        self.root.title("Algoritmo Óptimo")
        self.root.geometry("500x400")

        # Variables de control
        self.marcos = tk.IntVar(value=0)
        self.array_pg = []
        self.alg = tk.StringVar(value="Op")

        self.label_datos = ttk.Label(self.root, bootstyle="info", anchor="center", text="Ingrese los datos: ")
        self.label_datos.place(x=100, y=50, width=120, height=30)

        self.txt_marcos = ttk.Label(self.root, text="Marcos: ")
        self.txt_marcos.place(x=125, y= 105)
        self.entry_marcos = ttk.Entry(self.root, bootstyle="info", textvariable=self.marcos)
        self.entry_marcos.place(x=250, y=100, width=100, height=30)

        self.txt_nums = ttk.Label(self.root, text="Números de pagina: ")
        self.txt_nums.place(x=125, y=145)
        self.entry_nums = ttk.Entry(self.root, bootstyle="info")
        self.entry_nums.place(x=250, y=145, width=100, height=30)
        self.boton_guardar = tk.Button(self.root, text="Guardar en Array", command=lambda: guardar_datos(self))
        self.boton_guardar.place(x=360, y=145, width=100, height=30)
        self.label_array = ttk.Label(self.root, text="Datos guardados")
        self.label_array.place(x=220, y=190)

        self.boton_alg_optimo = ttk.Button(self.root, text="Probar con Algoritmo Optimo", command=lambda: envio_algs(self))
        self.boton_alg_optimo.place(x=180, y=240, width=200, height=30)

        self.txt_resultado = ttk.Label(self.root, text="No. de Fallos: ")
        self.txt_resultado.place(x=200, y=280)
        self.label_fallos = ttk.Label(self.root, text="Fallos")
        self.label_fallos.place(x=290, y=280)

def envio_algs(self):
    algs = self.alg.get()

    marcos_txt = self.entry_marcos.get()
    try:
        marcos = int(marcos_txt)
    except ValueError:
        self.label_fallos.config(text="Error: Número de marcos invalido.")
        return
    
    array_pg = self.array_pg
    array_pg_int = [int(i) for i in array_pg]
    peticiones = len(array_pg_int)

    if algs=="Op":
        fallos_op = Algs.Optimo(array_pg_int, peticiones, marcos) 
        self.label_fallos.config(text=fallos_op)

    if algs=="LRU":
        fallos_LRU = Algs.LRU(array_pg_int, peticiones, marcos)
        self.label_fallos.config(text=fallos_LRU)

    if algs=="bit":
        fallos_bit = Algs.aciertos_y_fallos(array_pg_int, marcos)
        self.label_fallos.config(text=fallos_bit)

def guardar_datos(self):
    info_nums = self.entry_nums.get()

    if info_nums:
        self.array_pg.append(info_nums)
        self.entry_nums.delete(0, tk.END)
        self.label_array.config(text=self.array_pg)


class ventana_principal:
    def __init__(self):
        
        self.root = ttk.Window(themename="cosmo")
        self.root.title("Simulación de Reemplazo de Páginas")
        self.root.geometry("400x300")

        # Optimo
        self.boton_optimo = ttk.Button(self.root, text="Algoritmo Óptimo", bootstyle="info, outline", command=self.Alg_optimo)
        self.boton_optimo.pack(pady=20)

        # Bit de referencia
        self.boton_bit_referencia = ttk.Button(self.root, text="Bit de Referencia", bootstyle="danger, outline", command=self.Alg_bit_referencia)
        self.boton_bit_referencia.pack(pady=20)

        # LRU
        self.boton_lru = ttk.Button(self.root, text="Algoritmo LRU", bootstyle="success, outline", command=self.Alg_lru)
        self.boton_lru.pack(pady=20)


        # Abre ventana principal
        self.root.mainloop()

    def Alg_optimo(self):
        ventana_optimo()

    def Alg_bit_referencia(self):
        ventana_bit_referencia()

    def Alg_lru(self):
        ventana_lru()


if __name__ == "__main__":
    ventana_principal()