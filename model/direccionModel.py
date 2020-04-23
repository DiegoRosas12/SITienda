from .model import Model
from mysql import connector

class DireccionModel(Model):
    def create(self, calle,col,noExt, noInt,cp,id_cliente):
        try:
            sql = 'INSERT INTO direccion(calle,col,noExt, noInt,cp, id_cliente) VALUES(%s, %s,%s,%s,%s,%s)'
            values = (calle,col,noExt, noInt,cp,id_cliente)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True
        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def read(self, id):
        try:
            sql = 'SELECT * FROM direccion WHERE id_direccion = %s'
            values = (id,)
            self._cursor.execute(sql, values)
            direccion = self._cursor.fetchone()

            return direccion
        except connector.Error as err:
            return (err) 

    def read_all(self):
        try:
            sql = 'SELECT * FROM direccion'
            self._cursor.execute(sql)
            direccion = self._cursor.fetchall()

            return direccion
        except connector.Error as err:
            return (err) 

    def update(self, id, calle = '', col = '', noExt = '', noInt = '', cp = '',id_cliente = '' ):
        fields = []
        val = []

        if calle !='':
            val.append(calle)
            fields.append('calle = %s')
        if col !='':
            val.append(col)
            fields.append('col = %s')
        if noExt !='':
            val.append(noExt )
            fields.append('noExt = %s')    
        if noInt!= '':
            val.append(noInt)
            fields.append('noInt = %s')
        if cp != '':
            val.append(cp)
            fields.append('cp = %s')
        if id_cliente != '':
            val.append(id_cliente)
            fields.append('id_cliente = %s')    

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE direccion SET ' + ','.join(fields) +' WHERE id_direccion =%s'

            self._cursor.execute(sql,val)
            self._cnx.commit()

            return True


        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def delete(self, id):
        try:
            sql = 'DELETE FROM direccion WHERE id_direccion = %s'
            values = (id,)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True
        except connector.Error as err:
            self._cnx.rollback()
            return (err)                       