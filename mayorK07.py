#coding: utf­8
min = int(input("Escriba un número: "))
max = int(input("Escriba un número mayor que " + str(min) + ": "))
while min >= max:
    max = int(input(str(max) + " no es mayor que " + str(min) + ".Inténtelo de nuevo: "))

num = float(input("Escriba un número entre " + str(min) + " y " + str(max) + ": "))
contador = 0

while min <= num <= max:
    contador += 1
    num = float(input("Escriba un número entre " + str(min) + " y " + str(max) + ": "))

print()
if contador == 0:
    print("No ha escrito ningún número entre", min, "y", str(max) + ".")
elif contador == 1:
    print("Ha escrito 1 número entre", min, "y", str(max) + ".")
else:
    print("Ha escrito", contador, "números entre", min, "y", str(max) + ".")
print("Programa terminado")
