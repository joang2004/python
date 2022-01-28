class Gato():
    def __init__(self):
        self.__nom = ""
        self.__color = ""
        self.__pes = ""
    

    def setNom(self, nom):
        self.__nom = nom
    def setColor(self, color):
        self.__color = color
    def setPes(self, pes):
        self.__pes = pes
    def getNom(self):
        return self.__nom
    def getColor(self):
        return self.__color
    def getPes(self):
        return self.__pes
    def maulla(self):
        print("-Miau- dice " + self.__nom)
   

moix = Gato()

moix.setNom(input("Introdueix el nom del moix: "))

moix.maulla()