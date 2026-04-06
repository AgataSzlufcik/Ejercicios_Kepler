def limpiar_datos(ventas):
    """Elimina valores negativos o None"""
    return [v for v in ventas if v is not None and v > 0]


def calcular_estadisticas(ventas):
    """Devuelve dict con total, promedio, max, min"""
    total = sum(ventas)
    promedio = total / len(ventas) if ventas else 0
    return {
        "total": total,
        "promedio": promedio,
        "max": max(ventas) if ventas else 0,
        "min": min(ventas) if ventas else 0
    }


def clasificar_ventas(ventas, umbral_bajo, umbral_alto):
    """Devuelve dict con ventas bajas, medias, altas"""
    bajas = [v for v in ventas if v < umbral_bajo]
    medias = [v for v in ventas if umbral_bajo <= v < umbral_alto]
    altas = [v for v in ventas if v >= umbral_alto]

    return {
        "bajas": bajas,
        "medias": medias,
        "altas": altas
    }


def generar_reporte(ventas):
    """Usa las funciones anteriores y muestra reporte completo"""
    
    ventas_limpias = limpiar_datos(ventas)
    eliminadas = len(ventas) - len(ventas_limpias)

    stats = calcular_estadisticas(ventas_limpias)
    clasificacion = clasificar_ventas(ventas_limpias, 2000, 4000)

    total_ventas = len(ventas_limpias)

    def porcentaje(cantidad):
        return (cantidad / total_ventas * 100) if total_ventas else 0

    print("=== REPORTE DE VENTAS ===\n")

    print(f"Datos procesados: {total_ventas} ventas válidas ({eliminadas} inválidas eliminadas)\n")

    print("Estadísticas:")
    print(f"  Total: {stats['total']}")
    print(f"  Promedio: {round(stats['promedio'], 2)}")
    print(f"  Máximo: {stats['max']}")
    print(f"  Mínimo: {stats['min']}\n")

    print("Clasificación:")
    print(f"  Ventas bajas (< 2000): {len(clasificacion['bajas'])} ({round(porcentaje(len(clasificacion['bajas'])), 1)}%)")
    print(f"  Ventas medias: {len(clasificacion['medias'])} ({round(porcentaje(len(clasificacion['medias'])), 1)}%)")
    print(f"  Ventas altas (>= 4000): {len(clasificacion['altas'])} ({round(porcentaje(len(clasificacion['altas'])), 1)}%)")


# Datos de prueba
ventas_brutas = [1500, -200, 2500, None, 3000, 0, 4500, -100, 2800, 5000]

generar_reporte(ventas_brutas)