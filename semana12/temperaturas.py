import random
# Definir ciudades, días de la semana y número de semanas
ciudades = ["Loja", "El Oro", "Quito", "Cuenca", "Guayaquil"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas

# Crear una matriz 3D con temperaturas aleatorias entre 15 y 35 grados
temperaturas = [
    [[random.randint(15, 35) for _ in dias] for _ in range(semanas)]
    for _ in ciudades
]

# Mostrar la matriz de temperaturas
print("\nTemperaturas registradas:")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for semana in range(semanas):
        print(f"  Semana {semana + 1}: {temperaturas[i][semana]}")
