from PIL import Image
color= input()
img = Image.new("RGB" ,(500 , 500), str(color))
img.save("output.png")