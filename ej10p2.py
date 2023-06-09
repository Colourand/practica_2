nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

nombres = nombres.split(",")

#A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#notas. Utilizar esta estructura para la resolución de los siguientes items.
dic_nombres_notas = {i : [j , k] for i, j, k in zip(nombres, notas_1, notas_2)}
print(dic_nombres_notas)


#B. Calcular el promedio de notas de cada estudiante.
dic_nombres_notas_promediadas = {i : [j] for i,j in zip(nombres, list(map(lambda x: (x[0]+x[1])/2, dic_nombres_notas.values())))}
print(dic_nombres_notas_promediadas)


#C. Calcular el promedio general del curso.
promedio_general = (sum(list(map(lambda x: x[0]+x[1], dic_nombres_notas.values())))) / (len(notas_1) * 2)
print(promedio_general)


#D. Identificar al estudiante con la nota promedio más alta.
alumno_promedio_max = max(dic_nombres_notas_promediadas, key = dic_nombres_notas_promediadas.get)
print(alumno_promedio_max)


#E. Identificar al estudiante con la nota más baja.
alumno_nota_min = min(dic_nombres_notas, key = dic_nombres_notas.get)
print(alumno_nota_min)
