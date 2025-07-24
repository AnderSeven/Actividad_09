destinos_turisticos = {}
def registro():
    clientes = int(input("Cuantos clientes desea registar: "))
    for i in range (clientes):
        i += 1
        print(f"Cliente #{i}")
        codigo = int(input("Ingrese el codigo del cliente: "))
        input("Ingrese el nombre del cliente: ")
        destinos = int(input("Ingrese la cantidad de destinos: "))
        for a in range (destinos):
            print(f"Destino {a +1}: ")


opciones = 0
a = False
while a == False:
    print("---Destinos Turisticos---")
    print("1. Registro de clientes")
    print("2. Listado de clientes con sus destinos")
    print("3. Total de destinos registrados")
    print("4. El cliente con mas destinos")
    print("5. Salir")
    opciones = ("Elija una opcion: ")
    match opciones:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            print("Gracias por usar el sistema")
            a == True
        case _:
            print("Opcion invalida")