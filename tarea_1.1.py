#Estructura principal

n = int(input("ingrese un numero para tamano de la piramide:"))

x = n
for i in range(n):
  for j in range(x):
      print("*", end="")
  x-=1
  print("")