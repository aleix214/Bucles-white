#coding: utf­8

num1 = int(input("Escriba un número: "))
num2 = int(input("Escriba un número mayor que el anterior: "))

while num2 > num1:
    num1 = num2
    num2 = int(input("Escriba un número mayor que el anterior: "))

print("No es mayor que", str(num1) + ".")
print("Programa terminado")
