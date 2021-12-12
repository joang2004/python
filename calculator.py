import math
def menu():
    print("En aquest progrma podras fer diversos calculs:")
    print("1.Pasar de Celsius cap a Fahrenheit")
    print("2.Calcul de volums")
    print("3.Calcul d'arees")
    print("4.Sortir del programa")

    entrada=input("Introduiex introdueix un del nombres per anar en aquell apartat: ")

    while entrada != "4" :
        if entrada == "1" :
            temperatura()
        if entrada == "2" :
            volums()
        if entrada == "3":
            arees()
        else:
            entrada=str(input("Introdueix una opció correcta: "))
    
    print("Has sortit del programa")
    exit()

def nombre_valid_negatiu(x): #S'utilitza en es calcul de temperatura per saber si és una temperatura posible
    x=x.replace(".", ",") 
    comes=x.count(",")
    guions=x.count("-")
    posicio_guions=x.find("-")
    posicio_comes=x.find(",")

    if comes > 1 or guions > 1 or posicio_comes == 0 or posicio_guions != 0 and posicio_guions != -1 :
        return False
    else:
        resultat=x.replace("-", "")
        nombre=resultat.replace(",", "")
        return nombre.isnumeric()

def nombre_valid_positiu(x): #S'utilitza en per saber si una longitud es valida
    x=x.replace(".", ",") 
    comes=x.count(",")
    guions=x.count("-")
    posicio_comes=x.find(",")

    if comes > 1 or guions > 0 or posicio_comes == 0:
        return False
    else:
        resultat=x.replace("-", "")
        nombre=resultat.replace(",", "")
        return nombre.isnumeric()

def temperatura():
    print("")
    print("CALCUL DE TEMPERATURES")
    print("")
    print("En aquest apartat podras pasar temperatures de Celsius cap a Fahrenheit")
    seguir = "Y"
    
    while seguir == "Y":
        print("")
        celsius=input("Introdueix una temperatura (nombre enter) en graus Celsius: ")
        es_valid = nombre_valid_negatiu(celsius)
        
        while es_valid == False :
            print("")
            celsius=input("Introdueix un nombre senser: ")
            es_valid=nombre_valid_negatiu(celsius)

        fahrenheit= (int(celsius)*( 9 / 5)) + 32
        print("La temperatura en Fahrenheit és: " + str(fahrenheit))
        print("")
        seguir=input("Vols fer una altre conversió? Y/N: ")
    
    menu()

def volums():
    print("")
    print("CALCULS DE VOLUMS")
    print("")
    
    print("En aquest apartat podras calcular els volums de diverses figures:")
    print("  1.Volumen d'un con")
    print("  2.Volumen d'una esfera")
    print("  3.Sortir cap el menu")
    
    print("")
    opcio=input("Introdueix la teva opció: ")
    
    while opció != "3":
        if opcio == "1":
            print("")
            con()
        if opcio == "2":
            print("")
            esfera()
        else:
            opcio=input("Introdueix una opció correcte: ")
    
    menu()

def con():
    print("")
    print("VOLUM DEL CON")
    seguir="Y"
    while seguir == "Y":
        print("")
        radi=input("Introdueix el radi de la base: ")
        es_radi = nombre_valid_positiu(radi)

        while es_radi == False :
            print("")
            radi = input("Introdueix una longitud vàlida: ")
            es_radi = nombre_valid_positiu(radi)
    
        altura=input("Introdueix l'altura del con: ")
        es_altura = nombre_valid_positiu(altura)
        
        while es_altura == False :
            print("")
            altura = input("Introdueix una longitud vàlida: ")
            es_altura = nombre_valid_positiu(altura)
        
        print("")
        volum = (math.pi*math.pow(float(radi), 2)*float(altura))/3
        print(" El volum del con és: " + str(volum) + " unitats^3." )
        
        print("")
        seguir=str(input("Vols calcular el volum d'un altre con? Y/N: "))
    
    volums()

def esfera():
    print("")
    print( "Volum d'una esfera")
    seguir="Y"
    while seguir == "Y":
        radi=input("Introdueix el radi de la esfera: ")
        es_radi = nombre_valid_positiu(radi)
        while es_radi == False :
            print("")
            radi = input("Introdueix una longitud vàlida: ")
            es_radi = nombre_valid_positiu(radi)

        volum = (4*math.pi*pow(float(radi), 3))/3
        print(" El volum de la esfera és: " + str(volum) + " unitats^3." )
        print("")
        seguir=str(input("Vols calcular el volum d'una altra esfera? Y/N: "))
    volums()

def arees():
    print("")
    print("Calcul d'arees:")
    print("1.Area d'un trapezoide")
    print("2.Area d'un cercle")
    print("3.Area d'una elipse")
    print("4.Area d'un triangle equilater")
    print("5.Area de qualsevol triangle")
    print("6.Sortir al menu")
    print("")
    opcio=str(input("Introdueix l'opció desitjada: "))
    while opcio != "6":
        if opcio == "1":
            print("")
            trapezoide()
        if opcio == "2":
            print("")
            cercle()
        if opcio == "3":
            print("")
            elipse()
        if opcio == "4":
            print("")
            triangle_equilater()
        if opcio == "5":
            print("")
            triangle()
        else:
            opcio=input("Introdueix una opció vàlida: ")
    menu()

