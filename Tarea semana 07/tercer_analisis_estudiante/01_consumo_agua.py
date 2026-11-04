"""Caso 1: cambio del consumo diario de agua. Complete el programa."""
"""consumos_litros = [100, 100, 100, 100, 100]"""#para probar 


consumos_litros = [120, 115, 108, 102, 96]


# TODO: Calcule el consumo total y el promedio diario.
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / len(consumos_litros)

primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]

ahorro_litros = primer_dia - ultimo_dia
porcentaje_reduccion = (ahorro_litros/ primer_dia) * 100


if porcentaje_reduccion >= 15:
    clasificacion = "reduccion alta"
elif porcentaje_reduccion > 0:
    clasificacion = "reduccion moderada"
else:
    clasificacion = "sin reduccion"
    
print(f"Total: {consumo_total} L")
print(f"Promedio: {promedio_diario} L")
print(f"Ahorro: {ahorro_litros} L")
print(f"Reduccion: {porcentaje_reduccion} %")
print(f"Clasificacion: {clasificacion}")