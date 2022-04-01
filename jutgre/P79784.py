from easyinput import read
x = 0
y = 0
l =read(chr)
while l is not None :
    if (l == "n"):
        y -= 1
    if (l == "s"):
        y += 1
    if (l == "e"):
        x += 1
    if (l == "w"):
        x -= 1
    l = read(chr)


print( "(" + str(x) + ", " + str(y) + ")")