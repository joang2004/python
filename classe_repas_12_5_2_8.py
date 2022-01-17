class Estrella():
    def __init__(self):
        print("ha nacido una estrella")

a = int(input("Introdueix el nombre d'estrelles: "))

for i in range(a):
    i = Estrella()