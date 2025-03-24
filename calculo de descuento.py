# Este programa define una función para calcular descuentos y la llama con diferentes parámetros.
def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el monto del descuento aplicado a una compra.

  Args:
    monto_total: El monto total de la compra.
    porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 10).

  Returns:
    El monto del descuento calculado.
  """
  descuento = (porcentaje_descuento / 100) * monto_total
  return descuento

# Programa principal: Llamada a la función calcular_descuento

# Llamada 1: Usando el porcentaje de descuento por defecto (10%)
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

print(f"Compra 1: Monto total = ${monto_compra1}, Descuento = ${descuento1}, Monto final = ${monto_final1}")

# Llamada 2: Proporcionando un porcentaje de descuento personalizado (20%)
monto_compra2 = 250
descuento2 = calcular_descuento(monto_compra2, 20)
monto_final2 = monto_compra2 - descuento2

print(f"Compra 2: Monto total = ${monto_compra2}, Descuento = ${descuento2}, Monto final = ${monto_final2}")