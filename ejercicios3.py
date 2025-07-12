#EJERCICIO 11
def area_triangulo(base, altura):
    return (base * altura) / 2

base = int(input("ingrese el valor de la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))

print("El area es: ", area_triangulo(base,altura))