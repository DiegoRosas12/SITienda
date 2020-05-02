from view.view import View
from .clienteController import ClienteController
from .productController import ProductoController
from .pedidosController import PedidosController 

class Controller:

    def __init__(self):
        self.__view = View()

    def start(self):
        self.__view.start()  
        self.menu_principal()  

    def menu_principal(self): 
        option = None
        
        while option != '0':
            self.__view.menu()
            self.__view.select_opcion()

            option = input()

            if option == '1':
                clienteController = ClienteController()
                clienteController.menu()
            elif option == '2':
                pedidosController = PedidosController()
                pedidosController.menu()
            elif option == '3':
                productoController = ProductoController()
                productoController.menu()    
            elif option == '0':
                self.__view.end()
            else:
                self.__view.opcion_invalid()
        
        return    
     
