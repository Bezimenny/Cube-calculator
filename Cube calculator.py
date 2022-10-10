from math import*

object = input("Object: ")
oweight = input(object + "'s weight in kg: ")
onumber = input(object + "s number: ")
oheight = input(object + "'s max height in meters: ")
olenght = input(object + "'s max length in meters: ")
owidth = input(object + "'s max width in meters: ")

dimention = (((float(oheight) + float(olenght) + float(owidth)) / 3) * float(onumber)) / 3
cside = (float(oheight) + float(olenght) + float(owidth)) / 3
area = pow(float(dimention), 3)
cweight = float(oweight) * float(onumber)

print("Cube made of " + str(onumber) + " " + str(object) + "s weights " + str(float(cweight)) + "kg, is " + str(float(cside)) + "m long, wide and tall and has an area of " + str(float(area)) + "m3")
