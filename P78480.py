from PIL  import Image, ImageDraw
n =int(input())
img= Image.new("RGB",(8*n,8*n), "White")
dib= ImageDraw.Draw(img)
dib.ellipse([0,0, 8*n, 8*n],"Blue" )
dib.ellipse([n,n, 7*n, 7*n],"Yellow")
dib.ellipse([2*n,2*n, 6*n, 6*n],"Red")
dib.ellipse([3*n,3*n, 5*n, 5*n],"Green")
img.save("output.png")