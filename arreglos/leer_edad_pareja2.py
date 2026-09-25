def validar_edad(edad):
    if edad > 18 and edad < 48:
        print(f"Edad válida: {edad}")
    else:
        print(f"Edad inválida: {edad}. Debe estar entre 18 y 48 años.")

def leer_edad():
    while True:
        try:
            edad = int(input("Ingrese una edad entre 1 y 100: "))
            if edad >= 1 and edad <= 100:
                validar_edad(edad)
                break
            else:
                print("Fuera de rango. Debe ser un número entre 1 y 100.\n")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.\n")

leer_edad()