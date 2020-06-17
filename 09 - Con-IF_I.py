print("Programa de Evaluacion de Alumnos")

nota_alumno = input("Introduce la nota del alumno")

def calificacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Reprobado"
    return valoracion

print(calificacion(int(nota_alumno)))
