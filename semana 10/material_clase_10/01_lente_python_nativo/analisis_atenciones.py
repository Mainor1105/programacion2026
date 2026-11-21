"""Semana 10: resolvemos juntos el caso pendiente de la Semana 9."""

from lector_csv import cargar_atenciones


def explorar_atenciones(atenciones):
    """Decisión 1: ¿qué leímos y cuántas atenciones hay?"""
    # Contamos las filas con un for. Luego miramos los campos de la primera.
    
    cantidad = 0
    for atencion in atenciones:
        # Completamos aquí el contador.
        cantidad += 1
        

    
    print("Atenciones:", cantidad)
    print("Campos:", list(atenciones[0]))
    print("Tipo atenciones",type(atenciones))

def contar_categorias(atenciones):
    """Decisión 2: ¿qué medicamentos, hospitales y diagnósticos aparecen?"""
    medicamentos = {}
    hospitales = {}
    diagnosticos = {}

    for atencion in atenciones:
        # Los nombres ya vienen uniformes en el CSV.
        # Contamos cada categoría en su diccionario con .get().
        medicamento = atencion["medicamento"]
        if medicamento not in medicamentos:
            medicamentos[medicamento] = 0 #aca se agrega el registro al Diccionario
        medicamentos[medicamento] =+ 1
        
        #.get
        hospital = atencion["hospital"]
        hospitales[hospital] = hospitales.get(hospital, 0) + 1
        diagnostico = atencion["diagnostico"]
        diagnosticos[diagnostico] = diagnosticos.get(diagnostico, 0) + 1

    print("Medicamentos:", medicamentos)
    print("Hospitales:", hospitales)
    print("Diagnósticos:", diagnosticos)


def concluir(atenciones):
    """Decisiones 3 y 4: ¿cuántas personas hay y cuánto esperaron?"""
    visitas = {}
    total_minutos = 0

    for atencion in atenciones:
        # Contamos la cédula y acumulamos los minutos de espera.
        total_minutos += int(atencion["minutos_espera"])
        cedula = atencion ["cedula"]
        if cedula in visitas:
            visitas[cedula] += 1
        else:
            visitas[cedula] = 1
        #agregarle que cuente si alguien fue mas veces (12)
        

    print("Personas:", len(visitas))
    print("Minutos de espera:", total_minutos)
    print("Promedio:", total_minutos / len(atenciones))


atenciones = cargar_atenciones()
if atenciones:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("Revisamos los TODO de lector_csv.py.")
