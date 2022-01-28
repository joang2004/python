"""
Escribe un programa que reciba un número del usuario e imprima si es positivo, negativo o cero. Utiliza la cadena
if/elif/else apropiada.
No vayas a emplear tres if consecutivos.
"""

num=float(input("Introdueix un nombre: "))
if num > 0 :
    print("El nombre és positiu.")
elif num < 0:
    print("El nombre es negatiu.")
else:
    print("El nombre és cero.")