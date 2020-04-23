from mysql import connector

class Model:
    def __init__(self,config_db_file = 'config.txt'):
        self.__config_db_file = config_db_file
        self.__config_db = self.__read_config_db()
        self.__connect_to_db()
    
    def __read_config_db(self):
        d ={}

        with open(self.__config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def __connect_to_db(self):
        self._cnx = connector.connect(**self.__config_db)
        self._cursor = self._cnx.cursor()

    def __close_db(self):
        self._cnx.close() 

                   


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

                
            

