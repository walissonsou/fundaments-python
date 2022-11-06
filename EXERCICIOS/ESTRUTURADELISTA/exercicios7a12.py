import numpy
# Onde armazeno meus numeros
numeros = []
# Onde está no loop
i = 0
# Loop apenas para voltar pro começo caso um número esteja inválido
while len(numeros) != 5:
    i += 1
    print("Diga o número " + str(i) + "º:")
    try:
        numero = int(input())
    except:
        print("Número inválido.")
        i -= 1
        continue
    numeros.append(numero)
# Mostrar os números

print("Números: " + ", ".join(str(numero) for numero in numeros))
soma = sum(numeros)
print("Soma: " + str(soma))

## para multiplicação, como nao temos um método, temos que fazer um loop como lá acima

# sem biblioteca

multi = 1
for numero in numeros:
    multi = multi * numero
print(multi)

## com biblioteca
result1 = numpy.prod(numeros)
print("Multiplicação: " + str(result1))
print('Fim')
# 8 Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
# informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

listaidade = []
listaaltura = []
def cadastrar_idade(idade):
    cadastroi = {'idade': idade}
    listaidade.append(cadastroi)

def cadastrar_altura(altura):
    cadastroa = {'altura': altura}
    listaaltura.append(cadastroa)

for i in range(2):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite a sua altura: "))
    cadastrar_idade(idade)
    cadastrar_altura(altura)

print(listaaltura)
print(listaidade)
listaidade.reverse()
print("reverse", listaidade)
listaaltura.reverse()
print("reverse", listaaltura)
# OU
print(listaidade[::-1])
print(listaaltura[::-1])

print("fim ")


# 9 Faça um Programa que leia um vetor A com 10 números inteiros, calcule e
# mostre a soma dos quadrados dos elementos do vetor.
# 10 Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
#  11 Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
# 12 Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.