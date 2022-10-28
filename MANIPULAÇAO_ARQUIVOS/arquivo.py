basededados = []

with open('iris.data', "r") as arquivo:
#raedlines -> Retorne todas as linhas do arquivo,
# como uma lista onde cada linha é um item no
# objeto de lista
    for registro in arquivo.readlines():
        basededados.append(registro.split(","))
    print(basededados)

print(float(basededados[0][1]) + float(basededados[0][0]))
