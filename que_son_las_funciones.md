📦 ¿Qué son las funciones?
La idea básica
Una función es un bloque de código reutilizable que hace una tarea específica.

Es como una receta: defines los pasos una vez, y luego puedes usarla cuantas veces quieras.

Sin funciones:

# Calcular promedio de ventas de enero
ventas_enero = [100, 150, 200]
suma_enero = 0
for venta in ventas_enero:
    suma_enero += venta
promedio_enero = suma_enero / len(ventas_enero)
print(promedio_enero)

# Calcular promedio de ventas de febrero (copiar todo de nuevo)
ventas_febrero = [120, 180, 160]
suma_febrero = 0
for venta in ventas_febrero:
    suma_febrero += venta
promedio_febrero = suma_febrero / len(ventas_febrero)
print(promedio_febrero)
Con funciones:

def calcular_promedio(lista):
    suma = 0
    for valor in lista:
        suma += valor
    return suma / len(lista)

# Usar la función
print(calcular_promedio([100, 150, 200]))  # 150.0
print(calcular_promedio([120, 180, 160]))  # 153.33
Crear una función
Sintaxis:

def nombre_funcion():
    # código de la función
    print("Hola desde la función")
Llamar la función:

nombre_funcion()  # Ejecuta el código dentro
Funciones con parámetros
Puedes pasarle información a la función:

def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Ana")  # Hola, Ana
saludar("Carlos")  # Hola, Carlos
Múltiples parámetros:

def calcular_total(precio, cantidad):
    total = precio * cantidad
    print(f"Total: {total}")

calcular_total(25.50, 3)  # Total: 76.5
El return
Las funciones pueden devolver un valor:

def sumar(a, b):
    resultado = a + b
    return resultado

# Guardar el resultado en una variable
total = sumar(10, 5)
print(total)  # 15
Sin return, la función hace algo pero no devuelve nada (devuelve None).

Parámetros con valores por defecto
def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    return precio - descuento

print(calcular_descuento(100))  # 90.0 (usa 10% por defecto)
print(calcular_descuento(100, 20))  # 80.0 (usa 20%)
Ejemplo con datos: análisis de préstamos
def clasificar_prestamo(dias):
    """
    Clasifica un préstamo según los días transcurridos.
    
    Args:
        dias (int): Días del préstamo
    
    Returns:
        str: Clasificación del préstamo
    """
    if dias <= 21:
        return "A tiempo"
    elif dias <= 30:
        return "Retraso leve"
    else:
        return "Retraso grave"

# Usar la función
print(clasificar_prestamo(15))  # A tiempo
print(clasificar_prestamo(25))  # Retraso leve
print(clasificar_prestamo(35))  # Retraso grave
Documentar funciones (docstrings)
Es buena práctica explicar qué hace tu función:

def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        lista (list): Lista de números
    
    Returns:
        float: El promedio de los números
    """
    return sum(lista) / len(lista)
Puedes ver la documentación con help(calcular_promedio).

Funciones que llaman a otras funciones
def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_total_con_impuesto(precio, cantidad, impuesto=21):
    subtotal = calcular_subtotal(precio, cantidad)
    total = subtotal + (subtotal * impuesto / 100)
    return total

print(calcular_total_con_impuesto(100, 3, 21))  # 363.0
Práctica: funciones para análisis
Crea un archivo funciones.py:

def analizar_ventas(ventas):
    """
    Analiza una lista de ventas y devuelve estadísticas.
    
    Args:
        ventas (list): Lista de valores de ventas
    
    Returns:
        dict: Diccionario con estadísticas
    """
    total = sum(ventas)
    promedio = total / len(ventas)
    maximo = max(ventas)
    minimo = min(ventas)
    
    return {
        'total': total,
        'promedio': promedio,
        'maximo': maximo,
        'minimo': minimo
    }

# Usar la función
ventas_mes = [1500, 2000, 1800, 2200, 1900]
estadisticas = analizar_ventas(ventas_mes)

print(f"Total: {estadisticas['total']}")
print(f"Promedio: {estadisticas['promedio']}")
print(f"Máximo: {estadisticas['maximo']}")
print(f"Mínimo: {estadisticas['minimo']}")
¿Por qué son importantes las funciones?
Reutilización: Escribes el código una vez, lo usas muchas veces
Organización: Tu código está dividido en bloques lógicos
Mantenimiento: Si algo cambia, solo modificas la función
Legibilidad: Nombres descriptivos hacen el código más claro
Testing: Puedes probar cada función por separado
En análisis de datos, usarás funciones constantemente para transformar, validar y procesar información.

