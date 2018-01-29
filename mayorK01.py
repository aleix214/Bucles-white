#coding: utf­8

num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe un número mayor que " + str(num1) + ": "))

while num2 <= num1:
    print(num2, "no es mayor que", str(num1) + ". Vuelve a intentarlo: ")
    num2 = int(input())

print("El pograma ha finalizado.")


