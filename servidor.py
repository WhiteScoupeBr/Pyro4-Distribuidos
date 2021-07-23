from __future__ import print_function
import Pyro4


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class Servidor(object):
    def __init__(self):
        self.usuario = []
        self.caroneiros = []
        self.caronas = []
        self.notificacao_caronas = []
        self.notificacao_caroneiros = []
        self.id_noti_desejo_carona = 0 
        self.id_noti_ofereco_carona = 1000


    def cadastrar_usuario(self, item):
        self.usuario.append(item)
        print(self.usuario)
    
    def desejo_carona(self, item):
        self.caronas.append(item)
        print(self.caronas)

    def notificao_desejo_carona(self,item):
        self.id_noti_desejo_carona += 1
        item['id'] = self.id_noti_desejo_carona
        self.notificacao_caronas.append(item)
        print(self.notificacao_caronas)
        return self.id_noti_desejo_carona 

    def ofereco_carona(self, item):
        self.caroneiros.append(item)
        print(self.caroneiros)


    def notificao_ofereco_carona(self,item):
        self.id_noti_ofereco_carona += 1
        item['id'] = self.id_noti_ofereco_carona
        self.notificacao_caroneiros.append(item)
        print(self.notificacao_caroneiros)
        return self.id_noti_ofereco_carona 

    
    def cancelar_carona(self,id_cancelar):
        for dicts in self.notificacao_caronas:
            for key,value in dicts.items():
                if (key == 'id'):
                    if(int(value) == int(id_cancelar)):
                        self.notificacao_caronas.remove(dicts)
                        print(self.notificacao_caronas)
                        return "Viagem removida!"
        
        print(self.notificacao_caronas)
        return "Id não está na Lista"


    def cancelar_caroneiro(self,id_cancelar):
        for dicts in self.notificacao_caroneiros:
            for key,value in dicts.items():
                if (key == 'id'):
                    if(int(value) == int(id_cancelar)):
                        self.notificacao_caroneiros.remove(dicts)
                        print(self.notificacao_caroneiros)
                        return "Viagem removida!"
        
        print(self.notificacao_caroneiros)
        return "Id não está na Lista"




def main():
    Pyro4.Daemon.serveSimple(
            {
                Servidor: "example.servidor"
            },
            ns = True)

if __name__=="__main__":
    main()