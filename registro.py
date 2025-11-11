import textwrap
from os import system
from base_datos import agregar_producto,mostrar_productos


def bienvenida():
    message = '''
    ==================================================================================================
    Bienvenido a la aplicacion de registro de tus alimentos
    Podras registrar los alimentos de tu hogar para que tengas en cuenta la fecha de vencimiento
    y asi aprovecharlos al maximo
    ================================================================================================== 
    '''
    print(textwrap.dedent(message).strip())

def mostrar_menu():
    message = '''
        Elija una opcion:
        (1) Registre un alimento / producto
        (2) Mostrar los productos a vencer
        (3) Editar un registro
        (4) Eliminar un registro
        (5) Salir
        '''
    print(textwrap.dedent(message).strip())

def registrar_alimento():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = input("Ingrese el numero de cantidad (kg,L,unidades, etc.): ")
    vencimiento = input("Ingrese la fecha de vencimiento: ")
    agregar_producto(producto,cantidad,vencimiento)

def mostrar_productos_vencidos():
    productos = mostrar_productos()
    for producto in productos:
        print(f"({producto[0]}) Nombre: {producto[1]}, Cantidad: {producto[2]} ,Fecha de vencimiento: {producto[3]}")

    input("Presione una tecla para continuar")
    system('cls')


def editar_registro():
    print("EDITAR REGISTRO")

def eliminar_registro():
    print("ELIMINAR REGISTRO")


bienvenida()



while True:

    try:
        mostrar_menu()
        opcion = input("Ingrese una opcion : ")
        opcion = int(opcion)

        if opcion <= 0 or opcion > 5:
            print("Ingrese una opcion valida")
        elif opcion == 1:
            registrar_alimento()
        elif opcion == 2:
            mostrar_productos_vencidos()
        elif opcion == 3:
            editar_registro()
        elif opcion == 4:
            eliminar_registro()
        elif opcion == 5:
            print("Gracias por usar nuestro aplicativo")
            break

    except:
        print("Ingrese un opcion valida")




