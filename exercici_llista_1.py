valors= [1,4,1,4,1,4]
ordenat=valors.copy()
#for i in valors:
#    ordenat.append(i)
ordenat.sort()
maxim=ordenat[-1]
minim=ordenat[1]
variat=0
baixat = True
for i in valors:
    print(i)

    if baixat == True and i > 3:
        print("puja")
        variat +=1
        baixat = False
    
    if i < 3:
        print("baix")
        baixat = True

print("Màxim: " +str(maxim))
print("Mínim: " + str(minim))
print("Variat: " + str(variat))