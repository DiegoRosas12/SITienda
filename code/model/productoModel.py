from .model import Model
from mysql import connector

class ProductoModel(Model):
    def create(self, id_barcode,nombre,marca, detalles,precio):
        try:
            sql = 'INSERT INTO productos(id_barcode,nombre,marca, detalles,precio) VALUES(%s, %s,%s,%s,%s)'
            values = (id_barcode,nombre,marca, detalles,precio)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True
        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def read(self, id):
        try:
            sql = 'SELECT * FROM productos WHERE id_barcode = %s'
            values = (id,)
            self._cursor.execute(sql, values)
            producto = self._cursor.fetchone()

            return producto
        except connector.Error as err:
            return (err) 

    def read_all(self):
        try:
            sql = 'SELECT * FROM productos'
            self._cursor.execute(sql)
            producto = self._cursor.fetchall()

            return producto
        except connector.Error as err:
            return (err) 

    def leer_precios(self, lower, higher):
        try:
            sql = 'SELECT * FROM productos WHERE precio <= %s AND precio >= %s'
            values = (higher, lower)
            self._cursor.execute(sql, values)
            productos = self._cursor.fetchall()

            return productos
        except connector.Error as err:
            return (err)        

    def update(self, id_barcode, nombre= '', marca = '', detalles = '', precio = '' ):
        fields = []
        val = []

        if id_barcode !='':
            val.append(id_barcode)
            fields.append('id_barcode = %s')
        if nombre !='':
            val.append(nombre)
            fields.append('nombre = %s')
        if marca !='':
            val.append(marca  )
            fields.append('marca  = %s')    
        if detalles!= '':
            val.append(detalles)
            fields.append('detalles = %s')
        if precio != '':
            val.append(precio)
            fields.append('precio = %s')    

        val.append(id_barcode)
        val = tuple(val)         
        try:
            sql = 'UPDATE productos  SET ' + ','.join(fields) +' WHERE id_barcode =%s'

            self._cursor.execute(sql,val)
            self._cnx.commit()

            return self._cursor.rowcount >0


        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def delete(self, id):
        try:
            sql = 'DELETE FROM productos WHERE id_barcode = %s'
            values = (id,)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return self._cursor.rowcount >0
        except connector.Error as err:
            self._cnx.rollback()
            return (err) 