import sys
import Pyro4
import Pyro4.util

@Pyro4.expose
class Callback(object):
    
    @Pyro4.callback
    def call(self):
        print("callback received from server!")
        return 1//0    # crash!
    

daemon = Pyro4.Daemon()
callback = Callback()
teste = daemon.register(callback)
print(teste)

nameserver = Pyro4.locateNS()
uri = nameserver.lookup("example.teste")
servidor = Pyro4.Proxy(uri)

print("foi\n")
servidor.doCallback(teste)
print("foi2")
daemon.requestLoop()