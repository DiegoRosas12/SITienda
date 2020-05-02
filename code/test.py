
#con herencia:

#pedidoModel = PedidoModel()
#print(pedidoModel.update('2','1','2020/04/24', 9000,'2'))

#print(pedidoModel.read_all())

from controller.controller import Controller


controller = Controller()

controller.start()