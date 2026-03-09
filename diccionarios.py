# Datos de biblioteca
prestamos = [
    {"id": 1, "categoria": "Ficción", "dias": 15},
    {"id": 2, "categoria": "Ensayo", "dias": 22},
    {"id": 3, "categoria": "Ficción", "dias": 18},
    {"id": 4, "categoria": "Cómic", "dias": 30},
    {"id": 5, "categoria": "Ensayo", "dias": 25},
    {"id": 6, "categoria": "Ficción", "dias": 12}
]

# Agrupar por categoría
estadisticas = {}

for prestamo in prestamos:
    categoria = prestamo["categoria"]
    dias = prestamo["dias"]
    
    if categoria not in estadisticas:
        estadisticas[categoria] = {
            "total": 0,
            "suma_dias": 0,
            "max_dias": dias,
            "min_dias": dias
        }
    
    estadisticas[categoria]["total"] += 1
    estadisticas[categoria]["suma_dias"] += dias
    estadisticas[categoria]["max_dias"] = max(estadisticas[categoria]["max_dias"], dias)
    estadisticas[categoria]["min_dias"] = min(estadisticas[categoria]["min_dias"], dias)

# Mostrar resultados
for categoria, datos in estadisticas.items():
    promedio = datos["suma_dias"] / datos["total"]
    print(f"\n{categoria}:")
    print(f"  Total préstamos: {datos['total']}")
    print(f"  Promedio días: {promedio:.1f}")
    print(f"  Máximo: {datos['max_dias']} días")
    print(f"  Mínimo: {datos['min_dias']} días")