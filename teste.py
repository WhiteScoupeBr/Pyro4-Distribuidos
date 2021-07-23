


teste = [{'id':1},{'id':2}]

id_cancelar = 2

for dicts in teste:
    print(dicts)
    for key, value in dicts.items():
        if(value == id_cancelar):
            teste.remove(dicts)
            print(teste)