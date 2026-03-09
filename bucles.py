# Días de préstamo de varios libros
dias_prestamo = [15, 22, 18, 30, 12, 25]
limite = 21

prestamos_a_tiempo = 0
prestamos_retraso = 0
total_dias_retraso = 0

for dias in dias_prestamo:
    if dias <= limite:
        prestamos_a_tiempo += 1  # Equivale a: prestamos_a_tiempo = prestamos_a_tiempo + 1
    else:
        prestamos_retraso += 1
        dias_extra = dias - limite
        total_dias_retraso += dias_extra

# Mostrar resultados
print(f"Total de préstamos: {len(dias_prestamo)}")
print(f"Préstamos a tiempo: {prestamos_a_tiempo}")
print(f"Préstamos con retraso: {prestamos_retraso}")
print(f"Total días de retraso: {total_dias_retraso}")

# Calcular promedio de retraso
if prestamos_retraso > 0:
    promedio_retraso = total_dias_retraso / prestamos_retraso
    print(f"Promedio de días de retraso: {promedio_retraso:.2f}")


""" ¿for o while?
Usa for cuando sabes cuántas veces vas a iterar (lista, rango definido)
Usa while cuando la condición de parada depende de algo que cambia durante la ejecución
En análisis de datos, for es mucho más común."""