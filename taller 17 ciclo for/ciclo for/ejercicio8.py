n = int(input("Cuántas notas quieres ingresar "))

notas = []
for i in range(n):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / n

print(f"El promedio de las {n} notas ingresadas es: {promedio}")