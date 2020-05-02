from model.pedidoModel import PedidoModel
from model.ventaModel import VentaModel
from view.view import View
from datetime import datetime


class PedidosController:

    def __init__(self):
       self.__view = View()
       self.__model = PedidoModel()
       self.__ventasmodel = VentaModel()

    def menu(self): 
        option = None
        
        while option != '0':
            self.__view.pedidos_menu()
            self.__view.select_opcion()

            option = input()

            if option == '1':
                self.agregar()
            elif option == '2':
                self.read()
            elif option == '3':
                self.read_all()
            elif option == '4':
                self.read_all_dates()    
            elif option == '5':
                self.update()
            elif option == '6':
                self.__view.ask("ID pedido: ")
                idpedido = input()
                self.agregar_pedidos_a_ordenes(idpedido)
            elif option == '7':
                self.actualizar_pedido_productos()
            elif option == '8':
                self.borrar_producto_del_pedido()  
            elif option == '9':
                self.delete()       
            elif option == '0':
                pass           
            else:
                self.__view.opcion_invalid()
            
        return

    def agregar(self):
        
        self.__view.ask("ID Cliente: " )
        idclientes = input()

        self.__view.ask("ID de la dirección del envio")
        iddireccion = input()

        now = datetime.now()
        result ,idpedido = self.__model.create(0,now.strftime("%Y/%m/%d %H:%M:%S"), idclientes, iddireccion)

        if result == True:
            self.agregar_pedidos_a_ordenes(idpedido)        
        else:
            self.__view.id_invalido()
            print(result)

    def read(self):
        self.__view.ask("ID del pedido: ")
        idpedido = input()

        pedido =  self.__model.read(idpedido)
        pedidoProducto = self.__model.obtener_pedido(idpedido)

        total = 0
        for productos in pedidoProducto:
            total += productos[5]

        if type(pedido) == tuple:
            self.__view.mostrar_pedido(pedido)
            self.__view.mostrar_pedidosProductos(pedidoProducto)
            self.__view.mostrar_total(total)

        elif pedido ==  None:
            self.__view.id_invalido()

        else:
            self.__view.error() 

    def read_all(self):
        pedidos = self.__model.read_all()

        if type(pedidos) == list:
            self.__view.mostrar_pedidos(pedidos)
        else:
            self.__view.error() 

    def read_all_dates(self):
        self.__view.ask("Fecha mayor: ")
        lastdate = input()

        self.__view.ask("Fecha menor: ")
        firstdate = input()

        pedidos = self.__model.read_fechas(lastdate, firstdate)

        if type(pedidos) == list:
            self.__view.mostrar_pedidos(pedidos)
        else:
            self.__view.error()   
          

    def update(self):
        self.__view.mostrar_update()

        self.__view.ask("ID Pedido: ")
        idpedido = input()

        self.__view.ask("Status de envio: ")
        status = input()

        self.__view.ask("Fecha y hora (Año/Mes/Dia HH:MM:SS)")
        fecha = input()
        self.__view.ask("ID Dirección: ")
        iddireccion = input()


        result = self.__model.update(idpedido, status_envio = status,fecha = fecha, direccion_id_direccion =iddireccion)
        
        if result == True:
            self.__view.success()
        elif result == False: 
            self.__view.id_invalido()   
        else:
            self.__view.error()  

    def delete(self):
        self.__view.ask("idpedido: ")
        idpedido = input()

        result = self.__model.delete(idpedido)

        if result == True:
            self.__view.success()
        elif  result == False:
            self.__view.id_invalido()
        else:    
            self.__view.error()   

    def agregar_pedidos_a_ordenes(self,idpedido):

        more = True
        while more == True:
                self.__view.ask("barcode del producto que se desea agregar a la compra: ")
                barcode = input()

                self.__view.ask("Cantidad: ")
                cantidad = input()

                result, idventa = self.__ventasmodel.create(barcode, cantidad)
            
                if result == True:
                    self.__model.create_aux(idpedido, idventa)
                else:
                    self.__view.id_invalido()
                
                self.__view.ask("Desea agregar más productos (y/n):")  
                res = input()
                        
                if res.lower() == "n":
                    more = False   
    def actualizar_pedido_productos(self):
        self.__view.ask("ID pedido: ")
        idpedido = input()

        productos = self.__model.obtener_pedido(idpedido)
        if type(productos) == list:
          
            self.__view.mostrar_pedidosProductos(productos)
            self.__view.ask("\nID venta: ")
            idventa = input()

            self.__view.ask("Cantidad: ")
            cantidad = input()
            
            result = self.__ventasmodel.update(idventa, cantidad =  cantidad)
            
            if result == True:
                self.__view.success()
            elif result == False: 
                self.__view.id_invalido()   
            else:
                self.__view.error()   

        elif productos ==  None:
            self.__view.id_invalido()
            

        else:
            self.__view.error() 

    def borrar_producto_del_pedido(self):
        self.__view.ask("ID pedido: ")
        idpedido = input()

        productos = self.__model.obtener_pedido(idpedido)
        if type(productos) == list:
          
            self.__view.mostrar_pedidosProductos(productos)
            self.__view.ask("\nID venta que desa eliminar: ")
            idventa = input()   

            result = self.__ventasmodel.delete(idventa)
            if result == True:
                self.__view.success()
            elif  result == False:
                self.__view.id_invalido()
            else:    
                self.__view.error()  

        elif productos ==  None:
            self.__view.id_invalido()
            

        else:
            self.__view.error()         
        

                        


