# This is the code that visits the warehouse.
import sys
import Pyro4
import Pyro4.util
from caroneiro import Caroneiro

sys.excepthook = Pyro4.util.excepthook


#servidor = Pyro4.Proxy("PYRONAME:example.servidor")

nameserver = Pyro4.locateNS()
uri = nameserver.lookup("example.servidor")
servidor = Pyro4.Proxy(uri)

cliente = Caroneiro()
cliente.acessar(servidor)