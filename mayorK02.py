#coding: utf­8

num1 = float(input("Escribe un número: "))
num2 = float(input("Escribe un número mayor que " + str(num1) + ": "))

while num2 <= num1:
    print(num2, "no es mayor que", str(num1) + ". Vuelve a intentarlo: ")
    num2 = float(input())

print("El pograma ha finalizado.")

