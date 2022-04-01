from PIL import Image, ImageDraw
x=int(input("x:"))
y=int(input("y:"))
r=int(input("r:"))
image = Image.new("RGB", (8*r,8*r), "White")
draw = ImageDraw.Draw(image)
leftUpPoint = (r, y-r)
rightDownPoint = (x+r, y+r)
twoPointList = [leftUpPoint, rightDownPoint]
draw.ellipse(twoPointList, fill=(8*r,0,0,8*r))

image.save("output.png")
