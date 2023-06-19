n = int(input("Ingrese el número de estudiantes: "))
notas = []
suma = 0
i = 0

while i < n:
    nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    notas.append(nota)
    suma += nota
    i += 1

promedio = suma / n
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
print(f"Promedio: {promedio}")
