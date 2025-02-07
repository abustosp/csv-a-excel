import tkinter as tk
import tkinter.ttk as ttk
import bin.convertidor as convertidor

def cafecito():
    import webbrowser
    webbrowser.open('https://cafecito.app/abustos')
    
def obtener_valores_procesar():
    subcarpetas = app.subcarpetas.get()
    subcarpetas = True if subcarpetas == 'SI' else False
    delimitador = app.opcion_delimitador.get()
    convertidor.convertidor('.csv', subcarpetas, delimitador)
    tk.messagebox.showinfo("Proceso Finalizado", "Proceso Finalizado")
    

class ConvertidorApp:
    def __init__(self, master=None):
        # build ui
        Toplevel_1 = tk.Tk() if master is None else tk.Toplevel(master)
        Toplevel_1.configure(
            background="#2e2e2e",
            cursor="arrow",
            height=250,
            width=325)
        try:
            Toplevel_1.iconbitmap("bin/ABP-blanco-en-fondo-negro.ico")
        except:
            pass
        Toplevel_1.minsize(280, 440)
        Toplevel_1.overrideredirect("False")
        Toplevel_1.resizable(False, False)
        Toplevel_1.title("Convertidor de CSV")
        Label_3 = ttk.Label(Toplevel_1)
        self.img_ABPblanco = tk.PhotoImage(
            file="bin/ABP-blanco-sin-fondo.png")
        Label_3.configure(
            background="#2e2e2e",
            image=self.img_ABPblanco)
        Label_3.pack(side="top")
        Label_1 = ttk.Label(Toplevel_1)
        Label_1.configure(
            background="#2e2e2e",
            compound="top",
            foreground="#ffffff",
            justify="right",
            relief="flat",
            takefocus=False,
            text='Convertidor masivo de CSVs a Excels',
            wraplength=325)
        Label_1.pack(expand=True, pady=10, side="top")
        label1 = ttk.Label(Toplevel_1)
        label1.configure(
            background="#2e2e2e",
            foreground="#ffffff",
            justify="center",
            text='Seleccionar Subcarpetas?')
        label1.pack(side="top")
        self.subcarpetas = tk.StringVar(value='NO')
        __values = ['SI', 'NO']
        self.opcion_subcarpeta = ttk.OptionMenu(
            Toplevel_1, self.subcarpetas, "NO", *__values, command=None)
        self.opcion_subcarpeta.pack(side="top")
        label2 = ttk.Label(Toplevel_1)
        label2.configure(
            background="#2e2e2e",
            foreground="#ffffff",
            justify="center",
            text='Delimitador de caracteres del CSV\n(los más comunes son "," ";" "|")')
        label2.pack(side="top")
        self.opcion_delimitador = ttk.Entry(Toplevel_1)
        self.opcion_delimitador.pack(side="top")
        self.procesar = ttk.Button(Toplevel_1)
        self.procesar.configure(text='Seleccionar Carpeta y Procesar', command=obtener_valores_procesar)
        self.procesar.pack(expand=True, padx=0, pady=4, side="top")
        label3 = ttk.Label(Toplevel_1)
        label3.configure(
            background="#2e2e2e",
            foreground="#ffffff",
            justify="center",
            text='por Agustín Bustos Piasentini\nhttps://www.Agustin-Bustos-Piasentini.com.ar/')
        label3.pack(expand=True, pady=10, side="top")
        self.cafecito = ttk.Button(Toplevel_1)
        self.cafecito.configure(text='Donaciones', command=cafecito)
        self.cafecito.pack(side="top")

        # Main widget
        self.mainwindow = Toplevel_1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = ConvertidorApp()
    app.run()
