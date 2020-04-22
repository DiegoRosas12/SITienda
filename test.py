
#con herencia:

from model.clienteModel import clienteModel

clienteModel = clienteModel()
clienteModel.create("Mariana","Arce","Aguilar","mariana@hotmail.com",'4641660804')

print(clienteModel.read_all())