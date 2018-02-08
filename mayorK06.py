#coding: utf­8

num1 = float(input("Escribe el límite: "))
suma=0

while num1>0:
	aux = float(input("Escribe otro: "))
	suma=aux+suma
	if (suma>num1):
		print "Ha superado el límite. La suma de los números introducidos es", str(suma) + "." 
		break

