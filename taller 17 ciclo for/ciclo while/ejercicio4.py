num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while num1 >= num2:
    print("El primer número debe ser menor que el segundo.")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

print(f"Los números entre {num1} y {num2} son:")
i = num1
while i <= num2:
    print(i)
    i += 1
