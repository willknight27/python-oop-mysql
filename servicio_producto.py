import mysql.connector
from producto import Producto
class ProductoService:

    def __init__(self):
        self.servidor = "localhost"
        self.usuario = "root"
        self.clave = "pass123456"
        self.bd = "productos_python_db"

    def conectar(self):
        self.connection = mysql.connector.connect(
            host = self.servidor,
            user = self.usuario,
            password = self.clave,
            database = self.bd,
            auth_plugin = "mysql_native_password"

        )

    def desconectar(self):
        self.connection.close()


    def guardar(self, producto):
        self.conectar()

        cursor = self.connection.cursor()

        sql = "INSERT INTO productos (nombre,stock,valor,categoria) VALUES (%s,%s,%s,%s)"
        val = (producto.nombre,producto.stock,producto.valor,producto.categoria)
        cursor.execute(sql,val)

        self.connection.commit()
        self.desconectar()
    
    def obtenerProductos(self):
        self.conectar()
        
        cursor = self.connection.cursor()
        cursor.execute("SELECT nombre,valor,categoria,stock FROM productos")

        # resultado esta en formato tupla. Es necesario
        resultado = cursor.fetchall()

        #Crear obnjecto producto
        lista = []
        for r in resultado:
            producto = Producto(r[0],r[1],r[2],r[3])
            lista.append(producto)
        self .desconectar()
        return lista






