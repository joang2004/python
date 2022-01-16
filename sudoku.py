"""""
1.Falta millorar s'output
2.Simplificar el sistema de buleanes per fer s'output de Vàlid/Invàlid
3.Arreglar el problema de que quan es detecta una falla en el 3x3 ho escriqui com ha fila valida (relacionat amb el punt 1 )
4.Especificar el que ha de fer l'usuari cada vegada que doni error (ouput diferenciat per cada error)

"""
fila = 0
linea= []
j_possible=None
q_possible =None
valors=[]

quadrat = True
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
        return True

def comprova_columna(valors): #COMPROVA QUE CADA LÍNEA DE LA 
    
    base=0
    
    while base<9:#Marca la columna
        
        mult_a=0
        
        while mult_a <8:#marca la linea de la primera posició
            
            mult_b=0
            pos_a=9*mult_a+base

            while mult_b< 9:#marca la posició de la segona posició
                
                pos_b=9+base+9*mult_b
                
                if pos_b > pos_a:
                    
                    try:
                        
                        if valors[pos_a] == valors[pos_b]:
                            
                            linea_a=int((pos_a+1)/9)
                            columna_a=(pos_a+1)%9
                            linea_b=int((pos_b+1)/9)
                            columna_b=(pos_b+1)%9
                            
                            print()
                            print("El valor " + valors[pos_a] + " és repeteix en (" + str(columna_a) + "," + str(linea_a) + ") i en (" + str(columna_b) + ", " + str(linea_b) + ")")
                            
                            return False
                
                    except:
                        pass
                
                mult_b+=1
            
            mult_a+=1
        
        base+=1

def comprova_quadrats(valors):
    
    base_q_i=0
    
    while base_q_i<3:
        
        base_q_j = 0

        while base_q_j<3:
            
            a_base_j = 0
        
            while a_base_j<3:

                a_base_i=0
            
                while a_base_i<3:

                    b_base_j=0
                
                    while b_base_j<3:

                        b_base_i =0
                    
                        while b_base_i <3:

                            pos_a=a_base_i+9*a_base_j+27*base_q_j+3*base_q_i
                            pos_b=b_base_i + 9*b_base_j+27*base_q_j+3*base_q_i
                            b_base_i +=1

                            if pos_b>pos_a and pos_b<len(valors) and valors[pos_a] == valors[pos_b]:

                                linea_a=int((pos_a+1)/9)
                                columna_a=(pos_a+1)%9
                                linea_b=int((pos_b+1)/9)
                                columna_b=(pos_b+1)%9

                                print()
                                print("El valor " + valors[pos_a] + " és repeteix en (" + str(columna_a) + "," + str(linea_a) + ") i en (" + str(columna_b) + ", " + str(linea_b) + "), perquè estan dintre del mateix 3x3.")

                                return False
                    
                        b_base_j +=1
                
                    a_base_i +=1
            
                a_base_j+=1
        
            base_q_j +=1
    
        base_q_i +=1


while fila < 9 :

    print("Fila: " + str(fila))

    while j_possible != True: #Input, comprova que els valors introduits partanyin ha [1,9]
        
        for i in range(9):

            x = input("Nombre: ")
            linea.append(x)
         
        j_possible=linea_possible(linea,j_possible)
        
        if j_possible== False:

            linea.clear()
            print()
    
    for i in linea: #Afageix els nombres a la llista principal, a més, buida la llista d'entrada

        valors.append(i)
        print()
        print(valors)
        print()

    linea.clear()    
    j_possible=comprova_columna(valors)

    if j_possible != False and fila in [2,5,8]:

        q_possible=comprova_quadrats(valors)

    if q_possible == False:

        for i in range(27):

            try:
                valors.pop(-1)
                print()
                print(valors)
                print()
            except:
                pass
            print(i)

        fila -=2
        q_possible =None
        quadrat = False

    
    if j_possible == False:

        print("Fila invalida")

        for i in range(9):

            valors.pop(-1)
    
    if j_possible != False and q_possible != False and quadrat == True:# Encas que es repetesqui qualque nombre dintre de la columna s'activa i obliga a l'usuari a tornà ha introduïr els nombress

        fila +=1
        j_possible=None
        q_possible = None

        print("Fila Vàlida")
    
    quadrat=True

print("Sudoku correcte")