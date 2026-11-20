"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos en horas."""
    total = 0

    for minuto in minutos:
        total += minuto

    return total / 60


total = sumar_esperas(ESPERAS)
print(sumar_esperas(ESPERAS)) totales = [] totales.append(sumar_esperas([20,60,20,30,])) totales.append(sumar_esperas([10,60,180,20]))

resultado_horas = sumar_esperas(ESPERAS)
print(f"El tiempo total de espera es de {resultado_horas:.2f} horas.")




