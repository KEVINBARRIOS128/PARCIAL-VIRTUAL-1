ListaClientes = []
ListaDeProyecto = []
ListaDepartamentos = []
ListaMunicipios = []
ListaResgistro = []
import  os

def ingresarCliente(Codigo, Nombre, Direccion, Telefono):
    ListaClientes.append([Codigo, Nombre, Direccion, Telefono])
    print("Cliente  Ingresado Exitosamente")


def mostrarclientes():
    datos = len(ListaClientes)
    if datos != 0:
         for clientes in ListaClientes:
            print(clientes[0], clientes[1])
    else:
        print("Lista vacia")


def ingresarProyecto(nombreProyecto):
    # almacenando el proyecto a la lista de proyectos

    # mostrando la lista de clientes registrados
    mostrarclientes()
    codigoCliente = input("Ingrese El Codigo Del Cliente Para El Proyecto: ")
    posicion = buscarCliente(codigoCliente)
    if posicion != -1:
        print("Cliente Encontrado")
        mostrardepartamentos()
        departamento = input("Ingres El Nombre Del departamento Para El Proyecto: ")
        nombreDepar = buscardepartamento(departamento)
        if nombreDepar != "vacio":
            print("Departamento Encontrado")
            mostrarmunicipios()
            municipio = input("Ingrese el nombre del municipio para el proyecto: ")
            nombreMunicipio = buscarmunicipio(municipio)
            if nombreMunicipio != "vacio":
                print("Municipio encontrado")
                ListaDeProyecto.append([nombreProyecto, ListaClientes[posicion][0], ListaClientes[posicion][1],
                                        nombreDepar, nombreMunicipio, "ACTIVO"])
                print("Proyecto Registrado Satisfactoriamente")

            else:
                print("Municipio no encontrado volviendo al menu")
        else:
            print("Departamento no nencontrado volvinedo al menu")

    else:
        print("Cliente No Encontrado Volviendo Al Menu")
    print("Proyecto  Ingresado Exitosamente")


def verproyectos():
    for proyectos in ListaDeProyecto:
        print(proyectos)


def ingresarDepartamentos(nombreDepartamento):
    ListaDepartamentos.append(nombreDepartamento)
    print("Departamento agregado Exitosamente")


def mostrardepartamentos():
    for departamento in ListaDepartamentos:
        print(departamento)


def buscardepartamento(buscar):
    nombre = "vacio"
    encontrado = False
    for departamento in ListaDepartamentos:
        if departamento == buscar:
            nombre = departamento
            encontrado = True
            break

    return nombre


def ingresarMunicipios(nombreMunicipio):
    ListaMunicipios.append(nombreMunicipio)
    print("Municipio ingresado exitosamente")


def mostrarmunicipios():
    for municipio in ListaMunicipios:
        print(municipio)


def buscarmunicipio(buscar):
    nombre = "vacio"
    encontrado = False
    for municipio in ListaMunicipios:
        if municipio == buscar:  # si el nombre coincide almacenamos el nombre
            nombre = municipio
            encontrado = True
            break  # rompemos el bucle

    return nombre


def buscarCliente(buscar):
    print("Datos del cliente")
    posicion = 0  # EL PROGRAMA BUSCA LA UBICACION DEL CODIGO
    encontrado = False  # SI NO LO ENCUENTRA SE TIRA AL FOR PARA EL RECORRID
    Codigo = "Codigo"
    Nombre = "Nombre"
    Direccion = "Direccion"
    Telefono = "Telefono"
    Nombre_del_proyecto = "Nombre del Proyecto"
    Estado_del_proyecto = "Estado del Proyecto"
    Departamento = "Departamento"
    Municipio = "Municipio"

    print("{:10} {:10} {:10} {:10} {:10} {:10}  ".format(Codigo, Nombre, Direccion, Telefono, Nombre_del_proyecto, Estado_del_proyecto ))
    for clientes in ListaClientes:
        print("{:10} {:10} {:10} {:10} {:10} {:10}".format(clientes[0], clientes[1], clientes[2], clientes[3], clientes[0][0], clientes[0][1]))
        #print(clientes)

    for Cliente in ListaClientes:
        if Cliente[0] == buscar:  # SI LO ENCUENTRA EN LA EL DATO EN LA POCION 0 ENTONCES SE TIRA A VERDADERO Y PARA
            encontrado = True
            break
        else:
            posicion = posicion + 1  #

    if not encontrado:
        posicion = - 1  # CUANDO TERMINO EL RECORRIDO Y NO LO TERMINO EL REGRESA A UNA POSICON ANTERIOR

    return posicion


