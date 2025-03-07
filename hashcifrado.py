#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 01:29:26 2025

@author: santOS
"""

import hashlib

def calcular_sha256(mensaje):
    # Crear un objeto hash SHA-256
    hash_object = hashlib.sha256()
    
    # Convertir el mensaje a bytes (las funciones hash trabajan con bytes)
    mensaje_bytes = mensaje.encode('utf-8')
    
    # Actualizar el objeto hash con el mensaje
    hash_object.update(mensaje_bytes)
    
    # Obtener el hash en formato hexadecimal
    hash_hex = hash_object.hexdigest()
    
    return hash_hex

# Ejemplo de uso
mensaje = "Hola, mundo!"
hash_resultado = calcular_sha256(mensaje)
print(f"El hash SHA-256 de '{mensaje}' es: {hash_resultado}")