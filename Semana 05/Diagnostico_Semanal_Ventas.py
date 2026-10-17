"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""
#entradas

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) #total de ventas semanal
cantidad_centro = len(ventas_centro)#cantidad de dias registro

menor_centro = min(ventas_centro)#venta minima centro
mayor_centro = max(ventas_centro)#venta maxima centro
promedio_centro = total_centro / cantidad_centro

porcentaje_centro = total_centro * 100 / meta_centro

print(porcentaje_centro)

#tienda norte

total_norte = sum(ventas_norte) #total de ventas semanal
cantidad_norte = len(ventas_norte)#cantidad de dias registro

menor_norte = min(ventas_norte)#venta minima norte
mayor_norte = max(ventas_norte)#venta maxima norte
promedio_norte = total_norte / cantidad_norte

porcentaje_norte = total_norte * 100 / meta_norte

# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.

# TODO: repite los indicadores para Norte.

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
#centro
if total_centro > meta_centro:
    estado_centro = "Meta superada"
elif total_centro == meta_centro:
    estado_centro = "meta alcanzada exactamente"
else:
    estado_centro = "meta NO alcanzada"
    
#norte
if total_norte > meta_norte:
    estado_norte = "Meta superada"
elif total_norte == meta_norte:
    estado_norte = "meta alcanzada exactamente"
else:
    estado_norte = "meta NO alcanzada"

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_gano = "Tienda del centro"
elif total_norte > total_centro:
    tienda_gano = "tienda del norte"
else:
    tienda_gano = "Ambas tiendas vendieron lo mismo"
    
# TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.
print("\t\tCOMPARACION SEMANAL DE TIENDAS")
print("-" * 40,"\n")
print(f"Centro | total ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.0f}%")
print(f"Centro logro: {estado_centro}")
print("-" * 40,"\n")
print(f"Norte | total ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento {porcentaje_norte:.0f}%")
print(f"Norte logro: {estado_norte}")

print("-" * 40,"\n")

if total_centro > total_norte:
    print ("Tienda con mayor ventas: Tienda del centro")
elif total_centro < total_norte:
    print("Tienda con mayor ventas: Tienda del norte")
else:
    print ("Ambas tiendas vendieron lo mismo")



