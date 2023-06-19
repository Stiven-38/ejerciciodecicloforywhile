numero = int(input("Introduce un número: "))
suma = 0

for i in range(numero+1):
    if i % 2 == 0:
        suma += i

print("La suma de los números pares hasta", numero, "es:", suma)