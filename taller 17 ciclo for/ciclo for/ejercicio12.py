n = int(input("Cuántos estudiantes quieres evaluar"))
notas_por_estudiante = 4

notas = []

for i in range(n):
    print(f"Notas del estudiante {i+1}:")
    suma_notas = 0
    for j in range(notas_por_estudiante):
        nota = float(input(f"Nota {j+1}: "))
        suma_notas += nota
        notas.append(nota)
    promedio = suma_notas / notas_por_estudiante
    print(f"Promedio del estudiante {i+1}: {promedio:.2f}")

maxima = max(notas)
minima = min(notas)
promedio_general = sum(notas) / (n * notas_por_estudiante)

print(f"La nota más alta es: {maxima}")
print(f"La nota más baja es: {minima}")
print(f"El promedio general es: {promedio_general:.2f}")

