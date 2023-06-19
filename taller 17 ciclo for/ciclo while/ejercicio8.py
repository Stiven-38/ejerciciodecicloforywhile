numero = 0

while numero <= 0:
    numero = int(input("Ingrese un número  mayor que cero: "))

print(f"Los divisores de {numero} son:")

for i in range(1, numero+1):
    if numero % i == 0:
        print(i)
