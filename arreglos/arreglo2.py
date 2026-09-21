"""
    Create
    Read
    Update
    Delete
Registrar un listado de edades.
"""

edades = []

def agregarEdad(edad):
    edades.append(edad)

def mostrarEdades():
    return edades

def actualizarEdad(edad, index):
    edades[index] = edad

def eliminarEdad(edad):
    edades.remove(edad)

def menu():
    print("""1. Agregar
    2. Editar
    3. Eliminar
    4. Mostrar
    0. Salir
    Digite su opción [0 - 4]:
    """)
    op = int(input())
    return op

def pedirEdad():
    edad = 0
    while True:
        try:
            edad = int(input(""))
            return edad
        except ValueError:
            print ("Escribe un valor válido")

def seleccionarOpcion():
    op = menu()
    if op == 1:
        print("Dime una edad: ")
        edad = pedirEdad()
        agregarEdad(edad)
    elif op == 2:
        print("Dime en que posición se encuentra")
        pos = pedirEdad()
        print("Dime la nueva edad: ")
        edad = pedirEdad()
        actualizarEdad(edad, pos)
    elif op == 3:
        print("Dime la edad a eliminar: ")
        edad = pedirEdad()
        eliminarEdad()
    elif op == 4:
        print(mostrarEdades())
    elif op == 0:
        print("Adiós.")
        return 0
    else:
        print("Opción inválida")
    seleccionarOpcion()

def main():
    seleccionarOpcion()

main()