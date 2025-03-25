# Crear un diccionario llamado informacion_personal con datos ficticios
informacion_personal = {
    "nombre": "Liam Ramirez",
    "edad": 25,
    "ciudad": "Loja",
    "profesion": "Estudiante"
}

# Acceder y modificar la clave "ciudad"
informacion_personal["ciudad"] = "Quito"  # Cambiamos la ciudad a otra diferente

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0981533538"  # Agregamos el número de teléfono

# Eliminar la clave "edad" ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final después de las modificaciones
print(informacion_personal)