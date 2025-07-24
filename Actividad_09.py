destinos_turisticos = {}
def registro():
    clientes = int(input("Cuantos clientes desea registar: "))
    for i in range (clientes):
        i += 1
        print(f"Cliente #{i}")
        codigo = int(input("Ingrese el codigo del cliente: "))
        nombre = input("Ingrese el nombre del cliente: ")
        destinos_turisticos[codigo] = {
            "nombre": nombre,
            "destinos":{}
        }
        a = False
        while a == False:
            destinos = int(input("Ingrese la cantidad de destinos: "))
            if destinos > 0 and destinos <= 5:
                a = True
            else:
                print("Minimo 1 destino, maximo 5")
        for a in range(destinos):
            nombre_destino = input(f"\nDestino {a + 1}: ")
            destinos_turisticos[codigo]["destinos"] = {
                "nombre_destino": nombre_destino
            }
            print("Se ha registrado el destino con exito")

def listado_clientes_destinos(cliente, destino):
    if cliente == 1:
        return 1
    else:
        return


opciones = 0
a = False
while a == False:
    print("---Destinos Turisticos---")
    print("1. Registro de clientes")
    print("2. Listado de clientes con sus destinos")
    print("3. Total de destinos registrados")
    print("4. El cliente con mas destinos")
    print("5. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            registro()
        case 2:
            listado_clientes_destinos()
        case 3:
            print("adf")
        case 4:
            print("adsf")
        case 5:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")