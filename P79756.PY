from PIL import Image, ImageDraw
from easyinput import read
r = read(int)
g = read(int)
b = read(int)
img= Image.new("RGB", (900,300), "White")
dib = ImageDraw.Draw(img)

dib.polygon([(0,0),(150,0),(150,300),(0,300)], (r,g,b))
dib.polygon([(150,0),(300,0),(300,300),(150,300)], (int((4*r)/5),int((4*g)/5),int((4*b)/5)))
dib.polygon([(300,0),(450,0),(450,300),(300,300)], (int((3*r)/5),int((3*g)/5),int((3*b)/5)))
dib.polygon([(450,0),(600,0),(600,300),(450,300)], (int((2*r)/5),int((2*g)/5),int((2*b)/5)))
dib.polygon([(600,0),(750,0),(750,300),(600,300)], (int((r)/5),int((g)/5),int((b)/5)))
dib.polygon([(750,0),(900,0),(900,300),(750,300)], (0,0,0))

img.save("output.png")