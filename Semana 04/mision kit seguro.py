#solucion: mision kit seguro

nombre = input("nombre: ").upper().strip()
kit = input("tipo de kit: ").lower().strip()
autorizacion = input("tiene autorizacion (si/no)? ").lower().strip() == "si"
try:
    cantidad = int(input("cantidad de kits?: "))
    if cantidad < 1:
        print("Error: la cantidad minima es 1")
except ValueError:
    print("Cantidad de kits invalida, digite del 1 al 100")
    cantidad = -1
    
try:
    dias = int(input("cantidad de dias: "))
except ValueError:
    print("Cantidad de dias invalida, digite del 1 al 100")
    cantidad = -1
if not nombre or not kit or cantidad < 1:
    resultado = "Registro rechazado: revise los datos ingresados"
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f"solicitud aprobada {nombre} :{cantidad} kit(s) de {kit}"
else:
    resultado = "Solicitud enviada a revision"
print(resultado)


print("_"*50,"\n")
print(resultado)
    