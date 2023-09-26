def obtener_estadisticas_equipo(nombre_equipo):
     
    while True:
        try:
            victorias = int(input(f"Ingrese el número de victorias de {nombre_equipo}: "))
            derrotas = int(input(f"Ingrese el número de derrotas de {nombre_equipo}: "))
            empates = int(input(f"Ingrese el número de empates de {nombre_equipo}: "))
            anotados = int(input(f"Ingrese el número de goles anotados por {nombre_equipo}: "))
            contra = int(input(f"Ingrese el número de goles en contra de {nombre_equipo}: "))
            puntos = int(input(f"Ingrese el número de puntos del torneo de {nombre_equipo}: "))
            vcinco = int(input(f"Ingrese el número de victorias en los últimos cinco partidos de {nombre_equipo}: "))
            dcinco = int(input(f"Ingrese el número de derrotas en los últimos cinco partidos de {nombre_equipo}: "))
            titulares = int(input(f"Ingrese el número de jugadores titulares lesionados de {nombre_equipo}: "))
            promedio = float(input(f"Ingrese el promedio de goles por partido de {nombre_equipo}: "))
            tiros_arco = float(input(f"Ingrese el promedio de tiros al arco por partido de {nombre_equipo}: "))
            posesion = float(input(f"Ingrese el promedio de  porcentaje de posesión del balón por partido de {nombre_equipo}: "))
            paradas_portero = float(input(f"Ingrese el promedio de paradas del portero por partido de {nombre_equipo}: "))
            victorias_ult5_entre_ellos= int(input(f"Ingrese el número de victorias en los últimos cinco enfrentamientos entre estos equipos para {nombre_equipo}: "))
            return victorias, derrotas, empates, anotados, contra, puntos, vcinco, dcinco, titulares, promedio, tiros_arco, posesion, paradas_portero, victorias_ult5_entre_ellos
            break
        except ValueError:
            print("¡Error! Ingrese un valor válido.")

def calcular_puntaje(victorias, derrotas, empates, anotados, contra, puntos, vcinco, dcinco, titulares, promedio, tiros_arco, posesion, paradas_portero, victorias_ult5_entre_ellos):
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
        victorias * ponderacion_victorias
        + derrotas * ponderacion_derrotas
        + empates * ponderacion_empates
        + anotados * ponderacion_anotados
        + contra * ponderacion_contra
        + puntos * ponderacion_puntos
        + vcinco * ponderacion_vcinco
        + dcinco * ponderacion_dcinco
        + titulares * ponderacion_titulares
        + promedio * ponderacion_promedio
        + tiros_arco * ponderacion_tiros_arco
        + posesion * ponderacion_posesion
        + paradas_portero * ponderacion_paradas_portero
        + victorias_ult5_entre_ellos * ponderacion_ult5_entre_ellos
    )
    
    return puntaje

import math

import math

def calcular_probabilidades(puntaje_equipo1, puntaje_equipo2):
    probabilidad_victoria_equipo1 = 1 / (1 + math.exp((puntaje_equipo2 - puntaje_equipo1) / 100))
    probabilidad_victoria_equipo2 = 1 / (1 + math.exp((puntaje_equipo1 - puntaje_equipo2) / 100))

    # Calcular la diferencia de puntajes relativa
    diferencia_puntajes = abs(probabilidad_victoria_equipo1 - probabilidad_victoria_equipo2)
    
    probabilidad_empate = 1 / (1 + math.exp(-diferencia_puntajes / 100))

    suma_probabilidades = probabilidad_victoria_equipo1 + probabilidad_empate + probabilidad_victoria_equipo2

    # Normalizar las probabilidades y convertirlas a porcentaje
    probabilidad_victoria_equipo1 = (probabilidad_victoria_equipo1 / suma_probabilidades) * 100
    probabilidad_empate = (probabilidad_empate / suma_probabilidades) * 100
    probabilidad_victoria_equipo2 = (probabilidad_victoria_equipo2 / suma_probabilidades) * 100

    return probabilidad_victoria_equipo1, probabilidad_empate, probabilidad_victoria_equipo2


def determinar_resultado(puntaje_equipo1, puntaje_equipo2):
    if puntaje_equipo1 > puntaje_equipo2:
        return f"{EQUIPO1} GANA"
    elif puntaje_equipo2 > puntaje_equipo1:
        return f"{EQUIPO2} GANA"
    else:
        return "EMPATE"

while True:
  EQUIPO1 = input("Ingrese el nombre del EQUIPO 1: ")
  victorias1, derrotas1, empates1, anotados1, contra1, puntos1, partidos1, dcinco1, titulares1, promedio1, tiros_arco1, posesion1, paradas_portero1, victorias_ult5_entre_ellos1 = obtener_estadisticas_equipo(EQUIPO1)

  EQUIPO2 = input("Ingrese el nombre del EQUIPO 2: ")
  victorias2, derrotas2, empates2, anotados2, contra2, puntos2, partidos2, dcinco2, titulares2, promedio2, tiros_arco2, posesion2, paradas_portero2, victorias_ult5_entre_ellos2 = obtener_estadisticas_equipo(EQUIPO2)

  PUNTAJE1 = calcular_puntaje(victorias1, derrotas1, empates1, anotados1, contra1, puntos1, partidos1, dcinco1, titulares1, promedio1, tiros_arco1, posesion1, paradas_portero1, victorias_ult5_entre_ellos1)
  PUNTAJE2 = calcular_puntaje(victorias2, derrotas2, empates2, anotados2, contra2, puntos2, partidos2, dcinco2, titulares2, promedio2, tiros_arco2, posesion2, paradas_portero2, victorias_ult5_entre_ellos2)

  resultado = determinar_resultado(PUNTAJE1, PUNTAJE2)
  probabilidad_victoria_equipo1, probabilidad_empate, probabilidad_victoria_equipo2 = calcular_probabilidades(PUNTAJE1, PUNTAJE2)
  
  print(f"Predicción: {resultado}")
  print(f"Probabilidad de victoria de {EQUIPO1}: {probabilidad_victoria_equipo1:.2f}%")
  print(f"Probabilidad de empate: {probabilidad_empate:.2f}%")
  print(f"Probabilidad de victoria de {EQUIPO2}: {probabilidad_victoria_equipo2:.2f}%")
  
  respuesta = input("¿Desea predecir el resultado de otro partido? (si/no): ").strip().lower()
  if respuesta != "si":
        break
