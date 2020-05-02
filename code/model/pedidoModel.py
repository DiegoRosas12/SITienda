from .model import Model
from mysql import connector

class PedidoModel(Model):
    def create(self,status_envio,fecha,idCliente,iddireccion):
        try:
            sql = 'INSERT INTO pedidos(status_envio,fecha,clientes_idCliente,direccion_id_direccion) VALUES(%s, %s,%s,%s)'
            values = (status_envio,fecha,idCliente,iddireccion)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True, self._cursor.lastrowid 
        except connector.Error as err:
            self._cnx.rollback()
            return(err), None

    def read(self, id):
        try:
            sql = 'SELECT id_pedido, status_envio,fecha, clientes.id_cliente,CONCAT( nombre, "", apellido_p, "", apellido_m,"") AS Nombre, CONCAT(calle, ",",noExt, ",",noInt,",",col,",",cp) AS Direccion, Correo, Tel FROM pedidos INNER JOIN clientes ON pedidos.clientes_idCliente = clientes.id_cliente INNER JOIN direccion ON pedidos.direccion_id_direccion = direccion.id_direccion WHERE id_pedido = %s'
            values = (id,)
            self._cursor.execute(sql, values)
            pedido = self._cursor.fetchone()

            return pedido
        except connector.Error as err:
            return (err) 

    def obtener_pedido(self, id):
        try:
            sql = 'SELECT ventas.id_venta, nombre, marca, precio, cantidad, (precio * cantidad) FROM AuxPedidos INNER JOIN ventas ON AuxPedidos.id_venta = ventas.id_venta INNER JOIN productos ON ventas.barcode = productos.id_barcode WHERE id_pedido = %s'
            values = (id,)
            self._cursor.execute(sql, values)
            productos = self._cursor.fetchall()

            return productos
        except connector.Error as err:
            return (err)


    def read_all(self):
        try:
            sql = 'SELECT * FROM pedidos'
            self._cursor.execute(sql)
            pedido= self._cursor.fetchall()

            return pedido
        except connector.Error as err:
            return (err) 

    def read_fechas(self, lastdate, firstdate):
        try:
            sql = 'SELECT * FROM pedidos WHERE fecha <= %s AND fecha >= %s'

            values = (lastdate,firstdate)
            
            self._cursor.execute(sql, values)
            pedido = self._cursor.fetchall()

            return pedido
        except connector.Error as err:
            return (err)        

    def update(self, id_pedido, status_envio= '', fecha = '', clientes_idCliente = '',direccion_id_direccion = ''):
        fields = []
        val = []

        if id_pedido !='':
            val.append(id_pedido)
            fields.append('id_pedido = %s')
        if  status_envio!='':
            val.append(status_envio)
            fields.append('status_envio = %s')
        if fecha !='':
            val.append(fecha )
            fields.append('fecha = %s')    
        if  clientes_idCliente!= '':
            val.append(clientes_idCliente)
            fields.append(' clientes_idCliente= %s')
        if  direccion_id_direccion!= '':
            val.append(direccion_id_direccion)
            fields.append(' direccion_id_direccion= %s')

        val.append(id_pedido)
        val = tuple(val)         
        try:
            sql = 'UPDATE pedidos  SET ' + ','.join(fields) +' WHERE id_pedido =%s'

            self._cursor.execute(sql,val)
            self._cnx.commit()

            return True


        except connector.Error as err:
            self._cnx.rollback()
            return(err)

    def delete(self, id):
        try:
            sql = 'DELETE FROM pedidos WHERE id_pedido = %s'
            values = (id,)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True
        except connector.Error as err:
            self._cnx.rollback()
            return (err)

    def create_aux(self,idpedido, idventa):
        try:
            sql = 'INSERT INTO AuxPedidos(id_pedido, id_venta) VALUES(%s, %s)'
            values = (idpedido, idventa)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return True
        except connector.Error as err:
            self._cnx.rollback()
            return(err) 

    def borrarRelacion(self, idpedido, idventa): 
        try:
            sql = 'DELETE FROM AuxPedidos WHERE id_pedido = %s AND id_venta 0 %s'
            values = (idpedido,idventa)

            self._cursor.execute(sql, values)
            self._cnx.commit()

            return self.__cursor.rowcount > 0
        except connector.Error as err:
            self._cnx.rollback()
            return (err)               