class Estudiante:
    def __init__(self, nombre, edad, sexo, nota):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nota = nota

# Función para cargar estudiantes en una lista
def cargar_estudiantes():
    lista_estudiantes = []
    for i in range(8):
        nombre = input(f'Nombre del estudiante {i+1}: ')
        edad = int(input(f'Edad del estudiante {i+1}: '))
        sexo = input(f'Sexo del estudiante {i+1} (M/F): ')
        nota = float(input(f'Nota del estudiante {i+1}: '))
        estudiante = Estudiante(nombre, edad, sexo, nota)
        lista_estudiantes.append(estudiante)
    return lista_estudiantes

# Función para contar hombres y mujeres que aprobaron
def contar_aprobados(lista_estudiantes):
    hombres_aprobados = 0
    mujeres_aprobados = 0
    lista_aprobados = []

    for estudiante in lista_estudiantes:
        if estudiante.nota >= 4.5:
            lista_aprobados.append(estudiante.nombre)
            if estudiante.sexo.upper() == 'M':
                hombres_aprobados += 1
            elif estudiante.sexo.upper() == 'F':
                mujeres_aprobados += 1

    return hombres_aprobados, mujeres_aprobados, lista_aprobados

# Cargar dos listas de estudiantes
print("Cargando estudiantes para la primera lista:")
lista_estudiantes_1 = cargar_estudiantes()
print("\nCargando estudiantes para la segunda lista:")
lista_estudiantes_2 = cargar_estudiantes()

# Contar aprobados en ambas listas
hombres_aprobados_1, mujeres_aprobados_1, lista_aprobados_1 = contar_aprobados(lista_estudiantes_1)
hombres_aprobados_2, mujeres_aprobados_2, lista_aprobados_2 = contar_aprobados(lista_estudiantes_2)

# Total de aprobados
hombres_aprobados_total = hombres_aprobados_1 + hombres_aprobados_2
mujeres_aprobados_total = mujeres_aprobados_1 + mujeres_aprobados_2
lista_aprobados_total = lista_aprobados_1 + lista_aprobados_2

# Resultados
print(f"\nHombres que aprobaron: {hombres_aprobados_total}")
print(f"Mujeres que aprobaron: {mujeres_aprobados_total}")
print("Lista de estudiantes que recibirán estímulo académico:")
for nombre in lista_aprobados_total:
    print(nombre)
