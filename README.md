## Football Guesser ⚽
Este programa realiza una serie de preguntas sobre diferentes estadísticas de dos equipos que jugaran un partido de fútbol. Las estadísticas individuales que solicita son: victorias, derrotas, empates, goles anotados, goles en contra, puntos obtenidos durante el torneo, victorias en los últimos cinco partidos, derrotas en los últimos cinco partidos, número de jugadores titulares lesionados, promedio de goles por partido, etc. En base a tus respuestas que proporciones, el programa tratará de predecir cual será el resultado más probable de que suceda en el tiempo regular del partido ya sea victoria, empate o derrota de los equipos correspondientes.

Es importante destacar que no hay una única estadística que garantice el éxito en la predicción de resultados de partidos de fútbol. Es una combinación de múltiples factores y datos lo que puede llevar a resultados más precisos. Además, el fútbol es un deporte impredecible, y siempre habrá una cantidad de incertidumbre involucrada en las predicciones.

ALGORITMO:

ENTRADA: EQUIPO1, EQUIPO2, PUNTAJE1, PUNTAJE2, victorias1, victorias2, derrotas1, derrotas2, empates1, empates2, anotados1, anotados2, contra1, contra2, puntos1, puntos2, partidos1, partidos2, dcinco1, dcinco2, titulares1, titulares2, promedio1, promedio2.

PROCESO:

Pedir el EQUIPO1

Pedir el EQUIPO2

Pedir el número de victorias1 del EQUIPO1

Pedir el número de victorias2 del EQUIPO2

Pedir el número de derrotas1 del EQUIPO1

Pedir el número de derrotas2 del EQUIPO2

Pedir el número de empates1 del EQUIPO1

Pedir el número de empates2 del EQUIPO2

Pedir el número de goles anotados1 del EQUIPO1

Pedir el número de goles anotados2 del EQUIPO2

Pedir el número de goles en contra1 del EQUIPO1

Pedir el número de goles en contra2 del EQUIPO2

Pedir el número de puntos1 del torneo del EQUIPO1

Pedir el número de puntos2 del torneo del EQUIPO2

Pedir el número de victorias en los últimos cinco partidos1 del EQUIPO1

Pedir el número de victorias en los últimos cinco partidos2 del EQUIPO2

Pedir el número de derrotas en los últimos cinco1 partidos del EQUIPO1

Pedir el número de derrotas en los últimos cinco2 partidos del EQUIPO2

Pedir el número de jugadores titulares1 lesionados del EQUIPO1

Pedir el número de jugadores titulares2 lesionados del EQUIPO2

Pedir el promedio1 de goles por partido del EQUIPO1

Pedir el promedio2 de goles por partido del EQUIPO2

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

PUNTAJE1 = 
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

PUNTAJE2 =
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

Si PUNTAJE1 > PUNTAJE2 escribir “EQUIPO1 GANA”

Si PUNTAJE2 > PUNTAJE1 escribir “EQUIPO2 GANA”

Si PUNTAJE1 = PUNTAJE2 escribir “EMPATE”


SALIDA: EQUIPO1 GANA, EQUIPO2 GANA O EMPATE

