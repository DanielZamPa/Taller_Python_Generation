#EJERCICIO 1, Suma de dos numeros
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print("El resultado de la suma es: ", num1+num2)

#EJERCICIO 2
num1 = int(input("Ingrese un numero: "))
if (num1%2==0):
    print("El numero es par")
elif (num1%2!=0):
    print("El numero es impar")
else:
    print("Error")

#EJERCICIO 3
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
num3 = input("Ingrese el trecer numero: ")

if (num1>num2 and num1>num3):
    print("El numero mayor es: ",num1)
elif(num2>num1 and num2>num3):
    print("El numero mayor es: ",num2)
elif (num3>num1 and num3>num2):
    print("El numero mayor es: ",num3)
else:
    print("Los 3 numeros son iguales.")

#EJERCICIO 4
num = int(input("Ingrese un numero: "))

for c in range (1,11):
    print(num, "*",c," = ",num*c)

#EJERCICIO 5
ingreso = str(input("Ingresa una palabra: "))
vocales = "aeiouAEIOU"
contador = sum(1 for letra in ingreso if letra in vocales)   
print("Cantidad de vocales: ", contador) 
