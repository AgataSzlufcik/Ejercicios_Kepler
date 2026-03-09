""" Objetivo: Practicar listas, diccionarios y bucles

Enunciado
Tienes una lista de libros prestados con su categoría y días de préstamo:

prestamos = [
    {"titulo": "1984", "categoria": "Ficción", "dias": 15},
    {"titulo": "Sapiens", "categoria": "Ensayo", "dias": 22},
    {"titulo": "Watchmen", "categoria": "Cómic", "dias": 18},
    {"titulo": "El Quijote", "categoria": "Ficción", "dias": 30},
    {"titulo": "Breve historia", "categoria": "Ensayo", "dias": 25},
    {"titulo": "Batman", "categoria": "Cómic", "dias": 12}
]
Escribe un programa que:

Agrupe los préstamos por categoría
Calcule el promedio de días por categoría
Identifique la categoría más prestada
Muestre libros con más de 20 días
Pistas
Crea un diccionario para agrupar por categoría
Usa un bucle para iterar sobre los préstamos
Para cada categoría, guarda una lista de días
Calcula promedios usando sum() y len()
"""