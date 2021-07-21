
class ProductoService:

    listaProductos = []

    def __init__(self):
        self.servidor = ""
        self.usuario = ""
        self.clave = ""
        self.bd = ""


    def guardar(self, producto):
        self.listaProductos.append(producto)
    
    def obtenerProductos(self):
        return self.listaProductos
