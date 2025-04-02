# Escritura en el archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Línea 1: Aprendiendo Python paso a paso.\n")
    file.write("Línea 2: Trabajar con archivos es útil.\n")
    file.write("Línea 3: GitHub es una excelente herramienta para el control de versiones.\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:  # Lee cada línea del archivo
        print(line.strip())  # Imprime la línea sin saltos de línea adicionales
