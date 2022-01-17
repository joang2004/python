class Monstre():
    def __init__(self):
        self.__nom = None
        self.__resistencia = None
    def setNom(self, nom):
        self.__nom = nom
    def setResistencia(self, resistencia):
        self.__resistencia = resistencia
    def getNom(self):
        return self.__nom
    def getResistencia(self):
        return self._resistencia
    def reduir_resistencia(self, reduir):
        self.__resistencia = int(self.__resistencia)-int(reduir)
        if self.__resistencia <= 0 :
            print("Has vencut al monstre")

print("ey")
monstre=Monstre()
monstre.setResistencia(int(input("Introdueix la resistencia del monstre: ")))
monstre.reduir_resistencia(int(input("Introdueix la resistencia que vols llevar: ")))
    