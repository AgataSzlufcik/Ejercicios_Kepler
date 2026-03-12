""" Objetivo: Practicar variables, operadores y condicionales

Enunciado
Tienes datos de ventas mensuales. Escribe un programa que:

Guarde las ventas de cada mes en variables
Calcule el total y el promedio
Identifique el mes con mayores ventas
Determine si se alcanzó la meta anual (50000)
# Datos
enero = 4500
febrero = 5200
marzo = 4800
# ... completa los demás meses

# Tu código aquí
Pistas
Usa variables para cada mes
total = enero + febrero + ...
promedio = total / 12
Usa if para comparar meses y encontrar el máximo
Compara total >= 50000 para la meta
"""
enero = 4500
febrero = 5200
marzo = 4800
abril = 3900
mayo = 5100
junio = 5200
julio = 4200
agosto = 6200
septiembre = 5100
octubre = 4900
noviembre = 3000
diciembre = 7300
# guardamos las ventas en variables. Cada variable representa el dinero vendido ese mes

total = enero + febrero + marzo + abril + mayo + junio + julio + agosto + septiembre + octubre + noviembre + diciembre
print(f"Total de ventas: {total}")
# sumamos ventas de todo el año y imprimimos - La f permite insertar variables dentro del texto.

promedio = total / 12
print(f"Promedio de ventas: {promedio}")
# calculamos el promedio de ventas por mes

mayor_venta = max(enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre)
print(f"Mes con mayores ventas: {mayor_venta}")
# max() es una función que encuentra el valor más alto.

if total > 50000:
    print("Meta alcanzada")
else: 
    print("No alcazamos la meta")
# ponemos la condicion: si las ventas totales son mayores que 50000 entonces...

