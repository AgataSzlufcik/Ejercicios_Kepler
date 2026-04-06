 # Datos de ventas
precio_unitario = 25.50
cantidad_vendida = 120
costo_envio = 5.00

# Calcular total
subtotal = precio_unitario * cantidad_vendida
total = subtotal + costo_envio

# Calcular descuento si supera 2000
umbral_descuento = 2000
aplica_descuento = subtotal > umbral_descuento

if aplica_descuento:
    descuento = subtotal * 0.10
    total = total - descuento
    print(f"Descuento aplicado: {descuento}")

print(f"Subtotal: {subtotal}")
print(f"Total final: {total}")
print(f"¿Descuento aplicado? {aplica_descuento}") 