def trapezoide():
    print("")
    print("CALCUL DE L'AREA D'UN TRAPEZOIDE")
    seguir="Y"
    while seguir == "Y":
        print("")
        altura=input("Introdueix l'altura del trapezoide: ")
        es_altura = nombre_valid_positiu(altura)

        while es_altura == False :
            print("")
            altura = input("Introdueix una longitud vàlida: ")
            es_altura = nombre_valid_positiu(altura)

        base_menor=input("Introdueix la longitud de la base menor: ")
        es_base_menor = nombre_valid_positiu(base_menor)

        while es_base_menor == False:
            print("")
            base_menor = input("Introdueix una longitud vàlida: ")
            es_base_menor = nombre_valid_positiu(base_menor)
        
        base_major=input("Introdueix la longitud de la base major: ")
        es_base_major = nombre_valid_positiu(base_major)

        while es_base_major == False:
            print("")
            base_major = input("Introdueix una longitud vàlida: ")
            es_base_major = nombre_valid_positiu(base_major)

        area= 0.5*(float(base_major)+float(base_menor))*float(altura)
        print("L'area del trapezoide és " + str(area) + " unitat^2.")
        print("")
        seguir=str(input("Vols calcular l'area d'una altre trapezoide? Y/N: "))
    arees()

def cercle():
    print("CALCUL D'AREA DEL CERCLE")
    seguir = "Y"
    while seguir == "Y":
        print("")
        radi=input("Introdueix el radi de l'esfera: ")
        es_radi = nombre_valid_positiu(radi)

        while es_radi == False:
            print("")
            radi=input("Introdueix una longitud vàlida: ")
            es_radi = nombre_valid_positiu(radi)
        
        area = math.pi*math.pow(float(radi), 2)
        print("L'area de la circunferencia és: " + str(area) + " unitats^2.")
        seguir= input("Vols calcular l'area d'un altre cercle? Y/N: ")
    arees()

def elipse():
    print("")
    print("CALCUL DE L'AREA D'UNA ELIPSE")
    seguir="Y"

    while seguir == "Y":
        print()
        radi_menor=input("Introdueix el radi menor de l'elipse: ")
        es_radi_menor = nombre_valid_positiu(radi_menor)

        while es_radi_menor == False:
            print("")
            radi_menor=input("Introdueix una longitud vàlida: ")
            es_radi_menor = nombre_valid_positiu(radi_menor)

        radi_major=input("Introdueix el radi major de l'elipse: ")
        es_radi_major = nombre_valid_positiu(radi_major)

        while es_radi_major == False:
            print("")
            radi_major=input("Introdueix una longitud vàlida: ")
            es_radi_major = nombre_valid_positiu(radi_major)
        
        area=math.pi*float(radi_menor)*float(radi_major)
        print("L'area de l'elipse és: " + str(area) + " unitats^2.")

        seguir= input("Vols calcular l'area d'un altre elipse? Y/N: ")
    arees()

def triangle_equilater():
    print("CALCUL D'AREES DE TRIANGRLES EQUILATERS")
    seguir = "Y"

    while seguir == "Y":
        print("")
        altura = input("Introdueix l'altura del triangle: ")
        es_altura = nombre_valid_positiu(altura)

        while es_altura == False:
            print()
            altura=input("Introdueix una longitud vàlida: ")
            es_altura = nombre_valid_positiu(altura)
        
        area= (math.pow(float(altura), 2)*math.pow( 3, 0.5))/3
        print("L'area del triangle és : " + str(area) + " unitats^2.")
        print("")
        seguir=input("Vols calcular l'area d'un altre triangle equilater? Y/N : ")
    
    arees()

def triangle():
    print("")
    print("CALCUL DE AREES DE TRIANGLES")
    seguir = "Y"

    while seguir == "Y":
        print("")
        costat1=input("Introdueix la longitud d'un costat: ")
        es_costat1=nombre_valid_positiu(costat1)

        while es_costat1 == False:
            print("")
            costat1=input("Introdueix una longitud vàlida: ")
            es_costat1=nombre_valid_positiu(costat1)
        
        costat2=input("Introdueix la longitud d'un segon costat: ")
        es_costat2=nombre_valid_positiu(costat2)

        while es_costat2 == False:
            print("")
            costat2=input("Introdueix un valor vàlid: ")
            es_costat2=nombre_valid_positiu(costat2)
        
        angle=input("Introdueix l'angle que formen els dos costats en graus: ")
        es_angle=nombre_valid_positiu(angle)

        while es_angle == False:
            print("")
            angle=input("Introdueix un angle vàlid")
            es_angle=nombre_valid_positiu(angle)
        
        area=0.5*float(costat2)*float(costat1)*math.sin(float(angle))
        print("L'area del triangle és: " + str(area) + " unidads^2. ")

        seguir=input("Vols calcular una altra area d'un triangle? Y/N: ")
    
    arees()




menu()