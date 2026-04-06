# Ejercicio 5: Mini proyecto integrador
# Objetivo: Crear un análisis completo desde cero

# Enunciado
# Crea un programa que simule el análisis de una biblioteca durante un mes.

# Datos a generar aleatoriamente (o puedes usar datos fijos):

""" 100 préstamos
Categorías: Ficción, Ensayo, Cómic, Poesía
Días de préstamo: entre 5 y 45 días
Análisis a realizar:

Por categoría:
    Cuántos préstamos
    Promedio de días
    Porcentaje del total

Por estado:
    A tiempo (≤ 21 días)
    Retraso leve (22-30 días)
    Retraso grave (> 30 días)

Penalizaciones:
    Total recaudado en penalizaciones
    Promedio por préstamo con retraso

Top 5:
    Préstamos más largos"""
import random

# Datos
categorias = ["Ficción", "Ensayo", "Cómic", "Poesía"]
prestamos = []

# Generar datos
for i in range(100):
    categoria = random.choice(categorias)
    dias = random.randint(5, 45)

    prestamo = {
        "categoria": categoria,
        "dias": dias
    }

    prestamos.append(prestamo)


# --- ANÁLISIS POR CATEGORÍA ---
print("=== ANÁLISIS POR CATEGORÍA ===")

for cat in categorias:
    total = 0
    suma_dias = 0

    for p in prestamos:
        if p["categoria"] == cat:
            total += 1
            suma_dias += p["dias"]

    if total > 0:
        promedio = suma_dias / total
    else:
        promedio = 0

    procentaje = (total / len(prestamos)) * 100

    print(cat, "- cantidad:", total,
          ", promedio:", round(promedio, 2),
          ", procentaje:", round(procentaje, 1), "%")


# --- ESTADOS ---
print("\n=== ESTADOS ===")

a_tiempo = 0
leve = 0
grave = 0

for p in prestamos:
    dias = p["dias"]

    if dias <= 21:
        a_tiempo += 1
    elif dias <= 30:
        leve += 1
    else:
        grave += 1

print("A tiempo:", a_tiempo)
print("Retraso leve:", leve)
print("Retraso grave:", grave)


# --- PENALIZACIONES ---
print("\n=== PENALIZACIONES ===")

total_penal = 0
contador_retrasos = 0

for p in prestamos:
    dias = p["dias"]

    if dias > 21:
        retraso = dias - 21
        penal = retraso * 0.5

        total_penal += penal
        contador_retrasos += 1

if contador_retrasos > 0:
    promedio_penal = total_penal / contador_retrasos
else:
    promedio_penal = 0

print("Total penalizaciones:", round(total_penal, 2))
print("Promedio por retraso:", round(promedio_penal, 2))


# --- TOP 5 ---
print("\n=== TOP 5 PRÉSTAMOS MÁS LARGOS ===")

# ordenar
top5 = []

for p in prestamos:
    top5.append(p)

for i in range(len(top5)):
    for j in range(len(top5) - 1):
        if top5[j]["dias"] < top5[j + 1]["dias"]:
            temp = top5[j]
            top5[j] = top5[j + 1]
            top5[j + 1] = temp

# coger los 5 primeros
print("\nTOP 5 PRÉSTAMOS MÁS LARGOS:")

contador = 1
for p in top5[:5]:
    print(contador, p["categoria"], p["dias"])
    contador = contador + 1