"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_07():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dic = {}
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma una linea de la columna 5
            num= int(fila[1])
            
            # Si no esta en el diccionario, se crea
            if num not in dic:
                dic[num] = [fila[0]]
            # Se añaden letras al diccionario en caso de que ya exista su clave
            else:
                dic[num].append(fila[0])
        

    # Se ponen en formato de tupla  se ordena en base a su número(menor a mayor)
    lista = [(clave, valor) for clave, valor in sorted(dic.items())]
    
    return lista
