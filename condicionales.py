# Datos de un préstamo en biblioteca
dias_prestamo = 35
limite_normal = 21
limite_extendido = 30

# Clasificar estado del préstamo
if dias_prestamo <= limite_normal:
    estado = "A tiempo"
    penalizacion = 0
elif dias_prestamo <= limite_extendido:
    dias_retraso = dias_prestamo - limite_normal
    estado = "Retraso leve"
    penalizacion = dias_retraso * 0.50
else:
    dias_retraso = dias_prestamo - limite_normal
    estado = "Retraso grave"
    penalizacion = dias_retraso * 1.00

print(f"Estado: {estado}")
print(f"Días de préstamo: {dias_prestamo}")
print(f"Penalización: {penalizacion}€")

#Modifica dias_prestamo con diferentes valores (10, 25, 35) y ve cómo cambia la salida.

