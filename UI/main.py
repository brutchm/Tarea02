from CL.ArbolController import ArbolController


def agregarNodo(controller):
    num = int(input("Digite el numero que desea añadir al arbol binario"))
    controller.agregarNodo(num)


def imprimirInOrden(controller):
    print(controller.obtenerInOrden())


def imprimirPreOrden(controller):
    print(controller.obtenerPreOrden())


def imprimirPostOrden(controller):
    print(controller.obtenerPostOrden())


def ejecutarOpcion(x, controller):
    if x == 1:
        agregarNodo(controller)
        return None
    if x == 2:
        imprimirInOrden(controller)
        return None
    if x == 3:
        imprimirPreOrden(controller)
        return None
    if x == 4:
        imprimirPostOrden(controller)
        return None
    if x == 5:
        print("Gracias por usar el programa")
        return None
    print("Digite una opcion valida")


def menu():
    x = 0
    controller = ArbolController()

    while x != 5:
        print("Menú")
        print("1. Agregar Nodo")
        print("2. Imprimir In Orden")
        print("3. Imprimir Pre Orden")
        print("4. Imprimir Post Orden")
        print("5 Salir")

        x = int(input("Digite el numero de opción a elegir"))

        ejecutarOpcion(x, controller)


if __name__ == '__main__':
    menu()
