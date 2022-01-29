"""
jugador-->1
ordinador-->2
buit-->0
"""
import random
disponibles=[0,1,2,3,4,5,6,7,8]
graella=[[0,0,0],[0,0,0],[0,0,0]]
ocupat=True

def llistagraella(graella,posicio, es_ordinador):
    i=int(posicio/3)
    j=posicio%3
    if es_ordinador ==False:
        graella[i][j]=1
    else:
        graella[i][j]=2
    return graella
    
def guanya(graella, es_ordinador):
    for i in range(3):#Comparació per columnes
        if graella[0][i] == graella[1][i] == graella[2][i] and graella[0][i] != 0:
            if es_ordinador == False:
                imprimir(graella)
                print("GUANYA EL JUGADOR")
                exit()
            else:
                imprimir(graella)
                print("GUANYA L'ORDINADOR")
                exit()
    if graella[0][0] == graella[1][1] ==graella[2][2] and graella[0][0]!= 0 or graella[0][2] == graella[1][1] ==graella[2][0] and graella[0][2]!= 0: #Comprovació de  diagonals
            if es_ordinador == False:
                imprimir(graella)
                print("GUANYA EL JUGADOR")
                exit()
            else:
                imprimir(graella)
                print("GUANYA L'ORDINADOR")
                exit()
    for i in range(3):
        if graella[i][0] == graella[i][1]== graella[i][2] and graella[i][0] != 0: #Comprova per linees
            if es_ordinador == False:
                imprimir(graella)
                print("GUANYA EL JUGADOR")
                exit()
            else:
                imprimir(graella)
                print("GUANYA L'ORDINADOR")
                exit()

def imprimir(graella):
    print()
    for i in range(3):
        print(graella[i])


print("JOC DEL TRES EN RALLA\nJugador -->1\nOrdinador -->2\nPosició buida -->0")
print("Les posicions dintre del joc són les següents:\n[0,1,2]\n[3,4,5]\n[6,7,8]")

while len(disponibles)>0:
    ocupat=True
    while ocupat ==True:
        imprimir(graella)
        jugador=input("introdueix la posició que voleu colocar la fitxa: ")
        try:
            disponibles.remove(int(jugador))
            ocupat=False
        except:
            print("Introdueix una posició correcta")
            ocupat=True
    
    graella=llistagraella(graella,int(jugador), False)
    guanya(graella, False)
    if len(disponibles) >0:
        ordinador= random.randrange(0,len(disponibles))
        posicio_ordinador=disponibles[int(ordinador)]
        disponibles.pop(int(ordinador))
    graella=llistagraella(graella,int(posicio_ordinador), True)
    guanya(graella, True)
imprimir(graella)
print("EMPAT")