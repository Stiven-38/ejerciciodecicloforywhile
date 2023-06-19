n = int(input("Ingrese el número de notas: "))
notas = []
i = 0

while i < n:
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
    i += 1

promedio = sum(notas) / n

print(f"El promedio de las {n} notas es: {promedio}")
