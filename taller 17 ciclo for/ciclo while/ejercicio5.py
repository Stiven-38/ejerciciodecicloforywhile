total = 0
venta = float(input("Ingrese el monto de la venta (0 para terminar): "))
while venta != 0:
    total += venta
    venta = float(input("Ingrese el monto de la venta (0 para terminar): "))

if total > 1000:
    descuento = total * 0.1
    total -= descuento

print("El total a pagar es:", total)