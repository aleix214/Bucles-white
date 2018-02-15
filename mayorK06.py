#coding: utf­8

lim = float(input("Escriba el valor límite: "))
while lim <= 0:
    lim = float(input("El límite ha ser mayor que 0. Vuélve a ponerlo: "))

num = float(input("Escriba un número: "))
suma = 0
suma += num

while suma < limite:
    num = float(input("Escriba otro número: "))
    suma += num

print("Ha superado el límite. La suma de los números positivos introducidos es", str(suma) + ".")
print("Ha finalizado")
