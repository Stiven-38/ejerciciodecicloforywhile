n = int(input("Ingrese la suma de todos los números impares : "))
suma_impares = 0
num_impares = 0

for i in range(1, n+1, 2):
    suma_impares += i
    num_impares += 1

print("La suma de todos los números impares desde 1 hasta", n, "es:", suma_impares)
print("Hay", num_impares, "números impares desde 1 hasta", n)