from easyinput import read


def Crea_Pla(llista, linea,columna):
    for j in range(linea):
        llista.append([])
    
        for i in range(columna):
            llista[j].append('.')
    return llista

def Valors_Inicials(llista):
    linea_inicial=read(str)
    j=0
    while linea_inicial is not None:
        i=0
        for caracter in linea_inicial:
            llista[j].pop(i)
            llista[j].insert(i,caracter)
            i+=1
        j+=1
        linea_inicial=read(str)
    return llista

n=read(int) #linea
m=read(int)#columna

pla=[]
pla=Crea_Pla(pla,n,m)

"""""
j=0
while linea_inicial is not None:
    i=0
    for caracter in linea_inicial:
        pla[j].pop(i)
        pla[j].insert(i,caracter)
        i+=1
    j+=1
    linea_inicial=read(str)
""" 

pla=Valors_Inicials(pla)












for i in pla:
    print(i)
