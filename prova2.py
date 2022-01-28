
class Llibre:
    def __init__(self):
        self.__titol = None
        self.__editorial = None
        self.__anypublicacio = None
        self.__nompagines = None
    def setTitol(self, titol):
        self.__titol = titol
    
    def setEditorial(self, editorial):
        self.__editorial = editorial

    def setAnyPublicacio(self, anypublicacio):
        self.__anypublicacio = anypublicacio

    def setNomPagines (self, nompagines):
        self.__nompagines = nompagines
    
    def getTitol(self):
        return self.__titol
    
    def getEditorial(self):
        return self.__editorial
    
    def getAnyPublicacio(self):
        return self.__anypublicacio
    
    def getNomPagines(self):
        return self.__anypublicacio

    def mostraInfo(self):
        print("El llibre " + self.__titol + " de la editorial fou publicat per la editorial " + self.__editorial + " fou publicat l'any " + str(self.__anypublicacio) + " i té " + str
        (self.__nompagines) + " pàgines")

def carllibre():
    llibre1 = Llibre()
    llibre1.setTitol("La història natural de les paraules")
    llibre1.setEditorial("Vicens Vives")
    llibre1.setAnyPublicacio(1994)
    llibre1.setNomPagines(124)


    llibre2 = Llibre()
    llibre2.setTitol("El camino de los reyes")
    llibre2.setEditorial("El Mundo")
    llibre2.setAnyPublicacio(2010)
    llibre2.setNomPagines(1233)
    
    llibre1.mostraInfo()
    llibre2.mostraInfo()


carllibre()