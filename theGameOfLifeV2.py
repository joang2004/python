########################################
#######FALTA UN CONTROL DEL TAMANY######
###############DEL TABLERO##############
########################################

########################################
#####UTILITZA LA MATEIXA LLISTA PER#####
############TORNA A COMPARAR############
########################################

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

def Llista_Resultat(inicial, pla, linea, columna):
    resultat=pla.copy()
    
    for j in range(linea):
        for i in range(columna):
            veinat=Recompte_veinat(inicial, j,i, linea, columna)
            x = Actualitza(inicial,veinat, j, i)
            print("Resultat:"+str(x) + " " +str(inicial[j][i]) + " " + str(veinat) )
            resultat[j].pop(i)
            resultat[j].insert(i,x)
            

    return resultat

def Recompte_veinat(inicial, linea, columna, n, m):
    veinat=0
    try:
        if inicial[linea-1][columna-1] == "B" and (linea-1) >= 0 and (columna-1) >=0 :
            veinat+=1
    except:
        pass
    try:
        if inicial[linea-1][columna] == "B" and (linea-1)>=0:
            veinat+=1
    except:
        pass
    try:
        if inicial[linea-1][columna+1] == "B" and (linea-1) >= 0 and (columna+1)< m:
            veinat+=1
    except:
        pass
    try:
        if inicial[linea][columna-1] == "B"and (columna-1) >=0:
            veinat+=1
    except:
        pass
    try:
        if inicial[linea][columna+1] == "B" and (columna+1) < m:
            veinat+=1
    except:
        pass
    try:
        if inicial[linea+1][columna-1] == "B" and (linea+1)<n and (columna-1)>= 0:
            veinat+=1
    except:
        pass
    try:
        if inicial[linea+1][columna] == "B" and (linea+1)<n :
            veinat+=1
    except:
        pass
    try:
        if inicial[linea+1][columna+1] == "B" and (linea+1)<n and (columna+1)<m:
            veinat+=1
    except:
        pass
    
    return veinat

def Actualitza(inicial, veinat, linea, columna):
    if inicial[linea][columna]=='B':
        if veinat<2 or veinat >3:
            return "."
        else:
            return "B"
    else:
        if veinat != 3:
            return "."
        else:
            return "B"

n=read(int) #linea
m=read(int)#columna
pla=[]

pla=Crea_Pla(pla,n,m)
inicial=Valors_Inicials(pla)
for i in inicial:
    print(i)
final=Llista_Resultat(inicial, pla, n, m)

for i in final:
    print(i)