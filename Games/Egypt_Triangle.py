from math import acos, degrees

lados = input("Introduca los lados del triangulo").split(" ")

A = lados[0]=int(lados[0])
B = lados[1]=int(lados[1])
C = lados[2]=int(lados[2])

ang1 = degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
ang2 = degrees(acos((B * B + C * C - A * A)/(2.0 * B * C)))
ang3 = degrees(acos((C * C + A * A - B * B)/(2.0 * C * A)))

if ang1 > 90 or ang2 > 90 or ang3 > 90:
  print("wrong")
else:
  print("right")
