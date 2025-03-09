import random

# Definimos las dimensiones y los nombres
nombres_ciudades = ["Puerto Quito", "Santo Domingo de los Tsáchilas", "La Concordia"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_ciudades = len(nombres_ciudades)
num_dias = len(dias_semana)
num_semanas = 4

# Inicializamos la matriz 3D con valores aleatorios (temperaturas)
matriz_temperaturas = [[[random.randint(15, 30) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(num_ciudades)]

# Calculamos el promedio de temperaturas para cada ciudad y cada semana
promedio_temperaturas = [[0 for _ in range(num_semanas)] for _ in range(num_ciudades)]

for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(num_dias):
            suma_temperaturas += matriz_temperaturas[ciudad][semana][dia]
        promedio_temperaturas[ciudad][semana] = suma_temperaturas / num_dias
# Mostramos los resultados
for ciudad in range(num_ciudades):
    print(f"Ciudad: {nombres_ciudades[ciudad]}")
    for semana in range(num_semanas):
        print(f"  Semana {semana + 1}:")
        for dia in range(num_dias):
            temp = matriz_temperaturas[ciudad][semana][dia]
            print(f"    {dias_semana[dia]}: {temp} °C")
        print(f"  Promedio de la semana {semana + 1}: {promedio_temperaturas[ciudad][semana]:.2f} °C")