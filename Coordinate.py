
import math
import os

path = os.path.dirname(__file__) #os.path.realpath(__file__)
print(path)

rfile = "{0}/koordinat.txt".format(path)
wfile = "{0}/output.txt".format(path)


aralik1 = 20
aralik2 = 75

print("Araligi belirlemek icin birinci ve ikinci degerleri giriniz..\n")
aralik1 = int(input('Birinci deger:'))
aralik2 = int(input('ikinci deger:'))

readfile = open(rfile,"r")
writefile = open(wfile,"w")


myList = []

for line in readfile:
    words = line.split()
    myList.append(words)


sX = 0 #Dugumler bu dugum ile karsilastirilacak
sY = 0

sX = float(myList[0][1])
sY = float(myList[0][2])
writefile.write(str(myList[0][0]+"  "+myList[0][1]+"  "+myList[0][2]+"  "+myList[0][3])+"\n")

x = 0

for i in myList:
    dX = float(myList[x][1])
    dY = float(myList[x][2])

    mesafe = math.sqrt((sX-dX)**2+(sY-dY)**2)

    if mesafe >= aralik1 and mesafe < aralik2:

        #print("{0}  {1}  {2}  {3}").format(myList[x][0],myList[x][1],myList[x][2],myList[x][3])
        writefile.write(str(myList[x][0]+"  "+myList[x][1]+"  "+myList[x][2]+"  "+myList[x][3])+"\n")
        sX = float(myList[x][1])
        sY = float(myList[x][2])

    x = x+1

