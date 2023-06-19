n = int(input("Ingrese el numero: "))
suma = 0
impares = 0
i = 1

while i <= n:
    if i % 2 != 0:
        suma += i
        impares += 1
    i += 1

print(f"La suma de los {impares} números impares entre 1 y {n} es: {suma}")
