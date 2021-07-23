from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input


class Carona(object):
    def __init__(self):
        self.nome = ''
        self.telefone = ''
        #implementar 
        self.chave = '123'
        self.id_noti = ''

    def acessar(self, servidor):
        self.cadastrar(servidor)
        self.inserir_carona(servidor)
        print("Arigato!")



    def cadastrar_notificacao(self, servidor,viagem):
            print("Cadastrando sua viagem para ser notificação...\n")
            nome = self.nome
            telefone = self.telefone
            item = {'nome':nome,'contato':telefone,'origem':viagem['origem'],'destino':viagem['destino'],'data':viagem['data']}
            self.id_noti = servidor.notificao_desejo_carona(item)
            print("O id da sua viagem é: ")
            print(self.id_noti)



    def cadastrar(self, servidor):
        nome = input("Insira seu nome: ").strip()
        telefone = input("Insira seu telefone: ").strip()
        if (nome and telefone):
            item = {'nome':nome,'telefone':telefone}
            servidor.cadastrar_usuario(item)
            print("Usuário cadastrado com sucesso! \n")
        else:
            print("Faltam dados! \n")



    def inserir_carona(self, servidor):
        print("Vamos cadastrar sua viagem desejada! \n")
        origem = input("Insira seu local de origem: ").strip()
        destino = input("Insira seu local de destino: ").strip()
        data = input("Insira a data no formato dd/mm/aaaa: ").strip()
        if (origem and destino and data):
            item = {'origem':origem,'destino':destino,'data':data}
            servidor.desejo_carona(item)
        notificacao = input("Deseja receber notificação caso alguma viagem atenda esses critérios? \n s para Sim \n n para Não\n").strip()
        if(notificacao == 's'):
            self.cadastrar_notificacao(servidor,item)
        else:
            print('ok :(\n')
    


    

