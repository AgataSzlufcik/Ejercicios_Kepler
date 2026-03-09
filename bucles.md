## 🔁 Bucles: for y while
¿Qué son los bucles?
Los bucles te permiten repetir acciones sin escribir el mismo código mil veces.

Imagina que necesitas analizar las ventas de 365 días. ¿Vas a escribir 365 líneas de código? No. Usas un bucle.

El bucle for
El más común. Repite una acción para cada elemento de una secuencia:

# Iterar sobre una lista
ventas = [100, 150, 200, 175, 225]

for venta in ventas:
    print(f"Venta: {venta}")
Salida:

Venta: 100
Venta: 150
Venta: 200
Venta: 175
Venta: 225
Iterar sobre un rango
Si solo necesitas repetir N veces:

# Imprimir números del 0 al 4
for i in range(5):
    print(i)
# Imprimir números del 1 al 5
for i in range(1, 6):
    print(i)
# Imprimir números del 0 al 10 de 2 en 2
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10
Ejemplo con datos
precios = [19.99, 25.50, 15.00, 30.00]
total = 0

for precio in precios:
    total = total + precio

print(f"Total: {total}")  # 90.49
El bucle while
Repite mientras una condición sea verdadera:

contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador = contador + 1
Salida:

Contador: 0
Contador: 1
Contador: 2
Contador: 3
Contador: 4
Cuidado: Si la condición nunca se vuelve False, el bucle se ejecuta infinitamente.

Ejemplo con datos
saldo = 1000
gasto_mensual = 150
meses = 0

while saldo > 0:
    saldo = saldo - gasto_mensual
    meses = meses + 1
    print(f"Mes {meses}: Saldo restante = {saldo}")

print(f"El saldo se agotó en {meses} meses")
break y continue
break - detener el bucle
ventas = [100, 200, 0, 300, 400]

for venta in ventas:
    if venta == 0:
        print("Dato inválido encontrado. Deteniendo análisis.")
        break
    print(f"Venta: {venta}")
Salida:

Venta: 100
Venta: 200
Dato inválido encontrado. Deteniendo análisis.
continue - saltar a la siguiente iteración
ventas = [100, -50, 200, -30, 300]

for venta in ventas:
    if venta < 0:
        continue  # Saltar ventas negativas
    print(f"Venta válida: {venta}")
Salida:

Venta válida: 100
Venta válida: 200
Venta válida: 300
Bucles anidados
Un bucle dentro de otro:

productos = ["Laptop", "Mouse", "Teclado"]
tiendas = ["Tienda A", "Tienda B"]

for producto in productos:
    for tienda in tiendas:
        print(f"{producto} en {tienda}")
Salida:

Laptop en Tienda A
Laptop en Tienda B
Mouse en Tienda A
Mouse en Tienda B
Teclado en Tienda A
Teclado en Tienda B
Enumerar con índice
Si necesitas el índice además del valor:

categorias = ["Ficción", "Ensayo", "Cómic"]

for i, categoria in enumerate(categorias):
    print(f"{i}: {categoria}")
Salida:

0: Ficción
1: Ensayo
2: Cómic