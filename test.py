
#con herencia:

from model.clienteModel import ClienteModel
from model.direccionModel import DireccionModel

direccionModel = DireccionModel()
direccionModel.delete(1)

print(direccionModel.read_all())