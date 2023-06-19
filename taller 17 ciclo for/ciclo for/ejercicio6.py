
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while num1 >= num2:
    print("El primer número debe ser menor que el segundo.")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

for i in range(num1, num2+1):
    print(i)