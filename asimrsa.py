#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 22:27:41 2025

@author: santOS
"""

from sympy import mod_inverse

# 1. Seleccionamos dos primos grandes
p = 61
q = 53

# 2. Calculamos n
n = p * q

# 3. Calculamos la función de Euler
phi = (p - 1) * (q - 1)

# 4. Elegimos e (exponente público)
e = 17  # Debe ser coprimo con phi

# 5. Calculamos d (inverso modular de e mod phi)
d = mod_inverse(e, phi)  # Calcula d tal que (d * e) % phi = 1

# Claves generadas
public_key = (e, n)
private_key = (d, n)

print("Clave pública:", public_key)
print("Clave privada:", private_key)

#cifrado del mensaje
# Mensaje original (por ejemplo, la letra 'A' en ASCII = 65)
M = 65

# Cifrar: C = M^e mod n
C = pow(M, e, n)  # Python permite calcular (M**e) % n de forma eficiente

print("Mensaje cifrado:", C)

# Descifrar: M = C^d mod n
M_descifrado = pow(C, d, n)

print("Mensaje descifrado:", M_descifrado)