# Faça um Programa que peça dois números e imprima o maior deles.
num1: float = float(input('Digite um numero: '))
num2: float = float(input('Digite outro número '))
maior = 'O {} é maior'.format(num1) if num1 > num2 else 'O {} é maior'.format(num2)
print(maior)
print('Fim')
# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num1: float = float(input('Digite um numero: '))
positivoornegativo = 'O {} é positivo'.format(num1) if num1 > 0 else 'O {} é negativo'.format(num1)
print(positivoornegativo)
print('Fim')
# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = (input("De acordo com seu sexo digite H para homem ou M para mulher  ")).upper()
while sexo != 'H' or sexo != 'M':
    print('Digite uma opção válida')
    sexo = (input("De acordo com seu sexo digite H para homem ou M para mulher  ")).upper()
    if sexo == 'H':
        print('Você é homem')
        break
    elif sexo == 'M':
         print('Você é mulher')
         break
print('Fim')


# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vogals = ['A', 'E', 'I', 'O', 'U']
letra: str = str(input('Digite uma letra: ')).upper()
print("Checando se a letra é uma vogal ou consoante...")
if (letra in vogals):
    print("É uma vogal")
else:
    print('Não é vogal')


# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
nota1: float = float(input('Digite a primeira nota: '))
nota2: float = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
if media >= 7:
    print('Aprovado')
# A mensagem "Reprovado", se a média for menor do que sete;
if media < 7:
    print('Reprovado')
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
if media == 10:
    print('Aprovado com Distinção')
print('Fim')
#  Faça um Programa que leia três números e mostre o maior deles.
listanum = []
maior = 0
menor = 1000000
for posicao in range(0,3):
    listanum.append(float(input('Digite a um numero para posição {}: '.format(posicao+1))))
    print(listanum)
    if posicao == 0:
        maior = menor = listanum[posicao]
    else:
        if listanum[posicao] > maior:
            maior = listanum[posicao]
        if listanum[posicao] < menor:
            menor = listanum[posicao]
print('Você digitou os valores {}'.format(listanum))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))



