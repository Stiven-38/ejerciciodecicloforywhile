n = int(input("Cuántas temperaturas quieres ingresar "))

temperaturas = []

for i in range(n):
    temperatura = float(input(f"Ingrese la temperatura {i+1}: "))
    temperaturas.append(temperatura)

maxima = max(temperaturas)
minima = min(temperaturas)
promedio = sum(temperaturas) / n

print(f"La temperatura más alta es: {maxima}")
print(f"La temperatura más baja es: {minima}")
print(f"La temperatura promedio es: {promedio:.2f}")