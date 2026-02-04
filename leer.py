try:
    with open("alumno.md", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Archivo no encontrado.")
