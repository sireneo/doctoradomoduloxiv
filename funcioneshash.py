#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 01:08:57 2025

@author: santOS
"""

import hashlib

# Función para calcular el hash de un mensaje usando diferentes algoritmos
def calcular_hash(mensaje, algoritmo='sha256'):
    # Crear un objeto hash según el algoritmo especificado
    hash_object = hashlib.new(algoritmo)
    
    # Convertir el mensaje a bytes
    mensaje_bytes = mensaje.encode('utf-8')
    
    # Actualizar el objeto hash con el mensaje
    hash_object.update(mensaje_bytes)
    
    # Obtener el hash en formato hexadecimal
    return hash_object.hexdigest()

# Ejemplos de uso
mensaje = "Hola, mundo!"

# MD5 (No seguro, solo para propósitos educativos)
print(f"MD5: {calcular_hash(mensaje, 'md5')}")

# SHA-1 (No seguro, solo para propósitos educativos)
print(f"SHA-1: {calcular_hash(mensaje, 'sha1')}")

# SHA-256 (Seguro y ampliamente utilizado)
print(f"SHA-256: {calcular_hash(mensaje, 'sha256')}")

# SHA-3 (Alternativa segura)
print(f"SHA-3 (256 bits): {calcular_hash(mensaje, 'sha3_256')}")
