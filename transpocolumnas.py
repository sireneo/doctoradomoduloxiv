#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 23:40:15 2025

@author: santOS
"""

def cifrado_transposicion(texto, clave):
    # Eliminar espacios y convertir a mayúsculas
    texto = texto.replace(" ", "").upper()
    # Calcular el número de filas necesarias
    filas = (len(texto) // clave) + (1 if len(texto) % clave != 0 else 0)
    # Crear la matriz de transposición
    matriz = [['' for _ in range(clave)] for _ in range(filas)]
    # Llenar la matriz por filas
    index = 0
    for fila in range(filas):
        for columna in range(clave):
            if index < len(texto):
                matriz[fila][columna] = texto[index]
                index += 1
            else:
                matriz[fila][columna] = 'X'  # Relleno si es necesario
     # Mostrar la matriz de columnas
    print("\nMatriz de columnas (cifrado):")
    for fila in matriz:
        print(fila)
    # Leer la matriz por columnas para obtener el texto cifrado
    texto_cifrado = ""
    for columna in range(clave):
        for fila in range(filas):
            texto_cifrado += matriz[fila][columna]
    return texto_cifrado

def descifrado_transposicion(texto_cifrado, clave):
    # Calcular el número de filas necesarias
    filas = (len(texto_cifrado) // clave) + (1 if len(texto_cifrado) % clave != 0 else 0)
    # Crear la matriz de transposición
    matriz = [['' for _ in range(clave)] for _ in range(filas)]
    # Llenar la matriz por columnas
    index = 0
    for columna in range(clave):
        for fila in range(filas):
            if index < len(texto_cifrado):
                matriz[fila][columna] = texto_cifrado[index]
                index += 1
    # Leer la matriz por filas para obtener el texto original
    texto_original = ""
    for fila in range(filas):
        for columna in range(clave):
            texto_original += matriz[fila][columna]
    return texto_original

# Solicitar datos desde el teclado
texto_original = input("Ingrese el texto original: ")
clave = int(input("Ingrese la clave (número de columnas): "))

# Cifrar el texto
texto_cifrado = cifrado_transposicion(texto_original, clave)
print(f"Texto cifrado: {texto_cifrado}")

# Descifrar el texto
texto_descifrado = descifrado_transposicion(texto_cifrado, clave)
print(f"Texto descifrado: {texto_descifrado}")