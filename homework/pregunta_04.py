"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv

def pregunta_04():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dic = {}
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Obtiene la fecha y separa el mes
            fecha = fila[2].split('-')
            mes = fecha[1]

            if mes in dic:
                dic[mes] += 1
            else:
                dic[mes] = 1

    # Se obtienen los objetos del dic, y se ordenan en base a su letra
    lista = list(dic.items())
    lista.sort()
    
    return lista
