tabla = int(input("Qué tabla de multiplicar quieres ver "))

for i in range(11):
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")