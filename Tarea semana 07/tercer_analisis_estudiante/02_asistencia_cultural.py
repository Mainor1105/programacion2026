"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
# TODO: Calcule el promedio y su porcentaje de ocupación.
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.

total_asistencias = 0
cantidad_bloques = 0
limite = capacidad * 0.70 

for asistencia in asistencias:
    total_asistencias += asistencia
    if asistencia > limite:
        cantidad_bloques += 1
        

if cantidad_bloques > 0:   
    promedio = total_asistencias / len(asistencias)
    porcentaje = (promedio / capacidad) * 100
else:
    promedio = 0
    porcentaje = 0
    


if porcentaje >= 80:
    estado = "Alta"
elif porcentaje >= 50:
    estado = "Media"
else:
    estado = "Baja"
    

print (f"Total: {total_asistencias}")
print(f"Promedio: {promedio}")
print (f"Porcentaje: {porcentaje}%")
print (f"Cantidad de bloques que superan el 70%: {cantidad_bloques}")
print (f"Estado: {estado}")
