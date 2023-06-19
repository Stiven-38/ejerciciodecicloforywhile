n = int(input("Ingrese el número: "))
resultado = 0
i = 1

if n > 10:
    resultado = 1
    while i <= 10:
        resultado *= i
        i += 1
else:
    while i <= n:
        resultado += i
        i += 1

if n > 10:
    print("El número ingresado es mayor que 10. La multiplicación de los primeros 10 números es:", resultado)
else:
    print("El número ingresado es menor o igual que 10. La suma de los números desde 1 hasta", n, "es:", resultado)
