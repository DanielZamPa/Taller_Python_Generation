#EJERCICIO 6
num = int(input("Ingrese un numero: "))
contador = 0
while contador != num:
    contador=contador+1
    print(contador)
#EJERCICIO 7
num = int(input("Ingrese un numero: "))
resultado = 1
for c in range(1, num+1):
    resultado *= c
print("Resultado: ", resultado)

#EJERCICIO 8
resultado = []
for c in range (1,101):
    if(c%2==0):
        resultado.append(c)
        
print("Resultado: ", sum(resultado))

#EJERCICIO 9
import random
acierto = False
num = random.randint(1,10)
while acierto != True:
    intento = int(input("Adivina el numero: "))
    if (intento==num):
        print("¡ACERTASTE!")
        acierto=True
    else:
        if(intento<num):
            print("Muy bajo")
        elif(intento>num):
            print("Muy alto")

#EJERCICIO 10
num = int(input("Ingrese un numero: "))
contador = 0
acierto = False
for i in range (1, num+1):
    if(num%i==0):
        contador += 1
        if(contador > 2):            
            acierto=False
        else:
            acierto=True
if(acierto!=True):
    print("No es primo")   
else:
    print("Es primo")