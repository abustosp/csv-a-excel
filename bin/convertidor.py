import pandas as pd
import openpyxl
import os
from tkinter.filedialog import askdirectory

def listador(ruta):
    """
    Función que recibe una ruta y devuelve una lista con los archivos que se encuentran en ella.
    """
    
    archivos = os.listdir(ruta)
    archivos = [os.path.join(ruta, archivo) for archivo in archivos]
    
    return archivos


def listador_subcarpetas(ruta):
    """
    Función que recibe una ruta y devuelve una lista con los archivos que se encuentran en ella y en sus subcarpetas.
    """

    archivos = []

    for base, dirs, files in os.walk(ruta):
        for file in files:
            archivos.append(os.path.join(base, file))

    return archivos


def convertidor(extensión:str, subcarpetas:bool=False, delimitador:str=','):
    """
    Función para convertir los CSV a Excel.

    ### Args:
        - ruta (str): Ruta con Archivos a Convertir
        - extensión (str): Extensión de los Archivos a Convertir
        - subcarpetas (bool, optional): Indica si se deben buscar archivos en subcarpetas. Defaults es False.
    """
    
    ruta = askdirectory(title='Selecciona la Carpeta con los Archivos a Convertir')
    
    if subcarpetas==False:
        archivos = listador(ruta)
    else:
        archivos = listador_subcarpetas(ruta)
            
    for archivo in archivos:
        if archivo.endswith(extensión):
            try:
                df = pd.read_csv(archivo, delimiter=delimitador)
                df.to_excel(archivo.replace(extensión , ".xlsx"), index=False)
            except:
                print(f'Error al convertir {archivo}')



