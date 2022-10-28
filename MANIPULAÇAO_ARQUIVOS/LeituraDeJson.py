import json

#with open("bd.json", "r") as arquivo:
#   dicionario = json.load(arquivo)
#   print(dicionario)

# as duas formas dao certo
# with open("bd.json", "r") as arquivo:
    #    dicionario = json.load(arquivo)
    #    for chave, dados in dicionario.items():
#        print(chave+ "\n" + str(dados))


dicionario = {
    "CHAVES": ["CHAVES 09", "14-04-2022", "RECP1"],
    "KIKO": ["KIKO 10", "14-04-2022", "RECP1"],
    "FLORINDA": ["FLORINDA 11", "14-04-2022", "RECP1"]
}

print(dicionario)
# dump 2 informações
with open("db1.json", "w") as arquivo1:
    json.dump((dicionario), arquivo1)