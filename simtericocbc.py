#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 00:08:32 2025

@author: santOS
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Generar una clave AES de 256 bits (32 bytes)
clave = os.urandom(32)

# Crear un vector de inicialización (IV) de 16 bytes
iv = os.urandom(16)

# Texto a cifrar
mensaje = "Este es un mensaje secreto"
datos = mensaje.encode()  # Convertir a bytes

# Cifrado
cipher = AES.new(clave, AES.MODE_CBC, iv)
datos_cifrados = cipher.encrypt(pad(datos, AES.block_size))

print("Texto Cifrado:", datos_cifrados.hex())

# Descifrado
cipher_descifrado = AES.new(clave, AES.MODE_CBC, iv)
datos_descifrados = unpad(cipher_descifrado.decrypt(datos_cifrados), AES.block_size)

print("Texto Descifrado:", datos_descifrados.decode())
