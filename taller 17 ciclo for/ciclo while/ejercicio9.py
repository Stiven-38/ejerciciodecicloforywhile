n = int(input("Ingrese el número de temperaturas: "))
temperaturas = []
suma = 0
i = 0

while i < n:
    temperatura = float(input(f"Ingrese la temperatura {i+1}: "))
    temperaturas.append(temperatura)
    suma += temperatura
    i += 1

promedio = suma / n
temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)

print(f"Temperatura más alta: {temperatura_maxima}")
print(f"Temperatura más baja: {temperatura_minima}")
print(f"Temperatura promedio: {promedio}")