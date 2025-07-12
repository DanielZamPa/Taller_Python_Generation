#EJERCICIO 11
def area_triangulo(base, altura):
    return (base * altura) / 2

base = int(input("ingrese el valor de la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))

print("El area es: ", area_triangulo(base,altura))

#EJERCICIO 12
def imprimir_mayor(num1, num2, num3):
    mayor = max(num1, num2, num3)
    print(f"El número mayor es: {mayor}")

imprimir_mayor(100, 25, 7)
#EJERCICIO 13
def contar_palabras(cadena):    
    palabras = cadena.split()
    return len(palabras)
texto = str(input("Ingrese la texto a evaluar: "))
print(f"El texto contiene {contar_palabras(texto)} palabras.")

#EJERCICIO 14
listaNum = [1,34,52,46]
def sumaLista(listaNum):
    return sum(listaNum)
print("Resultado: ",sumaLista(listaNum))

#EJERCICIO 15
cadena = str(input("Ingrese su palabra: "))
cadena_invertida = ''.join(reversed(cadena))
if cadena==cadena_invertida:
    print("La palabra es un palindromo.")
else:
    print("La palabra no es un palindromo.")
