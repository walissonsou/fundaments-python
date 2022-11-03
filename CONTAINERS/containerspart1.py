                    # Listas - elas aceitam tudo = [x,y,z]
a=[[1,2,3,4]]
print(a[0][0])
# saída 1
# Slice - fatiar a lista
n = [0,1,2,3,4,5,6,7,8]
n[0] #0
n[6:] # [6,7,8]
n[:-6] # [0,1,2,3] do nada até menos 6
# Explicando com exemplos
l = [1,2,3,4,5,6,7,8,9]

print(l[-1]) # saída: 9 a lista vem andando de trás para frente
print(l[:-1]) # saída: 1,2,3,4,5,6,7,8 a lista remove o ultimo ou seja:
# -1 = 9, entao ele começa a contar do 8:  8,7,5,6,4,3,2,1
# dois pontos: é o step(passo)
l[::2] # inicia do primeiro e a saída: [1,3,5,9]
l[1::2] # inicia do segundo e a saída [2,4,8,10]
# Lista dentro da lista é matriz
matriz = [[1,2], [3,4,5], [7,8,9]]


# métodos x = [1,2,3]

x.append(4) -> insere no ultimo elemento da lista
x.insert(4) -> insere no primeiro item da lista, recebe dois parametros (posicao, item)
x.remove(2) -> REMOVE O ELEMENTO DA LISTA, mas a posição estará lá.
x.count(2) -> Retorna 1, pois retorna quantas aparições contém na minha lista
x.pop(2) -> Retorna [1,2], pois removeu o ultimo Retira o ultimo elemento da lista e retorna o valor
x.reverse(1) -> Retorna [3,2,1], pois m uda a posição da lista completa.

Em outras palavras:
append -> Fila, entra na ultima posicao.
insert -> Lista, entra na posicao q eu quiser, por padrao na primeira.
pop -> Pilha, lei de quem chega primeiro sai primeiro, remove o ultimo elemento.


                    ## Tuplas -> são listas IMUTÁVEIS ()

# Pode atribuir novos valores c/ setItem
a = ('ramos', 'lucas', 'caderno', [])
a[3].append(4) # ('ramos', 'lucas', 'caderno', [4])

x.count(2) -> tipo find, verifica quantos "2" tem na tupla
x.index(2) -> retorna a posição

# Por que a tupla é tão interessante?
# usadas para armazenar coleções de dados heterogêneos
#(como a tupla produzida pela função enumerate nativa).


# O que são hashable? - Conjuntos
# São coisas que não variam e continuam do mesmo jeito
# uma lista não pode ter um hash pois sempre irá variar
# shash(tuple()) -> 432423432


                        ## Conjuntos {}
 x = { 1,2,3}; y = { 3,4,5}
 x.union(y) -> {1,2,3,4,5}
 x.difference(y) -> {1,2}
 x.discard(1) => {2,3}
 x.pop() -> {2,3} # remove o primeiro item e nos trás
 x.update(y) -> { 1,2,3,4,5}
 x.intersection(y) -> {3}

                        ## Dicionários {}

# A chave chave necessáriamente deve ser hashable
# Os valores podem ser qualquer coisa
# Similar a um json
" Pessoa ={
'nome': 'walisson',
'profissao': 'programador'
}

# Toda vez que chamar a chave de um dicionário ele retornará um valor
Exemplo: x= {'Maria': 50, "José": 25}

x['Maria'] -> # 50
x['Maria'] = 10 -> # x= {'Maria': 10, "José": 25}
x.popitem() -> # ('José', 25) # retira o primeiro valor e trás de volta
x.keys() -> # ['Maria', 'José']
x.values() -> # [50,25]
x.setdefault('Calors') -> # acrescenta a key Calors na lista


a = {'Live': [1,2,3,4]}
a['Live'] -> [1,2,3,4]
                    # atribuir um novo valor:
a["Python"] = 17
a = {'Live': [1,2,3,4], 'Python': 17}
# para ter acesso as keys:
a.keys()
#retorna um tipo de dado que não é uma lista, parece ser uma
#lista devo transformá-la
dictkeys(['Live', 'python'])
list(a.keys())
['Live', 'Python']

a.items() -> retorna tudo ([('Live': [1,2,3,4]), ('Python': 17)])
# Embora ser uma lista, não suporta indexação
                    list.(a.items())[0][0]
                    # vou buscar um item 0, a chave 0



                          # Colections
from collections import Counter
# a funcao do counter é contar quantos itens existem na variavel

### Counter
Counter('eduardo')
Counter({'a': 1, 'd': 2....})
#deque

d = deque([1,2,3,4,5,7], maxlen=10)
d.append(4) -> adiciona no final
