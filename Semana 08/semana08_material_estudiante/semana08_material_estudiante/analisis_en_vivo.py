"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")


# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
equivalencias = {
    "acetaminofen" : "acetaminofén",
    "paracetamol" : "acetaminofén",
    "antiacido" : "antíacido",
    "losartán" : "losartan",
}

conteo_medicamentos = {}
total_medicamentos = 0
print("\n Analisis fase #1 muestra 3")
for indice in range (3):
    registro = registros[indice]
    print(f"\nCedula: {registro["paciente_cedula"]}"
      f"\nPaciente: {registro["paciente_nombre"]}"
      f"\nDiagnostico: {registro["diagnostico"]}"
      f"\nMedicamentos: {registro["medicamentos"]}")
    #cedula, nombre, diagnostico, medicamentos y el type()
   
    for medicamento in registro["medicamentos"]:
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
           medicamento = equivalencias[medicamento]
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
        total_medicamentos += 1
    
print("Total de medicamentos resetados:", total_medicamentos)
print(conteo_medicamentos)

# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
conteo_medicamentos = {}
total_medicamentos = 0
print("\n Analisis fase #2 medicamentos y atenciones")
for registro in registros:
     for medicamento in registro["medicamentos"]:
            medicamento = medicamento.strip().lower()
            if medicamento in equivalencias:
                medicamento = equivalencias[medicamento]
                
            if medicamento in conteo_medicamentos:
                conteo_medicamentos[medicamento] += 1
            else:
                conteo_medicamentos[medicamento] = 1
            total_medicamentos += 1
        
print("Total de medicamentos resetados:", total_medicamentos)
print(conteo_medicamentos)

for medicamento, cantidad in conteo_medicamentos.items():
    print(f"- {medicamento}:\t {cantidad}")
    
    
# FASE 3: CONTAR ATENCIONES POR HOSPITAL
pacientes_por_hospital = {}

for reg in registros:
    hosp = reg["hospital"]
    paciente = reg["paciente_id"]
   
    if hosp not in pacientes_por_hospital:
        pacientes_por_hospital[hosp] = set()
        

    pacientes_por_hospital[hosp].add(paciente)

conteo_pacientes_hospital = {}
for hosp, conjunto_pacientes in pacientes_por_hospital.items():
    conteo_pacientes_hospital[hosp] = len(conjunto_pacientes)

print("Cantidad de pacientes únicos atendidos por hospital:")
for hosp, cantidad in conteo_pacientes_hospital.items():
    print(f"- {hosp}: {cantidad} pacientes")
    
# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA
conteo_enfermedades = {}

for reg in registros:
    diag = reg["diagnostico"]
    
    if diag in conteo_enfermedades:
        conteo_enfermedades[diag] += 1
    else:
        conteo_enfermedades[diag] = 1

print("Atenciones por enfermedad:")
for diag, cantidad in conteo_enfermedades.items():
    print(f"- {diag}: {cantidad} atenciones")

