#Estructura principal

n = int(input("ingrese un numero para tamano de la piramide:"))

x = 0
for i in range(n):
  x+=1
  for j in range(x):
      print("*", end="")
  print("")