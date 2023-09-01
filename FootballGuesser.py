def obtener_estadisticas_equipo(nombre_equipo):
    victorias = int(input(f"Ingrese el número de victorias de {nombre_equipo}: "))
    derrotas = int(input(f"Ingrese el número de derrotas de {nombre_equipo}: "))
    empates = int(input(f"Ingrese el número de empates de {nombre_equipo}: "))
    anotados = int(input(f"Ingrese el número de goles anotados por {nombre_equipo}: "))
    contra = int(input(f"Ingrese el número de goles en contra de {nombre_equipo}: "))
    puntos = int(input(f"Ingrese el número de puntos del torneo para {nombre_equipo}: "))
    vcinco = int(input(f"Ingrese el número de victorias en los últimos cinco partidos para {nombre_equipo}: "))
    dcinco = int(input(f"Ingrese el número de derrotas en los últimos cinco partidos para {nombre_equipo}: "))
    titulares = int(input(f"Ingrese el número de jugadores titulares lesionados para {nombre_equipo}: "))
    promedio = float(input(f"Ingrese el promedio de goles por partido para {nombre_equipo}: "))
    tiros_arco = int(input(f"Ingrese el número de tiros al arco por partido para {nombre_equipo}: "))
    posesion = float(input(f"Ingrese el promedio de  porcentaje de posesión del balón por partido para {nombre_equipo}: "))
    paradas_portero = int(input(f"Ingrese el promedio de paradas del portero por partido para {nombre_equipo}: "))
    return victorias, derrotas, empates, anotados, contra, puntos, vcinco, dcinco, titulares, promedio, tiros_arco, posesion, paradas_portero

def calcular_puntaje(victorias, derrotas, empates, anotados, contra, puntos, vcinco, dcinco, titulares, promedio, tiros_arco, posesion, paradas_portero):
    ponderacion_victorias = 3
    ponderacion_derrotas = -1
    ponderacion_empates = 1
    ponderacion_anotados = 2
    ponderacion_contra = -1
    ponderacion_puntos = 1
    ponderacion_vcinco = 2
    ponderacion_dcinco = -1
    ponderacion_titulares = -1
    ponderacion_promedio = 1
    ponderacion_tiros_arco = 2
    ponderacion_posesion = 1
    ponderacion_paradas_portero = 2
    
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
    )
    
    return puntaje

def determinar_resultado(puntaje_equipo1, puntaje_equipo2):
    if puntaje_equipo1 > puntaje_equipo2:
        return f"{EQUIPO1} GANA"
    elif puntaje_equipo2 > puntaje_equipo1:
        return f"{EQUIPO2} GANA"
    else:
        return "EMPATE"

while True:
  EQUIPO1 = input("Ingrese el nombre del EQUIPO 1: ")
  victorias1, derrotas1, empates1, anotados1, contra1, puntos1, partidos1, dcinco1, titulares1, promedio1, tiros_arco1, posesion1, paradas_portero1 = obtener_estadisticas_equipo(EQUIPO1)

  EQUIPO2 = input("Ingrese el nombre del EQUIPO 2: ")
  victorias2, derrotas2, empates2, anotados2, contra2, puntos2, partidos2, dcinco2, titulares2, promedio2, tiros_arco2, posesion2, paradas_portero2 = obtener_estadisticas_equipo(EQUIPO2)

  PUNTAJE1 = calcular_puntaje(victorias1, derrotas1, empates1, anotados1, contra1, puntos1, partidos1, dcinco1, titulares1, promedio1, tiros_arco1, posesion1, paradas_portero1)
  PUNTAJE2 = calcular_puntaje(victorias2, derrotas2, empates2, anotados2, contra2, puntos2, partidos2, dcinco2, titulares2, promedio2, tiros_arco2, posesion2, paradas_portero2)

  resultado = determinar_resultado(PUNTAJE1, PUNTAJE2)
  print(resultado)
  respuesta = input("¿Desea predecir el resultado de otro partido? (si/no): ").strip().lower()
  if respuesta != "si":
        break
