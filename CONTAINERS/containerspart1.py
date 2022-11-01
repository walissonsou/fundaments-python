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


                    ## Tuplas -> são listas IMUTÁVEIS

