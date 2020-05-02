from .model import Model
from mysql import connector

class VentaModel(Model):
    def create(self,barcode,cantidad):
        try:
            sql = 'INSERT INTO ventas(barcode,cantidad) VALUES(%s, %s)'
            values = (barcode,cantidad)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True, self._cursor.lastrowid 
        except connector.Error as err:
            self._cnx.rollback()
            return(err), None

    def read(self, id):
        try:
            sql = 'SELECT * FROM ventas WHERE id_venta = %s'
            values = (id,)
            self._cursor.execute(sql, values)
            venta = self._cursor.fetchone()

            return venta
        except connector.Error as err:
            return (err) 

    def read_all(self):
        try:
            sql = 'SELECT * FROM ventas'
            self._cursor.execute(sql)
            venta = self._cursor.fetchall()

            return venta
        except connector.Error as err:
            return (err) 

    def update(self, id_venta, barcode= '',cantidad = '' ):
        fields = []
        val = []

        if barcode !='':
            val.append(barcode)
            fields.append('barcode = %s')
        if cantidad  !='':
            val.append(cantidad )
            fields.append('cantidad   = %s')    
        
        

        val.append(id_venta)
        val = tuple(val)         
        try:
            sql = 'UPDATE ventas  SET ' + ','.join(fields) +' WHERE id_venta =%s'

            self._cursor.execute(sql,val)
            self._cnx.commit()

            return True


        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def delete(self, id):
        try:
            sql = 'DELETE FROM ventas WHERE id_venta = %s'
            values = (id,)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True
        except connector.Error as err:
            self._cnx.rollback()
            return (err) 