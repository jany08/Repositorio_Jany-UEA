def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Matriz bidimensional 3x3
matriz = [
    [25, 30, 35],
    [10, 15, 20],
    [40, 45, 50]
]

fila_a_ordenar = 1  # Segunda fila (índice 1)

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la segunda fila ordenada:")
for fila in matriz:
    print(fila)