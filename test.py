from model.model import Model

m = Model()
print('Sucess')

"""
agregar un nuevo usuario.
m.create_cliente('Lupita', 'Perez Lopez','lupis@hotmail.com','464052328','Salamanca')
"""
"""
leer un solo cliente
client = m.read_cliente(6)
print(client)

"""

"""
clientes = m.read_all_clientes()
print(clientes)
"""
"""
actualizar cliente
m.update_cliente(8, Nombre = 'Carmen' )

m.create_producto('652018','Mouse','generico','8',200)
products = m.read_producto_between_price(300,2500)
print(products)
"""
print(m.create_pedido('652018','6','2020/04/10 17:14:00','oficina sur','3'))

m.close_db()
