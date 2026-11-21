"""El mismo expediente, con Pandas y las mismas tres funciones."""

from pathlib import Path
import pandas as pd

ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    print("atenciones: ", len(atenciones))
    print("atenciones tipo: ", type(atenciones) )
    print("campos: ", list(atenciones.columns))


def contar_categorias(atenciones):
    print("Medicamentos", atenciones["medicamento"].value_counts().to_dict())
    print("Hospitales: ", atenciones["hospital"].value_counts())

def concluir(atenciones):
    print("pacientes: ", atenciones["cedula"].unique())
    print("minutos de espera: ", atenciones["minutos_espera".sum()])
    print("minutos de espera: ", atenciones["minutos_espera".mean()])
    print("minutos de espera: ", atenciones["minutos_espera".mode()])
    print("minutos de espera: ", atenciones["minutos_espera".median()])    

try:
    atenciones = pd.read_csv(ARCHIVO_CSV) ##PANDAS.....
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
