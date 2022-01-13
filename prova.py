fila = 0
linea= []
j_possible=None
valors=[]
def linea_possible(valor, possible):# SERCA I CLASIFICA ELS POSSIBLES ERRORS D'UNA LÍNEA
    nombres= ["1","2","3","4","5","6","7","8","9"]
    possible = None
    for i in valor:
        try:
            nombres.index(i)
        except:
            print("El valor " + str(i) + " no és vàlid" )
            return False
    for i in range( 1,10 ) :
        try:
            valor.index(str(i))
        except:
            print("Falta el valor " + str(i))
            return False
    if possible==None:
        print("Linea vàlida")
        return True

def comprova_columna(valors): #COMPROVA QUE CADA LÍNEA DE LA 
    base=0
    while base<9:#Marca la columna
        mult_a=0
        mult_b=0
        while mult_a <8:#marca la linea de la primera posició
            pos_a=9*mult_a+base
            while mult_b< 9:#marca la posició de la segona posició
                pos_b=9+base+9*mult_b
                try:
                    if valors[pos_a] == valors[pos_b]:
                        linea_a=int((pos_a+1)/9)
                        columna_a=(pos_a+1)%9
                        linea_b=int((pos_b+1)/9)
                        columna_b=(pos_b+1)%9
                        print("El valor " + valors[pos_a] + " és repeteix en (" + str(columna_a) + "," + str(linea_a) + ") i en (" + str(columna_b) + ", " + str(linea_b) + ")")
                        return False
                
                except:
                    pass
                mult_b+=1
            mult_a+=1
        base+=1


while fila < 9 :

    while j_possible != True:
        for i in range(9):
            x = input("Nombre: ")
            linea.append(x)
        j_possible=linea_possible(linea,j_possible)
        if j_possible== False:
            linea.clear()
    for i in linea:
        valors.append(i)
    linea.clear()
    if fila !=0:
        j_possible=comprova_columna(valors)
    if j_possible != False:
        fila +=1
        j_possible=None
    else:
        print("Fila invàlida")
    
