from model.productoModel import ProductoModel
from view.view import View


class ProductoController:

    def __init__(self):
       self.__view = View()
       self.__model = ProductoModel()

    def menu(self): 
        option = None
        
        while option != '0':
            self.__view.producto_menu()
            self.__view.select_opcion()

            option = input()

            if option == '1':
                self.agregar()
            elif option == '2':
                self.read()
            elif option == '3':
                self.read_all()
            elif option == '4':
                self.leer_precios()    
            elif option == '5':
                self.update()
            elif option == '6':
                self.delete()
            elif option == '0':
                pass           
            else:
                self.__view.opcion_invalid()
        
        return

    def agregar(self):
        self.__view.ask('id_barcode:')
        id_barcode = input()
        self.__view.ask('nombre: ') 
        nombre = input()
        self.__view.ask('marca: ')
        marca = input()
        self.__view.ask('detalles: ')
        detalles = input()
        self.__view.ask('precio: ')
        precio = input()

        crear = self.__model.create(id_barcode,nombre,marca,detalles,precio)  
        
        if crear == True:
            self.__view.success()
        else:
            print(crear)
            self.__view.error()

    def read(self):
        self.__view.ask("ID Producto: ")
        idproducto = input()

        producto =  self.__model.read(idproducto)

        if type(producto) == tuple:
            self.__view.mostrar_producto(producto)
        elif producto ==  None:
            self.__view.id_invalido()

        else:
            self.__view.error() 

    def read_all(self):
        productos = self.__model.read_all()

        if type(productos) == list:
            self.__view.mostrar_productos(productos)
        else:
            self.__view.error() 

    def leer_precios(self): 
        self.__view.ask("Rango de precio min: ")
        lower = input()
        self.__view.ask("Rango de precio max: ")
        higher = input()

        productos = self.__model.leer_precios(lower, higher)

        
        if type(productos) == list:
            self.__view.mostrar_productos(productos)
        else:
            self.__view.error()  
            print(productos)       

    def update(self):
        self.__view.mostrar_update()

        self.__view.ask('id_barcode:')
        id_barcode = input()
        self.__view.ask('nombre: ') 
        nombre = input()
        self.__view.ask('marca: ')
        marca = input()
        self.__view.ask('detalles: ')
        detalles = input()
        self.__view.ask('precio: ')
        precio = input()


        result = self.__model.update(id_barcode, nombre,marca,detalles, precio)
        
        if result == True:
            self.__view.success()
        elif result == False: 
            self.__view.id_invalido()   
        else:
            self.__view.error()  

    def delete(self):
        self.__view.ask("barcode: ")
        idbarcode = input()

        result = self.__model.delete(idbarcode)

        if result == True:
            self.__view.success()
        elif  result == False:
            self.__view.id_invalido()
        else:    
            self.__view.error()   


