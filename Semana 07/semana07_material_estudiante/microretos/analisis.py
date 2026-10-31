from sedes import sedes
#acceso a listas de sedes emprendimientos
print("sedes registradas:", len(sedes))
print("Primera sede:", sedes[0]["nombre"])
print("ventas de la primera sede", sedes[0]["ventas"])

print("\nAnalisis semanal de empredimientos")

provincias = set()

for sede in sedes:
    total = sum(sede["ventas"])
    porcentaje = total / sede["meta"] * 100
    
    #clasificacion
    if porcentaje >= 100:
        estado = "Meta Alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atencion"
        
print(
    f"{sede["nombre"]} | Total:c{total:,.2f} | "
    f"Cumplimiento: {porcentaje:.2f}% | {estado}"
)
provincias.add(sede["provincia"])
print("set de provincias", provincias)
