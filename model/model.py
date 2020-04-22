from mysql import connector

class Model:
    def __init__(self,config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    
    def read_config_db(self):
        d ={}

        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close() 

    """
    metodos de clientes
    """                   
    def create_cliente(self, Nombre, Apellido,Correo, Tel, Direccion):
        try:
            sql = 'INSERT INTO Clientes(Nombre,Apellido,Correo,Tel,Direccion) VALUES(%s, %s,%s,%s,%s)'
            values = (Nombre,Apellido, Correo, Tel,Direccion)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_cliente(self, id):
        try:
            sql = 'SELECT * FROM Clientes WHERE id_Cliente = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            cliente = self.cursor.fetchone()

            return cliente
        except connector.Error as err:
            return (err)  

    def read_all_clientes(self):
        try:
            sql = 'SELECT * FROM Clientes'
            self.cursor.execute(sql)
            cliente = self.cursor.fetchall()

            return cliente
        except connector.Error as err:
            return (err)  

    def update_cliente(self, id, Nombre = '', Apellido = '', Correo = '', Tel = '', Direccion = ''):
        fields = []
        val = []

        if Nombre !='':
            val.append(Nombre)
            fields.append('Nombre = %s')
        if Apellido !='':
            val.append(Apellido)
            fields.append('Apellido = %s')
        if Correo != '':
            val.append(Correo)
            fields.append('Correo = %s')
        if Tel != '':
            val.append(Tel)
            fields.append('Tel = %s')
        if Direccion != '':
            val.append(Direccion)
            fields.append('Direccion = %s') 

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE Clientes SET ' + ','.join(fields) +' WHERE id_Cliente =%s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_cliente(self, id):
        try:
            sql = 'DELETE  FROM Clientes WHERE id_Cliente = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return (err)  

    def create_producto(self, id_barcode, Nombre, Detalles, Cantidad, Precio):
        try:
            sql = 'INSERT INTO Productos(id_barcode, Nombre,Detalles, Cantidad,Precio) VALUES(%s, %s,%s,%s,%s)'
            values = (id_barcode, Nombre,Detalles, Cantidad,Precio)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_producto(self, id_barcode):
        try:
            sql = 'SELECT * FROM Productos WHERE id_barcode = %s'
            values = (id_barcode,)
            self.cursor.execute(sql, values)
            producto = self.cursor.fetchone()

            return producto
        except connector.Error as err:
            return (err)  

    def read_all_productos(self):
        try:
            sql = 'SELECT * FROM Productos'
            self.cursor.execute(sql)
            producto = self.cursor.fetchall()

            return producto
        except connector.Error as err:
            return (err)  

    def read_producto_quantity_lower(self, Cantidad):
        try:
            sql = 'SELECT * FROM Productos WHERE Cantidad < %s'
            values =(Cantidad)
            self.cursor.execute(sql,values)
            producto = self.cursor.fetchall()

            return producto
        except connector.Error as err:
            return (err)

    def read_producto_between_price(self, pricekower, pricehigher):
        try:
            sql = 'SELECT * FROM Productos WHERE Precio >= %s AND Precio <= %s'
            values =(pricekower, pricehigher)
            self.cursor.execute(sql,values)
            producto = self.cursor.fetchall()

            return producto
        except connector.Error as err:
            return (err)            


    def update_producto(self, id_barcode, Nombre = '',Detalles = '', Cantidad = '',Precio = ''):
        fields = []
        val = []

        if Nombre !='':
            val.append(Nombre)
            fields.append('Nombre = %s')
        if Detalles !='':
            val.append(Detalles)
            fields.append('Detalles = %s')
        if Cantidad  != '':
            val.append(Cantidad )
            fields.append('Cantidad  = %s')
        if Precio != '':
            val.append(Precio)
            fields.append('Precio = %s')

        val.append(id_barcode)
        val = tuple(val)         
        try:
            sql = 'UPDATE Productos SET ' + ','.join(fields) +' WHERE id_barcode =%s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_producto(self,id_barcode):
        try:
            sql = 'DELETE  FROM Productos WHERE id_barcode = %s'
            values = (id_barcode,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return (err)   

    def create_pedido(self, id_barcode, id_Cliente, Fecha, Direccion, Cantidad):
        try:
            sql = 'INSERT INTO Pedidos(id_barcode, id_Cliente,Fecha,Direccion, Cantidad) VALUES(%s, %s,%s,%s,%s)'
            values = (id_barcode, id_Cliente,Fecha,Direccion,Cantidad)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

                
            
