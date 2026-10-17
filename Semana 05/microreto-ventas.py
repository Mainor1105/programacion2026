#Solución: Microreto de Ventas

producto = ["Cafe", 5000, 20]

#Definan una variable llamada porcentaje_aumento. Inicialmente utilicen el valor 20.
porcentaje_aumento = 20

#Calculen el descuento: precio actual × 15 ÷ 100. Réstenlo al precio actual para obtener el precio promocional.
descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento

#Calculen el ingreso actual: precio actual × unidades actuales.
ingreso_actual = producto[1] * producto[2]

#Calculen el aumento de unidades utilizando el valor de porcentaje_aumento: unidades actuales × porcentaje de aumento ÷ 100. Luego sumen ese aumento a las unidades actuales.
unidades_proyectadas = producto[2] * porcentaje_aumento /100 + producto[2]

#Calculen el ingreso proyectado: precio promocional × unidades proyectadas. Luego resten el ingreso actual para obtener la diferencia.
ingreso_proyectado = precio_promocional * unidades_proyectadas - ingreso_actual
ingreso_promocion = ingreso_actual + ingreso_proyectado

#Si la diferencia es mayor que cero, recomienden “lanzar”. Si es cero o menor, recomienden “no lanzar”.
if ingreso_proyectado > 0:
  recomendacion = "Lanzar"
else:
  recomendacion = "No lanzar"

#Salida Esperada
print('\t\tANÁLISIS DE PROMOCIÓN')
print("-" * 70, "\n")
print(f"Producto: {producto[0]}\nPrecio actual: ₡{producto[1]:.0f}\nUnidades actuales: {producto[2]}")
print(f"Ingreso actual: ¢{ingreso_actual:.0f}\nDescuento: ₡{descuento:.0f}\nPrecio promocional: ₡{precio_promocional:.0f}")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%\nUnidades proyectadas: {unidades_proyectadas:.0f}\nIngreso con promoción: ₡{ingreso_promocion:.0f}")
print(f"Diferencia ¢{ingreso_proyectado:.0f}")
print(f"\nRECOMENDACION: {recomendacion}")
