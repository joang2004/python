import math
from operator import length_hint
from easyinput import read
x = read(int)
resultat = []
foateat=""
sortida=""
b = "{area:.6f}"
for i in range(x):
    figura = read(str)
    
    if figura == "rectangle":
        base = read(float)
        altura = read(float)
        area = base * altura
        formateat = b.format(area=area)
        if i < x - 1:
            sortida += str(formateat) + '\n'
        else:
            sortida += str(formateat)
    
    if figura == "circle":
        radi = read(float)
        area = math.pi * radi**2
        formateat = b.format(area=area)
        if i < x - 1:
            sortida += str(formateat) + '\n'
        else:
            sortida += str(formateat)
print(sortida)