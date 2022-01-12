""""
def nombre_valid_positiu(x): #S'utilitza en per saber si una longitud es valida
    x=x.replace(".", ",") 
    comes=x.count(",")
    guions=x.count("-")
    posicio_comes=x.find(",")

    if comes > 0 or guions > 0 or not x.isdigit():
        return False
    else:
        resultat=x.replace("-", "")
        nombre=resultat.replace(",", "")
        return True
"""
def valid(valors):
    for i in valors:
    if i.isdecimal() and len(i) == 1 :
        if i == "0":
            return False
        else:
            return True
    else:
        return False

valors = []
for i in range(3):
    ey=input("nombre: ")
    valors.append(ey)
es_valid=valid(valors)

