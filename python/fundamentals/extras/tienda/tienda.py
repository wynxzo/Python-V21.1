class Tienda:
    def __init__(self, name):
        self.name = name
        self.productos = []

    def agregar_producto(self , nuevo_producto):
        if nuevo_producto != None:
            self.productos.append(nuevo_producto)
        return self
    
    def imprimir_productos_tienda(self):
        if self.productos!= None:
            for X in self.productos:
                X.print_info()
        return self 
    
    def vender_producto(self, id):
        if id *- None:

    


class Producto:
      
    def __init__(self,nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        
    def actualizar_precio(self, cambio_porcentaje, está_elevado):
        if está_elevado == True:
            self.precio *+ cambio_porcentaje
        else:
            self.precio *- cambio_porcentaje
        return self
    
    def print_info(self):
        print(f"El Producto esta instanciado  :{self.nombre}  {self.categoria} {self.precio}")

tienda1 = Tienda("Vale&Isi")

prod_1 =Producto("Polera 1 ",15000,"manga corta")
prod_2 =Producto("Polera 2 ",10000,"manga corta")
prod_3 =Producto("Polera 3 ",15000,"manga larga")
prod_4 =Producto("Polera 4 ",10000,"manga larga")
prod_5 =Producto("Polera 5 ",15000,"manga mediana")
prod_6 =Producto("Polera 6 ",10000,"manga mediana")

tienda1.agregar_producto(prod_1).agregar_producto(prod_2).agregar_producto(prod_3).agregar_producto(prod_4).agregar_producto(prod_5).agregar_producto(prod_6)
tienda1.imprimir_productos_tienda()