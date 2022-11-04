#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
vetor = [1,2,3,4,5]
i = 0
while i < len(vetor):
    print(vetor[i])
    i += 1
#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numerosReais = []
print("Digite os 10 número reais")
for i in range(10):
    numerosReais.append(int(input('Numero' + str(i+1)+ ':\n')))
numerosReais.reverse()
print(numerosReais)
# Ou
vetor = [1,2,3,4,5,6,8,9,11,432,312321,3123213]
vetor.reverse()
print(vetor)
print('FIM')
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
print("Digite suas novas dos 4 trimestres do ano de 2022")
for i in range(2):
    notas.append(float(input('Nota do {} trimestre'.format(str(i + 1)))))
media = (sum(notas) / len(notas))
print(media)
print('FIM')
#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
numerodecaracteres = int(input("Informe o numero caracteres: "))
listadenomes = []
for i in range(0, numerodecaracteres):
    caracteres= str(input("Insira o caractere n {}".format(i+1))).upper()
    listadenomes.append(caracteres)
print("A sua lista é: {}".format(listadenomes))
vogais = 'AEIOU'
for p in listadenomes:
    print(f'Na palabra {p} temos vogais')
    for letra in p:
        if letra in vogais:
            print(letra, end=' ')

def contaraSoma(listadenomes):
    soma = 0
    for i in listadenomes:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o'or i == 'u':
            continue
        else:
            soma += 1
    print("Soma das consoantes é igual a: ", soma)
    return soma
contaraSoma(listadenomes)


#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.
numerodecaracteres = int(input("Informe a quantidade de numero: "))
todos = []
pares = []
impares = []
for i in range(0, numerodecaracteres):
    todos.append(int(input("Insira-os n {}: ".format(i + 1))))
print(f'Todos numeros: {todos}')

for numero in range(0, numerodecaracteres):
    if todos[numero] % 2 == 0:
         pares.append(todos[numero])
    else:
        impares.append(todos[numero])

print(f'Numeros pares {pares}' )
print(f'Numeros impares {impares}''\n')



#Faça um Programa que peça as quatro notas de 10 alunos, calcule
# e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
numerodealunos = int(input("Informe o numero de alunos que deseja cadastrar: "))
listadealunos = []

def cadastrar_notas(nome,nota1,nota2,nota3,nota4):
    for i in range(0, numerodealunos):
        cadastro ={"nome": nome, "nota1": nota1,"nota2": nota2, "nota3": nota3, "nota4": nota4}
        listadealunos.append(cadastro)

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
nota4 = float(input("Digite sua nota: "))


cadastrar_notas(nome,nota1,nota2,nota3,nota4)
print(listadealunos)