def modificarCliente():
    print("ingrese el codigo del cliente")


def eliminarCliente(busqueda):
    print("ingrese el codigo del cliente: ")
    nombre = "vacio"
    encontrado = False
    for clientes in ListaClientes:
        print(clientes[0])
        if clientes[0] == busqueda:
            nombre = clientes
            encontrado = True
            ListaClientes.remove(nombre)
            break

    return nombre

def Salir():
    print("****SALIENDO DEL PROGRAMA******")


def menu():
    opcion = 0

    while opcion != 8:
        print("***************************************************************")
        print( "   BIENVENIDOS A PRINTADOS EXPRESS\n POR FAVOR INGRESA TUS DATOS")


        print("1:  Registrar Cliente  ")
        print("2:  Ingresar Proyecto  ")
        print("3.  Ingresar Departametos  ")
        print("4.  Ingresar Municipios  ")
        print("5.  Buscar el cliente  ")
        print("6.  Eliminar Cliente  ")
        print("7.  Modificar cliente  ")
        print("8.  salir")
        print("9.  Ver Proyectos")
        opcion = int(input("Digite Opcion:  "))

        if opcion == 1:
            Codigo = input("Ingrese El Codigo:   ")
            Nombre = input("Ingrese el Nombre  ")
            Direccion = input("Ingrese la Direccion  ")
            Telefono = input(" Ingrese la Telefono  ")
            ingresarCliente(Codigo, Nombre, Direccion, Telefono)
        elif opcion == 2:

            nombreProyecto = input("Nombre del proyecto  ")
            ingresarProyecto(nombreProyecto)
        elif opcion == 3:
            nombreDepartamento = input("Nombre del Departamento  ")
            ingresarDepartamentos(nombreDepartamento)
        elif opcion == 4:
            nombreMunicipio = input("Nombre del Municipio ")
            ingresarMunicipios(nombreMunicipio)
        elif opcion == 5:
            datos = len(ListaClientes)
            if datos != 0:
                buscar = input("Ingrese El Codigo Del Cliente  ")
                NOMBRE_PROYECTO = "NOMBRE DEL PROYECTO"
                CODIGO = "CODIGO"
                NOMBRE = "NOMBRE"
                DEPARTAMENTO = "DEPARTAMENTO"
                MUNICIPIO = "MUNICIPIO "
                ESTADO = "ESTADO"
                print("{:10} {:10} {:10} {:10} {:10} {:10}  ".format(NOMBRE_PROYECTO, CODIGO, NOMBRE, DEPARTAMENTO, MUNICIPIO, ESTADO))

                for clientes in ListaDeProyecto:
                    if clientes[1]==buscar:
                        print("{:20} {:10} {:10} {:10} {:10} {:10}".format(clientes[0],clientes[1],clientes[2],clientes[3],
                                                                           clientes[4],clientes[5]))
                        break

                respuesta = input("Desea volver al menu Principal 1:SI 0:NO")
                if respuesta == 1:
                    menu()

            else:
                print("Lista vacia")
                menu()

        elif opcion == 6:
            codigoCliente = input("Ingrese el Codigo del Cliente")
            eliminarCliente(codigoCliente)
            print("Supuestamente se borro el cliente")

        elif opcion == 7:
            print("hola")

        elif opcion == 8:
            Salir()
        elif opcion == 9:
            verproyectos()

menu()