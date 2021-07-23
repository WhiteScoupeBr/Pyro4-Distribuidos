from __future__ import with_statement
import Pyro4
@Pyro4.expose
class CallbackServer(object):
    def doCallback(self, callback):
        print("server: doing callback 1 to client\n")
        docall = Pyro4.Proxy(callback)
        docall.call()
       
        print("got an exception from the callback.")
        print("".join(Pyro4.util.getPyroTraceback()))
        print("server: doing callback 2 to client")
        


def main():
    Pyro4.Daemon.serveSimple(
            {
                CallbackServer: "example.teste"
            },
            ns = True)

if __name__=="__main__":
    main()