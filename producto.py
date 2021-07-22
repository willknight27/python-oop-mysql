
class Producto:

    #Constructor
    def __init__(self,nombre,valor,categoria,stock):
        self.nombre = nombre
        self.valor = valor
        self.categoria = categoria
        self.stock = stock
    
    def getIVA(self):
        return int(self.valor * 0.19)
    
    def getTotal(self):
        return self.valor + self.getIVA()
    
    def __str__(self):
        return f"nombre: {self.nombre}\nCategoria: {self.categoria}\nValor: {self.valor}\nStock: {self.stock}\nTotal: {self.getTotal()}"
    
