import textwrap


def bienvenida():
    message = '''
    ==================================================================================================
    Bienvenido a la aplicacion de registro de tus alimentos
    Podras registrar los alimentos de tu hogar para que tengas en cuenta la fecha de vencimiento
    y asi aprovecharlos al maximo
    ================================================================================================== 
    '''
    print(textwrap.dedent(message).strip())


bienvenida()


while True:

    try:
        opcion = input("Ingrese una opcion : ")
        opcion = int(opcion)

        if opcion <= 0 and opcion > 5:
            print("Ingrese una opcion valida")

        elif opcion == "5":
            break

    except:
        print("Ingrese un opcion valida")




