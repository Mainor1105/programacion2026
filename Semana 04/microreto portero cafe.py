"""microreto portero del café"""

nombre = input ("como te llamas?: ").upper().strip()
energia = int(input("cuanta energia tienes de 0 a 100?: "))
trae_cafe = input("Traes cafe (si/no?: ").lower().strip() == "si"

mensaje = ""

# si menos del 50%  y no tengo cafe: -> Descansar
if energia < 50 and not(trae_cafe):
    mensaje = "Acceso denegado: necesitas dormir o tomar café"
# si 50% o mas o tenga cafe: -> puede ingresar a la clase
elif energia >= 50 or trae_cafe:
    mensaje = "Acceso permitido: adelante puede entrar"
# cualquier otro escenario: portero confundido: revisar respuestas
else:
    mensaje = "Portero confundido : revisar respuestas"
    

print(f"{nombre}: {mensaje}")