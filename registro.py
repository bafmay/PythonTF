import textwrap
from os import system
from base_datos import agregar_producto,mostrar_productos,eliminar_producto,actualizar_titulo_producto,actualizar_cantidad_producto,actualizar_fecha_vencimiento_producto


def bienvenida():
    message = '''
    ==================================================================================================
    Bienvenido a la aplicacion de registro de tus alimentos
    Podras registrar los alimentos de tu hogar para que tengas en cuenta la fecha de vencimiento
    y asi aprovecharlos al maximo
    ================================================================================================== 
    '''
    print(textwrap.dedent(message).strip())
    print("")

def mostrar_menu():
    message = '''
        Elija una opcion:
        (1) Registre un alimento / producto
        (2) Mostrar los productos a vencer
        (3) Editar un registro
        (4) Eliminar un registro
        (5) Salir
        '''
    print("")
    print(textwrap.dedent(message).strip())

def registrar_alimento():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = input("Ingrese el numero de cantidad (kg,L,unidades, etc.): ")
    vencimiento = input("Ingrese la fecha de vencimiento (DD/MM/AAAA): ")
    agregar_producto(producto,cantidad,vencimiento)
    print("El registro fue exitoso")
    limpiar_consola()

def mostrar_productos_vencidos():
    elegir_producto()
    limpiar_consola()

def editar_registro():
    elegir_producto()
    producto_id = input("Seleccione el id del producto a actualizar: ")
    opcion_editar = menu_editar()

    if opcion_editar == 1: #titulo
        nuevo_titulo = input("Ingrese el nuevo titulo: ")
        actualizar_titulo_producto(producto_id,nuevo_titulo)
    elif opcion_editar == 2: #cantidad
        nuevo_cantidad = input("Ingrese la nueva cantidad: ")
        actualizar_cantidad_producto(producto_id,nuevo_cantidad)
    elif opcion_editar == 3: #fecha vencimiento
        nuevo_vencimiento = input("Ingrese la nueva fecha de vencimiento (DD/MM/AAAA): ")
        actualizar_cantidad_producto(producto_id,nuevo_vencimiento)

    if 1 <= opcion_editar <= 3:
        print("Los datos han sido actualizados")

    limpiar_consola()

def eliminar_registro():
    elegir_producto()
    producto_id = input("Ingrese el id a eliminar: ")
    eliminar_producto(producto_id)
    print("El registro se ha eliminado correctamente")
    limpiar_consola()

def limpiar_consola():
    input("Presione una tecla para continuar")
    system('cls')

def elegir_producto():
    productos = mostrar_productos()
    for producto in productos:
        print(f"({producto[0]}) Nombre: {producto[1]}, Cantidad: {producto[2]} ,Fecha de vencimiento: {producto[3]}")

def menu_editar():
    print("Campos que desea modificar:")
    print("(1) Titulo")
    print("(2) Cantidad")
    print("(3) Fecha de vencimiento (DD/MM/AAAA)")
    print("(4) Regresar al menu")
    print("")
    return int(input("Elija una opcion: "))

while True:

    try:
        bienvenida()
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




