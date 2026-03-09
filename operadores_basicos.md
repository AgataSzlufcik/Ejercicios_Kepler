## ➕ Operadores Básicos
Los operadores te permiten hacer cálculos, comparaciones y operaciones lógicas con tus datos.

Operadores aritméticos
Los usas para hacer matemáticas:

# Suma
total = 10 + 5  # 15

# Resta
diferencia = 20 - 8  # 12

# Multiplicación
producto = 7 * 3  # 21

# División
cociente = 15 / 3  # 5.0 (siempre devuelve float)

# División entera (sin decimales)
division_entera = 15 // 4  # 3

# Módulo (resto de la división)
resto = 15 % 4  # 3

# Potencia
cuadrado = 5 ** 2  # 25
Ejemplo con datos
ventas_enero = 15000
ventas_febrero = 18000
ventas_marzo = 12000

# Total trimestral
total_trimestre = ventas_enero + ventas_febrero + ventas_marzo

# Promedio
promedio = total_trimestre / 3

print(f"Total: {total_trimestre}")
print(f"Promedio: {promedio}")
Operadores de comparación
Te permiten comparar valores. Devuelven True o False:

# Igual a
5 == 5  # True
5 == 3  # False

# Diferente de
5 != 3  # True

# Mayor que
10 > 5  # True

# Menor que
10 < 5  # False

# Mayor o igual
10 >= 10  # True

# Menor o igual
5 <= 10  # True
Ejemplo con datos
precio_producto = 25
presupuesto = 30

puede_comprar = precio_producto <= presupuesto
print(f"¿Puedo comprar? {puede_comprar}")  # True
Operadores lógicos
Combinan condiciones:

# AND (y) - ambas condiciones deben ser True
edad = 25
tiene_licencia = True

puede_conducir = edad >= 18 and tiene_licencia  # True

# OR (o) - al menos una condición debe ser True
es_fin_de_semana = True
es_festivo = False

no_hay_trabajo = es_fin_de_semana or es_festivo  # True

# NOT (no) - invierte el valor
esta_lloviendo = False
hace_buen_tiempo = not esta_lloviendo  # True
Ejemplo con datos
ventas = 15000
meta = 10000
mes_completado = True

# ¿Alcanzamos la meta?
exito = ventas >= meta and mes_completado
print(f"¿Meta alcanzada? {exito}")  # True
Operadores de pertenencia
Comprueban si algo está dentro de otra cosa:

categorias = ["Ficción", "Ensayo", "Poesía", "Cómic"]

# ¿Está "Ficción" en la lista?
"Ficción" in categorias  # True

# ¿NO está "Teatro" en la lista?
"Teatro" not in categorias  # True
Orden de operaciones
Python sigue el orden matemático estándar (PEMDAS):

Paréntesis
Potencias
Multiplicación/División
Suma/Resta
# Sin paréntesis
resultado = 5 + 3 * 2  # 11 (primero 3*2, luego +5)

# Con paréntesis
resultado = (5 + 3) * 2  # 16 (primero 5+3, luego *2)
Consejo: Cuando dudes, usa paréntesis para dejar claro el orden.

Operaciones con texto
Los operadores también funcionan con strings:

# Concatenación (unir texto)
nombre = "Ana"
apellido = "García"
nombre_completo = nombre + " " + apellido  # "Ana García"

# Repetición
separador = "-" * 20  # "--------------------"

# Verificar si contiene
mensaje = "Análisis completado"
contiene_analisis = "Análisis" in mensaje  # True