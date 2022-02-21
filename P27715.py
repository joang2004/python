from PIL import Image, ImageDraw
n=int(input())

img= Image.new("RGB", (3*n,3*n), "Beige")
dib = ImageDraw.Draw(img)

dib.polygon([(n,0),(2*n,0),(3*n,n),(3*n,2*n),(2*n,3*n),(n,3*n),(0,2*n),(0,n)], "Red")

img.save("output.png")