#Pedir las estadisticas de los equipos
def obtener_estadisticas_equipo(nombre_equipo):
    victorias = int(input(f"Ingrese el número de victorias de {nombre_equipo}: "))
    derrotas = int(input(f"Ingrese el número de derrotas de {nombre_equipo}: "))
    empates = int(input(f"Ingrese el número de empates de {nombre_equipo}: "))
    anotados = int(input(f"Ingrese el número de goles anotados por {nombre_equipo}: "))
    contra = int(input(f"Ingrese el número de goles en contra por {nombre_equipo}: "))
    puntos = int(input(f"Ingrese el número de puntos del torneo para {nombre_equipo}: "))
    vcinco = int(input(f"Ingrese el número de victorias en los últimos cinco partidos para {nombre_equipo}: "))
    dcinco = int(input(f"Ingrese el número de derrotas en los últimos cinco partidos para {nombre_equipo}: "))
    titulares = int(input(f"Ingrese el número de jugadores titulares lesionados para {nombre_equipo}: "))
    promedio = float(input(f"Ingrese el promedio de goles por partido para {nombre_equipo}: "))
    tiros_arco = int(input(f"Ingrese el número de tiros al arco por partido para {nombre_equipo}: "))
    posesion = float(input(f"Ingrese el promedio de  porcentaje de posesión del balón por partido para {nombre_equipo}: "))
    paradas_portero = int(input(f"Ingrese el promedio de paradas del portero por partido para {nombre_equipo}: "))
    return victorias, derrotas, empates, anotados, contra, puntos, vcinco, dcinco, titulares, promedio, tiros_arco, posesion, paradas_portero

#Pedir las estadisticas del EQUIPO2
victorias2 = int(input(f"Ingrese el número de victorias de {EQUIPO2}: "))
derrotas2 = int(input(f"Ingrese el número de derrotas de {EQUIPO2}: "))
empates2 = int(input(f"Ingrese el número de empates de {EQUIPO2}: "))
anotados2 = int(input(f"Ingrese el número de goles anotados por {EQUIPO2}: "))
contra2 = int(input(f"Ingrese el número de goles en contra por {EQUIPO2}: "))
puntos2 = int(input(f"Ingrese el número de puntos del torneo para {EQUIPO2}: "))
partidos2 = int(input(f"Ingrese el número de victorias en los ultimos cinco partidos para {EQUIPO2}: "))
dcinco2 = int(input(f"Ingrese el número de derrotas en los últimos cinco partidos para {EQUIPO2}: "))
titulares2 = int(input(f"Ingrese el número de jugadores titulares lesionados para {EQUIPO2}: "))
promedio2 = float(input(f"Ingrese el promedio de goles por partido para {EQUIPO2}: "))

# Aplicar ponderaciones a las estadísticas
ponderacion_victorias = 3
ponderacion_derrotas = -1
ponderacion_empates = 1
ponderacion_anotados = 2
ponderacion_contra = -1
ponderacion_puntos = 1
ponderacion_partidos = 2
ponderacion_dcinco = -1
ponderacion_titulares = -1
ponderacion_promedio = 1

#Calcular puntajes
PUNTAJE1 = (
    victorias1 * ponderacion_victorias
    + derrotas1 * ponderacion_derrotas
    + empates1 * ponderacion_empates
    + anotados1 * ponderacion_anotados
    + contra1 * ponderacion_contra
    + puntos1 * ponderacion_puntos
    + partidos1 * ponderacion_partidos
    + dcinco1 * ponderacion_dcinco
    + titulares1 * ponderacion_titulares
    + promedio1 * ponderacion_promedio
)

PUNTAJE2 = (
    victorias2 * ponderacion_victorias
    + derrotas2 * ponderacion_derrotas
    + empates2 * ponderacion_empates
    + anotados2 * ponderacion_anotados
    + contra2 * ponderacion_contra
    + puntos2 * ponderacion_puntos
    + partidos2 * ponderacion_partidos
    + dcinco2 * ponderacion_dcinco
    + titulares2 * ponderacion_titulares
    + promedio2 * ponderacion_promedio
)

# Comparar puntajes y mostrar resultado
if PUNTAJE1 > PUNTAJE2:
    print(f"{EQUIPO1} GANA")
elif PUNTAJE2 > PUNTAJE1:
    print(f"{EQUIPO2} GANA")
else:
    print("EMPATE")
