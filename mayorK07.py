#coding: utf­8

num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe un número mayor que el anterior: "))

x=0

while (num1<num2):
	aux = int(input("Escribe el número: "))
	x=x+aux
	if (aux>num2) and (aux<num2):
		print "jeje"
