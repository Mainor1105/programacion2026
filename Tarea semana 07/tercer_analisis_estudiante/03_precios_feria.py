"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.

promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo


contador = 0
indice = 0

while indice < len(precios):
    if precios[indice] > promedio:
        contador += 1
    indice += 1 

if rango >= 300:
    clasificacion = "variacion alta"
elif rango >= 150:
    clasificacion = "variacion moderada"
else:
    clasificacion = "variacion baja"

print(f"Producto: {producto}") 
print(f"Promedio: ₡{promedio}") 
print(f"Minimo: ₡{minimo}") 
print(f"Maximo: ₡{maximo}") 
print(f"Rango: ₡{rango}") 
print(f"Precios que superan el promedio: {contador}") 
print(f"Clasificación del rango: {clasificacion}")

