#coding: utf­8

num1 = int(input("Escribe un número: "))

i=0
suma=0

while (i<num1):
	aux= int(input("Escribe un número: "))
	if (aux>0):
		i+=1
		suma=suma+num1
	
print "Has escrito", str(num1) +",", str(i) + " de ellos positivos."

