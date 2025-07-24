clientes = int(input("Cuantos clientes desea registar: "))
for i in range (clientes):
    i += 1
    print(f"Cliente #{i}")
    codigo = int(input("Ingrese el codigo del cliente: "))
    input("Ingrese el nombre del cliente: ")
    destinos = int(input("Ingrese la cantidad de destinos: "))
    for a in range (destinos):
        print(f"Destino {a +1}: ")