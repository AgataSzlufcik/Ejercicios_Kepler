""" Objetivo: Practicar funciones, condicionales y listas

Enunciado
Crea una función que clasifique préstamos según días transcurridos:

0-21 días: "A tiempo"
22-30 días: "Retraso leve" (penalización: 0.50€/día extra)
Más de 30 días: "Retraso grave" (penalización: 1.00€/día extra)
Luego procesa una lista de préstamos y muestra estadísticas.

def clasificar_prestamo(dias):
    # Tu código aquí
    pass

# Datos de prueba
prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]

# Procesar y mostrar estadísticas
Pistas
La función debe devolver un diccionario con estado y penalizacion
Usa un bucle for para procesar la lista
Cuenta cuántos están en cada categoría
Calcula la penalización total """

prestamos_dias = [15, 22, 18, 35, 25, 12, 40, 19, 28, 33]
# una lista con los días que cada usuario tuvo el préstamo.

def clasificar_prestamo(dias):          # una función que recibe un número de días (dias).La función decidirá:si el prestamo está a tiemposi hay retraso, cuánto se paga de penalización
    if dias <=21:                       # ponemos condiciones
        return {
            "estado": "A tiempo",       #crear un diccionario
            "penalizacion": 0
            }
    elif dias >=22 and dias <=30:
        return {
            "estado": "Retraso leve", 
            "penalizacion": (dias-21)*0.50 
            }
    else:
        return {
            "estado": "Retraso grave", 
            "penalizacion": (dias-30)*1.00
            }
    

for dias in prestamos_dias:                #empieza un bucle for. El programa toma cada numero de la lista y lo guarda temporalmente en la variable dias.
    resultado = clasificar_prestamo(dias)  #se llama a la función que devuelve un diccionario que se guarda en resultado
    print(f"{dias} dias: {resultado["estado"]}. Penalización: {resultado["penalizacion"]} EUR")