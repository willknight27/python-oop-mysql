from producto import Producto
from servicios.servicio_producto import ProductoService

productoService = ProductoService()

def menu():
    continuar = True
    print("--"*10)
    print("Administrador de productos")
    print("1. Ingresar Productos")
    print("2. Mostrar Productos")
    print("0. Salir")
    print("--"*10)

    opcion = input("Ingresar opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_producto()
    elif opcion =="0":
        continuar = False
    else:
        print("\nDebe ingresar un opción correctamente")

    return continuar

def agregar_producto():

    #global -> acceder dentro de una función a una variable/objeto global
    global productoService

    nombre = ""
    while nombre == "":
        nombre = input("Ingrese nombre del producto: ").strip()
        if nombre == "": print("Ingrese nombre del producto correctamente")

    valor = -1
    while valor <= 0:
        try:
            valor = int(input("Ingrese valor: "))
            if valor <=0: print("El valor del producto no puede ser negativo")
        except:
            print("El valor debe ser positivo y número")
    
    stock = -1
    while stock < 0:
        try:
            stock = int(input("Ingrese stock del producto: "))
            if stock < 0: print("El stock no puede ser negativo")
        except:
            print("El stock debe ser un valor numerico")

    categoria = ""
    while categoria == "":
        categoria = input("Ingrese categoria del producto: ").strip()
        if categoria == "": print("Ingrese categoria del producto correctamente")
    

    #Crear Producto
    producto = Producto(nombre,valor,categoria,stock)

    productoService.guardar(producto)

def ver_producto():
    global productoService
    producto = productoService.obtenerProductos()

    for i in producto:
        print("Nombre:",i.nombre) 

while menu():
    pass