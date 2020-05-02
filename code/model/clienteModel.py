from .model import Model
from mysql import connector

class ClienteModel(Model):
    def create(self, nombre, apellido_p,apellido_m, correo,tel):
        try:
            sql = 'INSERT INTO clientes(nombre, apellido_p,apellido_m, correo,tel) VALUES(%s, %s,%s,%s,%s)'
            values = (nombre, apellido_p,apellido_m, correo,tel)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True
        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def read(self, id):
        try:
            sql = 'SELECT * FROM clientes WHERE id_cliente = %s'
            values = (id,)
            self._cursor.execute(sql, values)
            cliente = self._cursor.fetchone()

            return cliente
        except connector.Error as err:
            return (err) 

    def leer_correo(self, correo):        
        try:
            sql = 'SELECT * FROM clientes WHERE correo = %s'
            values = (correo,)
            self._cursor.execute(sql, values)
            cliente = self._cursor.fetchone()

            return cliente
        except connector.Error as err:
            return (err)         

    def read_all(self):
        try:
            sql = 'SELECT * FROM clientes'
            self._cursor.execute(sql)
            cliente = self._cursor.fetchall()

            return cliente
        except connector.Error as err:
            return (err) 


    def update(self, id, nombre = '', apellido_p = '', apellido_m = '', correo = '', tel = ''):
        fields = []
        val = []

        if nombre !='':
            val.append(nombre)
            fields.append('nombre = %s')
        if apellido_p !='':
            val.append(apellido_p)
            fields.append('apellido_p = %s')
        if apellido_m !='':
            val.append(apellido_m)
            fields.append('apellido_m = %s')    
        if correo != '':
            val.append(correo)
            fields.append('correo = %s')
        if tel != '':
            val.append(tel)
            fields.append('tel = %s')

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE clientes SET ' + ','.join(fields) +' WHERE id_cliente =%s'

            self._cursor.execute(sql,val)
            self._cnx.commit()

            return self._cursor.rowcount > 0

        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def delete(self, id):
        try:
            sql = 'DELETE  FROM clientes WHERE id_cliente = %s'
            values = (id,)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return self._cursor.rowcount > 0
        except connector.Error as err:
            self._cnx.rollback()
            return (err)                       