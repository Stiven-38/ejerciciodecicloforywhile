numero = int(input("Ingrese un número entero mayor que cero: "))

while numero <= 0:
    numero = int(input("El número debe ser mayor que cero. Ingrese otro número: "))

print(f"Los divisores de {numero} son:")

for i in range(1, numero+1):
    if numero % i == 0:
        print(i)