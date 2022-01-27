paraula = str(input("Intrdueix una paraula o un oració per saber si és capicua: "))

lletra=[]
invertit=[]
capicua= True
for i in paraula:
    lletra.append(i)
try:
    lletra.remove(" ")
except:
    pass 
invertit=lletra.copy()
invertit.reverse()
for i in range(len(lletra)):
    if lletra[i] != invertit[i]:
        capicua=False
if capicua==True:
    print("La paraula/oració és capicua")
else:
    print("La paraula/pració no és capicua")