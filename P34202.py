from PIL import Image, ImageDraw
from easyinput import read

f = read(str)
t = read(str)
n = read(int) #amplada
m = read(int) #alçada


if m>(n+1)/2:
    img= Image.new("RGB", (n,m), f)

    dib = ImageDraw.Draw(img)

    dib.polygon([(0,0), (n/2,(n+1)/2) ,(n,0)], t)

    img.save("output.png")
else:
    print("Introdueix una amplada i altura correcta")
