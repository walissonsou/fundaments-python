# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
preco1 = float(input("Qual preço do primeiro? "))
preco2 = float(input("Qual preço do primeiro? "))
preco3 = float(input("Qual preço do primeiro? "))

lista = [preco1, preco2, preco3]
print("O produto {} é o mais acessível!".format(min(lista)))


# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Primeiro? "))
num2 = float(input("Segundo? "))
num3 = float(input("Terceiro? "))

lista = [num1, num2, num3]
print(num1, '-', num2, '-', num3)

if num1 > num2 > num3:
    print(num1, num2, num3)
elif num2 > num1 > num3:
    print(num2, num1, num3)
elif num3 > num2 > num1:
    print(num3, num2, num1)
elif (num1 == num2 == num3) or (num2 == num1 == num3) or (num3 == num2 == num1):
    print("Números iguais")

                        #Resolução num2

lista = []
for n in range(3):
    n = int(input("Entre com um valor para N: "))
    lista.append(n)

lista.sort()
print(f'Lista na ordem crescente: ' ,lista)
lista.reverse()
print('Lista na ordem decrescente ', lista)


# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
# conforme o caso.



turno = str(input('Digite em que turno você estuda: M=maturnino, V=vespertino ou N-noturno: ').upper())

if turno == "NOTURNO" or turno == "N":
    print('Boa noite ;)')
elif turno == "MATUTINO" or turno == "M":
    print('Bom dia ;)')
elif turno == "VESPERTINO" or turno == "N":
    print("Boa tarde ;)")
else:
    print("Opção inválida")


# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.


salario = float(input("Qual o seu salário? "))

if salario <= 200:
    por20 = salario * 0.20 + salario
    print("O seu salário anterior era {}, após o reajuste ficou: {}".format(salario, por20))

elif salario >= 280 and salario <= 700:
    por15 = salario * 0.15 + salario
    print("O seu salário anterior era {}, após o reajuste ficou: {}".format(salario, por15))
elif salario >= 700 and salario <= 1500:
    por10 = salario * 0.10 + salario
    print("O seu salário anterior era {}, após o reajuste ficou: {}".format(salario, por10))
elif salario > 1500:
    por05 = salario * 0.05
    print("O seu salário anterior era {}, após o reajuste ficou: {}".format(salario, por05))


# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

preco = float(input("Qual preço da sua hora de trabalho? "))
horas = float(input("Quantas horas você trabalha por dia? "))
diames = int(input("quantos dias você trabalha ao mês? "))
salariob = preco * horas * diames
print("Seu salário bruto é R${}".format(salariob))
sindicato = salariob * 0.03
fgts = salariob * 0.11
salariol = salariob - sindicato
print("Seu salário líquido com descontos do sindicato é R${}".format(salariol))
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
    #         Salário Bruto: (5 * 220)        : R$ 1100,00
    #    (-) IR (5%)                     : R$   55,00
    #    (-) INSS ( 10%)                 : R$  110,00
    #    FGTS (11%)                      : R$  121,00
    #    Total de descontos              : R$  165,00

if salariob <= 900:
    print("O custo da empresa quanto ao IR está isento")
elif salariob > 900 or salariob <= 1500:
    por5 = salariob * 0.05 + salariob
    print("A empresa irá ter um custo de R${}".format(por5))
elif salariob > 1500 or salariob <= 2500:
    por10 = salariob * 0.10 + salariob
    print("A empresa irá ter um custo de R${}".format(por10))
elif salariob > 2500:
    por20 = salariob * 0.2 + salariob
    print("A empresa irá ter um custo de R${}".format(por20))
# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
numero = input('Digite um numero: ')

if numero == 1:
    print('1-Domingo')
elif numero == 2:
    print('2-Segunda')
elif numero == 3:
    print('3-Terça')
elif numero == 4:
    print('4-Quarta')
elif numero == 5:
    print('5-Quinta')
elif numero == 6:
    print('6-Sexta')
elif numero == 7:
    print('7-Sabádo')
else:
    print('Entrada invalida')