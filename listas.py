# Datos de préstamos (días)
prestamos = [15, 22, 18, 30, 12, 25, 19, 28, 14, 35]
limite = 21

# Separar en dos listas
a_tiempo = []
con_retraso = []

for dias in prestamos:
    if dias <= limite:
        a_tiempo.append(dias)
    else:
        con_retraso.append(dias)

# Análisis
print(f"Total de préstamos: {len(prestamos)}")
print(f"A tiempo: {len(a_tiempo)} ({len(a_tiempo)/len(prestamos)*100:.1f}%)")
print(f"Con retraso: {len(con_retraso)} ({len(con_retraso)/len(prestamos)*100:.1f}%)")

if len(con_retraso) > 0:
    promedio_retraso = sum(con_retraso) / len(con_retraso)
    print(f"Promedio de días con retraso: {promedio_retraso:.1f}")
    print(f"Máximo retraso: {max(con_retraso)} días")
