from PIL import Image, ImageDraw
n = int(input("Amplada: "))
m =int(input("Alçada: "))   


img=Image.new("RGB", (n, 9*m), "Yellow")
dib=ImageDraw.Draw(img)

dib.rectangle([(0, m ), (n, 2*m)] ,fill="Red")
dib.rectangle([(0, 3*m ), (n, 4*m)] ,fill="Red")
dib.rectangle([(0, 5*m ), (n, 6*m)] ,fill="Red")
dib.rectangle([(0, 7*m ), (n, 8*m)] ,fill="Red")



img.save("output.png")