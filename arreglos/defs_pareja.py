#Crear un código que le permita al usuario ingresar carácteres a un arreglo, luego que le muestre los carácteres, después preguntarle en un menú si desea agregar, eliminar o editar.

#Michael Wong y Javier Suazo

from ast import While


caracteres = []

def agregar(caracter):
    caracteres.append(caracter)

def mostrar():
    return caracteres

def editar(nuevo_caracter, index):
    caracteres[index] = nuevo_caracter

def eliminar(caracter):
    print("Eliminando el caracter: ", caracter)
    caracteres.remove(caracter)

def menu():
    print("""1. Agregar
    2. Editar
    3. Eliminar
    4. Mostrar
    0. Salir
    Digite su opción [0 - 4]:
    """)

def solicitar_dato():
    while True:
        texto = input("Dime un texto: ")
        if len(texto) >0 :
            agregar(texto)
            break
        else:
            print("Entrada no válida, ingrese un dato de nuevo.")

solicitar_dato()