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

#Calcular los puntajes
PUNTAJE1 = victorias1 - derrotas1 - empates1 + anotados1 - contra1 + puntos1 + partidos1 - dcinco1 - titulares1 + promedio1
PUNTAJE2 = victorias2 - derrotas2 - empates2 + anotados2 - contra2 + puntos2 + partidos2 - dcinco2 - titulares2 + promedio2
