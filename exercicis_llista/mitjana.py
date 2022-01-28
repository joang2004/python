"""
Et fa lan mitjana de la llista
"""

valors=[1,2,3,4,5,6,7]
suma=0
mitjana=0
for i in valors:
    suma+=i

mitjana=suma/len(valors)

print("La mitjana dels valors és: " + str(mitjana))