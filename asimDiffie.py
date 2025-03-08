#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 22:31:39 2025

@author: santOS
"""

import random

# Paso 1: Selección de números primos públicos
p = 23  # Número primo
g = 5   # Base (raíz primitiva)

# Paso 2: Elección de claves privadas
a = random.randint(1, p-1)  # Clave privada de Alice
b = random.randint(1, p-1)  # Clave privada de Bob

# Paso 3: Cálculo de claves públicas
A = pow(g, a, p)  # A = g^a mod p
B = pow(g, b, p)  # B = g^b mod p

print(f"Clave pública de Alice (A): {A}")
print(f"Clave pública de Bob (B): {B}")

# Paso 4: Cálculo de clave compartida
S_Alice = pow(B, a, p)  # Clave secreta calculada por Alice
S_Bob = pow(A, b, p)    # Clave secreta calculada por Bob

print(f"Clave compartida de Alice: {S_Alice}")
print(f"Clave compartida de Bob: {S_Bob}")

# Ambas claves deben coincidir
assert S_Alice == S_Bob, "Error: Las claves no coinciden"
print("¡Clave compartida establecida correctamente!")
