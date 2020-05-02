class View:
    def start(self):
        print("--------------------------------")
        print("Bienvenido al sistema de compras")
        print("--------------------------------")
        
    def end(self):
        print("\n-----------------")
        print("¡Vuelve pronto!")
        print("-----------------")

    def menu(self):
        print("---------------------")
        print("    Menú Principal:  ")
        print("---------------------") 
        
        print("1. Clientes")
        print("2. Pedidos") 
        print("3. Productos")
        print("\n0. Salir") 
 
    def select_opcion(self):
        print("Seleccione una opción: ", end = '') 

    def opcion_invalid(self):
        print("¡Opción invalida vuelva a intentar!") 

    def ask(self, output):
        print(output, end = '')    
        
    def success(self):    
         print(f"Los cambios se efectuaron correctamente ")

    def error(self):
        print("Error: no se realizo correctamente")
    
    def id_invalido(self):
        print("Error. el id es invalido") 

    def mostrar_update(self):
        print("Actualiza los campos que sean necesarios")

    def mostrar_total(self, total):
        print("\nTotal del pedido: ", total)

    """
    Metodos cliente
    """
    def menu_cliente(self):
        print("---------------------")
        print("    Menú Cliente:  ")
        print("---------------------") 
        
        print("1. Agregar cliente")
        print("2. Leer cliente") 
        print("3. Leer todos los clientes")
        print("4. Leer cliente con correo")
        print("5. Actualizar cliente")
        print("6. Borrar cliente")
        print("7. Agregar dirección de un cliente")
        print("8. Leer dirección de un cliente")
        print("9. Actualizar dirección de un cliente")
        print("10. Borrar la dirección de un cliente")  
        print("\n0. Salir")

    def mostrar_cliente(self, cliente):
        print('ID: ', cliente[0])
        print('Nombre: ', cliente[1])
        print('Apellido Paterno: ', cliente[2])
        print('Apellido Materno: ', cliente[3])
        print('Correo: ', cliente[4])
        print('Télefono: ', cliente[5])

    def mostrar_producto(self, producto):
        print('barcode: ', producto[0])
        print('Nombre: ', producto[1])
        print('Marca: ', producto[2])
        print('Detalles: ', producto[3])
        print('Precio: ', producto[4])  

    def mostrar_clientes(self, clientes):
        print('\n' + 'ID'.ljust(5) + '|' + 'Nombre(s)'.ljust(20) + '|' + 'Apellido Paterno'.ljust(20)+ '|'+'Apellido Materno'.ljust(35)+'|'+'Correo'.ljust(20)+'|' +' Teléfono'.ljust(20))   

        for record in clientes:
            print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}|{record[5]:<35}')

    def mostrar_direcciones(self, direcciones):
        print('\n' + 'ID Dirección'.ljust(15) + '|' + 'Calle'.ljust(20) + '|' + 'Colonia'.ljust(20)+ '|'+'Número Exterior'.ljust(35)+'|'+'Número Interior'.ljust(20)+'|' +' Código Postal'.ljust(20)) 

        for record in direcciones:
            print(f'{record[0]:<15}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}|{record[5]:<35}') 

    """
    Metodos producto
    """
    
    def producto_menu(self):
        print("\n---------------------")
        print("    Menú Producto:  ")
        print("---------------------") 
        
        print("1. Agregar producto")
        print("2. Leer producto") 
        print("3. Leer todos los productos")
        print("4. Leer rangos de precio de los productos")
        print("5. Actualizar producto")
        print("6. Borrar producto")
        print("0. Salir") 

    def mostrar_productos(self, productos):
        print('\n' + 'barcode'.ljust(5) + '|' + 'Nombre(s)'.ljust(20) + '|' + 'Marca'.ljust(20)+ '|'+'Detalles'.ljust(35)+'|'+' Precio'.ljust(20))   

        for record in productos:
            print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}')

    """
    Metodos producto
    """
    
    def mostrar_pedido(self, var):
        print("\n---------------------")
        print("     Pedido:  ")
        print("---------------------")   
        print("ID: ", var[0])
        print("Estado orden:", self.obtener_pedido(var[1])) 
        print("Fecha: ",var[2])
        print("ID Cliente:", var[3])
        print("Nombre del cliente:", var[4])
        print("Dirección de envio:", var[5])
        print("Correo:", var[6])
        print("Teléfono:",var[7])

    def obtener_pedido(self, status):
        string = ''

        if status == 0:
            string = "Pendiente"
        elif status == 1:
            string = "Enviado"
        elif status == 2:
            string = "Retrasado"  
        elif status == 3:
            string = "Entregado" 
        else:
            string ="Desconocido"

        return string               
           

    def pedidos_menu(self):
        print("\n---------------------")
        print("    Menú Pedidos:  ")
        print("---------------------") 
        
        print("1. Empezar Compra")
        print("2. Leer Pedido")
        print("3. Leer todos los pedidos")
        print("4. Leer pedidos entre fechas")
        print("5. Actualizar pedido")
        print("6. Agregar el producto del pedido")
        print("7. Modificar productos del pedido")
        print("8. Borrar productos del pedido")
        print("9. Borrar pedido")
        print("0. Salir")      

    def mostrar_pedidosProductos(self, productos):
        print('\n' + 'ID venta'.ljust(5) + '|' + 'Nombre'.ljust(20) + '|' + 'Marca'.ljust(20)+ '|'+'Precio'.ljust(35)+'|'+' Cantidad'.ljust(20)+ '|'+' Total'.ljust(20))   

        for record in productos:
            print(f'{record[0]:<11}|{record[1]:<25}|{record[2]:<10}|{record[3]:<15}|{record[4]:<15}|{record[5]:<15}')

    def mostrar_pedidos(self, pedidos):
        print('\n' + 'ID pedido'.ljust(5) + '|' + 'Status'.ljust(20) + '|' + 'Fecha y Hora'.ljust(20)+ '|'+'ID Cliente'.ljust(35)+'|'+'ID Dirección'.ljust(20))  
        print('='*120) 

        for record in pedidos:
            print(f'{record[0]:<6}|{self.obtener_pedido(record[1]):<25}|{str(record[2]):<25}|{record[3]:<25}|{record[4]:<25}')

    



           

            


        