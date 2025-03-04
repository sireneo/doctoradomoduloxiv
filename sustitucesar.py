#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:36:27 2025

@author: santOS
"""
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        # Verificamos si la letra es mayúscula
        if letra.isupper():
            # Aplicamos el desplazamiento y manejamos el desbordamiento con módulo 26
            resultado += chr((ord(letra) - ord('A') + desplazamiento) % 26 + ord('A'))
        # Verificamos si la letra es minúscula
        elif letra.islower():
            # Aplicamos el desplazamiento y manejamos el desbordamiento con módulo 26
            resultado += chr((ord(letra) - ord('a') + desplazamiento) % 26 + ord('a'))
        else:
            # Si no es una letra (espacios, puntuación, etc.), lo dejamos igual
            resultado += letra
    return resultado

def descifrado_cesar(texto_cifrado, desplazamiento):
    # El descifrado es simplemente aplicar un desplazamiento negativo
    return cifrado_cesar(texto_cifrado, -desplazamiento)

# Pedir al usuario que ingrese el mensaje y el desplazamiento
texto_original = input("Ingresa el mensaje a cifrar: ")
desplazamiento = int(input("Ingresa el desplazamiento (número entero): "))

# Cifrar
texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print(f"Texto cifrado: {texto_cifrado}")

# Descifrar
texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)
print(f"Texto descifrado: {texto_descifrado}")
