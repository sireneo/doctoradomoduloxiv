#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 23:57:46 2025

@author: santOS
"""

from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

# Clave de 256 bits (32 bytes)
clave = os.urandom(32)

# Inicializar un contador para el modo CTR
nonce = os.urandom(8)  # 8 bytes de nonce
contador = Counter.new(64, prefix=nonce)

def cifrar_AES_CTR(mensaje):
    cipher = AES.new(clave, AES.MODE_CTR, counter=contador)
    return cipher.encrypt(mensaje.encode())

def descifrar_AES_CTR(cifrado):
    contador_descifrado = Counter.new(64, prefix=nonce)
    cipher = AES.new(clave, AES.MODE_CTR, counter=contador_descifrado)
    return cipher.decrypt(cifrado).decode()

mensaje = "Mensaje secreto en modo CTR"
cifrado = cifrar_AES_CTR(mensaje)
print("Cifrado:", cifrado.hex())

descifrado = descifrar_AES_CTR(cifrado)
print("Descifrado:", descifrado)
