import math


def obtener_estadisticas_equipo(nombre_equipo):
    estadisticas_equipo = {}

    while True:
        try:
            estadisticas_equipo['victorias'] = int(input(
                f"Ingrese el número de victorias de {nombre_equipo}: "
            ))
            estadisticas_equipo['derrotas'] = int(input(
                f"Ingrese el número de derrotas de {nombre_equipo}: "
            ))
            estadisticas_equipo['empates'] = int(input(
                f"Ingrese el número de empates de {nombre_equipo}: "
            ))
            estadisticas_equipo['anotados'] = int(input(
                f"Ingrese el número de goles anotados por {nombre_equipo}: "
            ))
            estadisticas_equipo['contra'] = int(input(
                f"Ingrese el número de goles en contra de {nombre_equipo}: "
            ))
            estadisticas_equipo['puntos'] = int(input(
                f"Ingrese el número de puntos del torneo de {nombre_equipo}: "
            ))
            estadisticas_equipo['vcinco'] = int(input(
                f"Ingrese el número de victorias en los últimos cinco partidos de {nombre_equipo}: "
            ))
            estadisticas_equipo['dcinco'] = int(input(
                f"Ingrese el número de derrotas en los últimos cinco partidos de {nombre_equipo}: "
            ))
            estadisticas_equipo['titulares'] = int(input(
                f"Ingrese el número de jugadores titulares lesionados de {nombre_equipo}: "
            ))
            estadisticas_equipo['promedio'] = float(input(
                f"Ingrese el promedio de goles por partido de {nombre_equipo}: "
            ))
            estadisticas_equipo['tiros_arco'] = float(input(
                f"Ingrese el promedio de tiros al arco por partido de {nombre_equipo}: "
            ))
            estadisticas_equipo['posesion'] = float(input(
                f"Ingrese el promedio de porcentaje de posesión del balón por partido de {nombre_equipo}: "
            ))
            estadisticas_equipo['paradas_portero'] = float(input(
                f"Ingrese el promedio de paradas del portero por partido de {nombre_equipo}: "
            ))
            estadisticas_equipo['victorias_ult5_entre_ellos'] = int(input(
                f"Ingrese el número de victorias en los últimos cinco enfrentamientos entre estos equipos para {nombre_equipo}: "
            ))
            
            break
        except ValueError:
            print("¡Error! Ingrese un valor válido.")

    return estadisticas_equipo


def calcular_puntaje(estadisticas_equipo):
    ponderacion_victorias = 3
    ponderacion_derrotas = -1
    ponderacion_empates = 1
    ponderacion_anotados = 2
    ponderacion_contra = -1
    ponderacion_puntos = 1
    ponderacion_vcinco = 2
    ponderacion_dcinco = -2
    ponderacion_titulares = -1
    ponderacion_promedio = 1
    ponderacion_tiros_arco = 2
    ponderacion_posesion = 1
    ponderacion_paradas_portero = 1
    ponderacion_ult5_entre_ellos = 5
    
    puntaje = (
        estadisticas_equipo['victorias'] * ponderacion_victorias
        + estadisticas_equipo['derrotas'] * ponderacion_derrotas
        + estadisticas_equipo['empates'] * ponderacion_empates
        + estadisticas_equipo['anotados'] * ponderacion_anotados
        + estadisticas_equipo['contra'] * ponderacion_contra
        + estadisticas_equipo['puntos'] * ponderacion_puntos
        + estadisticas_equipo['vcinco'] * ponderacion_vcinco
        + estadisticas_equipo['dcinco'] * ponderacion_dcinco
        + estadisticas_equipo['titulares'] * ponderacion_titulares
        + estadisticas_equipo['promedio'] * ponderacion_promedio
        + estadisticas_equipo['tiros_arco'] * ponderacion_tiros_arco
        + estadisticas_equipo['posesion'] * ponderacion_posesion
        + estadisticas_equipo['paradas_portero'] * ponderacion_paradas_portero
        + estadisticas_equipo['victorias_ult5_entre_ellos'] * ponderacion_ult5_entre_ellos
    )
    
    return puntaje


def calcular_probabilidades(puntaje_equipo1, puntaje_equipo2):
    probabilidad_victoria_equipo1 = 1 / (1 + math.exp((puntaje_equipo2 - puntaje_equipo1) / 100))
    probabilidad_victoria_equipo2 = 1 / (1 + math.exp((puntaje_equipo1 - puntaje_equipo2) / 100))

    diferencia_puntajes = abs(probabilidad_victoria_equipo1 - probabilidad_victoria_equipo2)
    
    probabilidad_empate = 1 / (1 + math.exp(-diferencia_puntajes / 100))

    suma_probabilidades = probabilidad_victoria_equipo1 + probabilidad_empate + probabilidad_victoria_equipo2

    probabilidad_victoria_equipo1 = (probabilidad_victoria_equipo1 / suma_probabilidades) * 100
    probabilidad_empate = (probabilidad_empate / suma_probabilidades) * 100
    probabilidad_victoria_equipo2 = (probabilidad_victoria_equipo2 / suma_probabilidades) * 100

    return probabilidad_victoria_equipo1, probabilidad_empate, probabilidad_victoria_equipo2


def determinar_resultado(puntaje_equipo1, puntaje_equipo2):
    if puntaje_equipo1 > puntaje_equipo2:
        return f"{EQUIPO_1} Gana"
    elif puntaje_equipo2 > puntaje_equipo1:
        return f"{EQUIPO_2} Gana"
    else:
        return "Empate"

while True:
    EQUIPO_1 = input("Ingrese el nombre del Equipo 1: ")
    estadisticas_equipo1 = obtener_estadisticas_equipo(EQUIPO_1)

    EQUIPO_2 = input("Ingrese el nombre del Equipo 2: ")
    estadisticas_equipo2 = obtener_estadisticas_equipo(EQUIPO_2)

    PUNTAJE1 = calcular_puntaje(estadisticas_equipo1)
    PUNTAJE2 = calcular_puntaje(estadisticas_equipo2)

    resultado = determinar_resultado(PUNTAJE1, PUNTAJE2)
    probabilidad_victoria_equipo1, probabilidad_empate, probabilidad_victoria_equipo2 = calcular_probabilidades(PUNTAJE1, PUNTAJE2)

    print(f"Predicción: {resultado}")
    print(f"Probabilidad de victoria de {EQUIPO_1}: {probabilidad_victoria_equipo1:.2f}%")
    print(f"Probabilidad de empate: {probabilidad_empate:.2f}%")
    print(f"Probabilidad de victoria de {EQUIPO_2}: {probabilidad_victoria_equipo2:.2f}%")

    respuesta = input("¿Desea predecir el resultado de otro partido? (si/no): ").strip().lower()
    if respuesta != "si":
        break
