""" 
def analizar_prestamo(dias, categoria, limite_normal=21):
    """
    Analiza un préstamo y calcula penalización.
    
    Args:
        dias (int): Días del préstamo
        categoria (str): Tipo de material ("libro", "revista", "dvd")
        limite_normal (int): Límite de días para préstamos normales
    
    Returns:
        dict: Información del análisis
    """
    # Ajustar límite según categoría
    if categoria == "revista":
        limite = limite_normal - 7
    elif categoria == "dvd":
        limite = limite_normal - 14
    else:
        limite = limite_normal
    
    # Calcular retraso
    if dias <= limite:
        retraso = 0
        estado = "A tiempo"
        penalizacion = 0
    else:
        retraso = dias - limite
        estado = "Retrasado"
        penalizacion = retraso * 0.50
    
    return {
        'estado': estado,
        'dias': dias,
        'limite': limite,
        'retraso': retraso,
        'penalizacion': penalizacion
    }

# Probar la función
resultado = analizar_prestamo(25, "libro")
print(f"Estado: {resultado['estado']}")
print(f"Días de retraso: {resultado['retraso']}")
print(f"Penalización: {resultado['penalizacion']}€")

# Probar con revista
resultado2 = analizar_prestamo(20, "revista")
print(f"\nRevista - Estado: {resultado2['estado']}")
print(f"Días de retraso: {resultado2['retraso']}") """