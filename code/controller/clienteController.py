from view.view import View
from model.clienteModel import ClienteModel
from model.direccionModel import DireccionModel

class ClienteController:

    def __init__(self):
       self.__view = View()
       self.__model = ClienteModel()
       self.__direccionModel = DireccionModel()

    def menu(self): 
        option = None
        
        while option != '0':
            self.__view.menu_cliente()
            self.__view.select_opcion()

            option = input()

            if option == '1':
                self.agregar()
            elif option == '2':
                self.read()
            elif option == '3':
                self.read_all()
            elif option == '4':
                self.read_correo()    
            elif option == '5':
                self.update()
            elif option == '6':
                self.delete()
            elif option == '7':
                self.agregar_direccion()
            elif option == '8':
                self.leer_direccion_cliente()
            elif option == '9':
                self.actualizar_direccion()
            elif option == '10':
                self.borrar_direccion()
            elif option == '0':
                pass
            else:
                self.__view.opcion_invalid()
        
        return    

    def agregar(self):
        self.__view.ask('nombre:')
        nombre = input()
        self.__view.ask('Apellido Paterno: ') 
        apellido_p = input()
        self.__view.ask(' Apellido Materno: ')
        apellido_m = input()
        self.__view.ask('Correo: ')
        correo = input()
        self.__view.ask('Tel: ')
        tel = input()

        crear = self.__model.create(nombre, apellido_p,apellido_m, correo,tel)  
        if crear == True:

            self.__view.success()
        else:
            self.__view.error()

    def read(self):
        self.__view.ask("ID Cliente: ")
        idcliente = input()

        cliente =  self.__model.read(idcliente)

        if type(cliente) == tuple:
            self.__view.mostrar_cliente(cliente)
        elif cliente ==  None:
            self.__view.id_invalido()

    def read_correo(self):
        self.__view.ask("Correo: ")
        correo = input()

        cliente =  self.__model.leer_correo(correo)
        if type(cliente) == tuple:
            self.__view.mostrar_cliente(cliente)
        elif cliente ==  None:
            self.__view.id_invalido()        

        else:
            self.__view.error() 

    def read_all(self):
        clientes = self.__model.read_all()

        if type(clientes) == list:
            self.__view.mostrar_clientes(clientes)
        else:
            self.__view.error()  
         

    def update(self):
        self.__view.mostrar_update()
    
        self.__view.ask('ID:')
        idcliente = input()
        self.__view.ask('nombre:')
        nombre = input()
        self.__view.ask('Apellido Paterno: ') 
        apellido_p = input()
        self.__view.ask(' Apellido Materno: ')
        apellido_m = input()
        self.__view.ask('Correo: ')
        correo = input()
        self.__view.ask('Tel: ')
        tel = input()

        result = self.__model.update(idcliente, nombre,apellido_p,apellido_m, correo, tel)
        
        if result == True:
            self.__view.success()
        elif result == False: 
            self.__view.id_invalido()   
        else:
            self.__view.error()  

    def delete(self):
        self.__view.ask("ID: ")
        idcliente = input()

        result = self.__model.delete(idcliente)

        if result == True:
            self.__view.success()
        elif  result == False:
            self.__view.id_invalido()
        else:    
            self.__view.error()

    def agregar_direccion(self):
        self.__view.ask("ID cliente: ")   
        idcliente = input()
        self.__view.ask("Calle: ")
        calle = input()
        self.__view.ask("col: ")
        col = input()
        self.__view.ask("Número exterior: ")  
        noExt = input()
        self.__view.ask("Número interior: ")
        noInt = input()
        self.__view.ask("Código postal: ")
        cp = input()

        result = self.__direccionModel.create(calle, col, noExt, noInt, cp, idcliente)

        if result == True:
            self.__view.success()
        else:
            self.__view.error()

    def leer_direccion_cliente(self):   
        self.__view.ask("ID Cliente: ")
        idcliente = input()
        
        direcciones = self.__direccionModel.leer_direccion_cliente(idcliente)

        if type(direcciones)== list:
            self.__view.mostrar_direcciones(direcciones)
        else:
            self.__view.error()

    def actualizar_direccion(self):
        self.__view.ask("ID Dirección:")
        iddireccion = input()  
        self.__view.ask("Calle: ")
        calle = input()
        self.__view.ask("col: ")
        col = input()
        self.__view.ask("Número exterior: ")  
        noExt = input()
        self.__view.ask("Número interior: ")
        noInt = input()
        self.__view.ask("Código postal: ")
        cp = input()

        result = self.__direccionModel.update(iddireccion, calle, col, noExt, noInt, cp)

        if result == True:
            self.__view.success()
        elif result == False: 
            self.__view.id_invalido()   
        else:
            self.__view.error() 

    def borrar_direccion(self):
        self.__view.ask("ID Dirección: ")
        iddireccion = input()

        result = self.__direccionModel.delete(iddireccion)

        if result == True:
            self.__view.success()
        elif  result == False:
            self.__view.id_invalido()
        else:    
            self.__view.error()
                 


          








        



        

            
