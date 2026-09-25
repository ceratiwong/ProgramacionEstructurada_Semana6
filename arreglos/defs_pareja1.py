#Crear un código que le permita al usuario ingresar carácteres a un arreglo, luego que le muestre los carácteres, después preguntarle en un menú si desea agregar, eliminar o editar.

#Michael Wong y Javier Suazo

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


def menu():
    print("""1. Agregar
    2. Editar
    3. Eliminar por índice
    4. Eliminar por valor
    5. Mostrar
    0. Salir
    Digite su opción [0 - 5]:
    """)
    while True:
        opcion = int(input())
        if opcion == 1:
            solicitar_dato()
            break
        elif opcion == 2:
            while True:
                index = int(input("Ingrese el índice del caracter a editar: "))
                if index < len(caracteres):
                    nuevo


def solicitar_dato():
    while True:
        texto = input("Dime un texto: ")
        if len(texto) > 0:
            agregar(texto)
            break
        else:
            print("Entrada no válida, ingrese un dato de nuevo.")
