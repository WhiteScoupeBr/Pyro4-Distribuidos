# This is the code that visits the servidor.
import sys
import Pyro4
import Pyro4.util
from carona import Carona

sys.excepthook = Pyro4.util.excepthook

nameserver = Pyro4.locateNS()
uri = nameserver.lookup("example.servidor")
servidor = Pyro4.Proxy(uri)


cliente = Carona()
cliente.acessar(servidor)