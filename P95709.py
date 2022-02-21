from PIL import Image, ImageDraw
from easyinput import read
f =read(str)
c = read(str)
b =read(int)
a =read(int)
x =read(int)

img=Image.new("RGB", (b,a), f)
dib =ImageDraw.Draw(img)
dib.polygon([(0,a),(x,0),(b,a)],c)

img.save("output.png")