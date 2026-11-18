"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos en horas."""
    total = 0

    for minuto in minutos:
        total += minuto

    return total / 60


resultado_horas = sumar_esperas(ESPERAS)
print(f"El tiempo total de espera es de {resultado_horas:.2f} horas.")