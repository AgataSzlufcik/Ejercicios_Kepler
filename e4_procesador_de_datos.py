"""Objetivo: Integrar todo (funciones, estructuras, validación)

Enunciado
Crea un sistema que procese datos de ventas con las siguientes funciones:

def limpiar_datos(ventas):
    """Elimina valores negativos o None"""
    pass

def calcular_estadisticas(ventas):
    """Devuelve dict con total, promedio, max, min"""
    pass

def clasificar_ventas(ventas, umbral_bajo, umbral_alto):
    """Devuelve dict con ventas bajas, medias, altas"""
    pass

def generar_reporte(ventas):
    """Usa las funciones anteriores y muestra reporte completo"""
    pass
Datos de prueba (con valores inválidos):

ventas_brutas = [1500, -200, 2500, None, 3000, 0, 4500, -100, 2800, 5000]
Requerimientos
limpiar_datos: Filtrar valores válidos (> 0 y no None)
calcular_estadisticas: Total, promedio, máximo, mínimo
clasificar_ventas:
Baja: < umbral_bajo
Media: entre umbrales
Alta: >= umbral_alto
generar_reporte: Llamar todas las funciones y mostrar resultados formateados
Salida esperada (aproximada)
=== REPORTE DE VENTAS ===

Datos procesados: 7 ventas válidas (3 inválidas eliminadas)

Estadísticas:
  Total: 21800
  Promedio: 3114.29
  Máximo: 5000
  Mínimo: 1500

Clasificación:
  Ventas bajas (< 2000): 1 (14.3%)
  Ventas medias: 4 (57.1%)
  Ventas altas (>= 4000): 2 (28.6%) """
