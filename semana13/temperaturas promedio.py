def calcular_temperaturas_promedio(datos):
    """
    Calcula la temperatura promedio de cada ciudad.


    Parámetros:
    datos (dict): Un diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas (una lista por semana).

    Retorna:
    dict: Un diccionario donde las claves son nombres de ciudades y los valores son la temperatura promedio de cada ciudad.
    """
    promedios = {}

    for ciudad, temperaturas in datos.items():
        total_temperaturas = 0
        numero_de_temperaturas = 0

        # Sumar todas las temperaturas de todas las semanas
        for semana in temperaturas:
            total_temperaturas += sum(semana)
            numero_de_temperaturas += len(semana)

        # Calcular el promedio
        if numero_de_temperaturas > 0:
            promedio = total_temperaturas / numero_de_temperaturas
        else:
            promedio = 0

        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso
if "_name_" == "_main_":
    datos = {
        'Puerto Quito': [[20, 22, 21], [19, 21, 22], [18, 20, 21], [21, 23, 22]],
        'Santo Domingo de los Tsáchilas': [[26, 28, 27], [25, 27, 28], [24, 26, 27], [25, 27, 28]],
        'La Concordia': [[17, 19, 18], [16, 18, 19], [15, 17, 18], [18, 20, 19]]
    }

    resultados = calcular_temperaturas_promedio(datos)
    print("Temperaturas promedio por ciudad:")
    for ciudad, promedio in resultados.items():
        print(f"{ciudad}: {promedio:.2f}")

