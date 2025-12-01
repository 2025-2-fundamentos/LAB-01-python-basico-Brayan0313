"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_09():
    route = "files/input/data.csv"
    # Diccionario que almacena los registros
    dic = {}
    with open(route, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma una linea de la columna 5
            cadena= fila[4]
            # Se divide la cadena, separa por comas
            datos = cadena.split(',')

            #
            # Se itera sobre cada uno de los datos separados
            #
            for dato in datos:
                # Se separan en pares de clave valor
                clave, valor = dato.split(':')

                # Se inicia el conteo de cuantas veces aparece una clave
                if clave not in dic:
                    dic[clave] = 1
                else:
                    dic[clave] += 1
        
        return dic