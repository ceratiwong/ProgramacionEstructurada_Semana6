# Crear un código que le permita al usuario ingresar carácteres a un arreglo, luego que le muestre los carácteres, después preguntarle en un menú si desea agregar, eliminar o editar.

# Michael Wong y Javier Suazo

caracteres = []

def agregar(caracter):
    caracteres.append(caracter)

def mostrar():
    return caracteres

def editar(nuevo_caracter, index):
    caracteres[index] = nuevo_caracter

def eliminar_valor(caracter):
    print("Eliminando el caracter: ", caracter)
    caracteres.remove(caracter)

def eliminar_indice(index):
    print("Eliminando el caracter en el índice: ", index)
    del caracteres[index]

def solicitar_dato():
    while True:
        texto = input("Dime un texto: ")
        if len(texto) > 0:
            agregar(texto)
            break
        else:
            print("Entrada no válida, ingrese un dato de nuevo.")

def menu_linea():
    print()
    menu()

def menu():
    while True:
        try:
            print("1. Agregar un caracter")
            print("2. Editar un caracter")
            print("3. Eliminar un caracter por índice")
            print("4. Eliminar un caracter por valor")
            print("5. Mostrar todos los caracteres")
            print("0. Salir")
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                solicitar_dato()
                menu_linea()
                break
            elif opcion == 2:
                while True:
                    index = int(input("Ingrese el índice del caracter a editar (0 - ∞): "))
                    if index < len(caracteres):
                        nuevo_caracter = input("Ingrese el nuevo caracter: ")
                        editar(nuevo_caracter, index)
                        menu_linea()
                        break
                    else:
                        print("Índice no válido, ingrese un índice de nuevo.")
            elif opcion == 3:
                while True:
                    index = int(input("Ingrese el índice del caracter a eliminar (0 - ∞): "))
                    if index < len(caracteres):
                        eliminar_indice(index)
                        menu_linea()
                        break
                    else:
                        print("Índice no válido, ingrese un índice de nuevo.")
            elif opcion == 4:
                while True:
                    print("Caracteres actuales: ",mostrar())
                    caracter = input("Ingrese el caracter a eliminar: ")
                    if caracter in caracteres:
                        eliminar_valor(caracter)
                        menu_linea()
                        break
                    else:
                        print("Caracter no encontrado, ingrese un caracter de nuevo.")
            elif opcion == 5:
                print("Caracteres actuales: ",mostrar())
                menu_linea()
            elif opcion == 0:
                print("Saliendo del programa. Adios.")
                break
            else:
                print("Opción no válida, ingrese una opción de nuevo.")
        except ValueError:
            print("Entrada no válida, ingrese un número de nuevo.")


def main():
    menu()


main()