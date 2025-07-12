#Ejercicio 16
N = int(input("Ingresa un numero: "))
def NnumerosFibonacci(N):
    fibo = [0,1]
    for i in range (1, N+1):
        fibo.append(fibo[i-1]+fibo[i])
    return fibo
print(NnumerosFibonacci(N))
#Ejercicio 17
cadena = str(input("Ingrese su palabra: "))
cadena_invertida = ''.join(reversed(cadena))
print(cadena_invertida)