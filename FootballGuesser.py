#Pedir los nombres de los equipos
EQUIPO1 = input("Ingrese el nombre del EQUIPO 1: ")
EQUIPO2 = input("Ingrese el nombre del EQUIPO2: ")

#Pedir las estadisticas del EQUIPO1
victorias1 = int(input(f"Ingrese el número de victorias de {EQUIPO1}: "))
derrotas1 = int(input(f"Ingrese el número de derrotas de {EQUIPO1}: "))
empates1 = int(input(f"Ingrese el número de empates de {EQUIPO1}: "))
anotados1 = int(input(f"Ingrese el número de goles anotados por {EQUIPO1}: "))
contra1 = int(input(f"Ingrese el número de goles en contra por {EQUIPO1}: "))
puntos1 = int(input(f"Ingrese el número de puntos del torneo para {EQUIPO1}: "))
partidos1 = int(input(f"Ingrese el número de victorias en los ultimos cinco partidos para {EQUIPO1}: "))
dcinco1 = int(input(f"Ingrese el número de derrotas en los últimos cinco partidos para {EQUIPO1}: "))
titulares1 = int(input(f"Ingrese el número de jugadores titulares lesionados para {EQUIPO1}: "))
promedio1 = float(input(f"Ingrese el promedio de goles por partido para {EQUIPO1}: "))

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
