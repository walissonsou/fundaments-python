# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
sexo = (input("De acordo com seu sexo digite H para homem ou M para mulher  ")).upper()
if sexo == "H":
    altura: float = float(input("Qual a sua altura? "))
    calc = (72.7 * altura) - 58
    print('Seu pso ideal é {:.2f}kg'.format(calc))
elif sexo == "M":
    altura: float = float(input("Qual a sua altura? "))
    calc = (62.1*altura) - 44.7
    print('Seu pso ideal é {:.2f}kg '.format(calc))
    print('Fim')

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso: float = float(input("Quantos kg você pescou? "))
excedente = (50 - peso) * (-1)
if peso > 50:
    calc = excedente * 4
    str = 'excedente' if excedente == 1.0 else 'excedentes'
    print("Você pagará R${} por {}kg {}".format(calc, excedente, str))
elif peso <= 50:
    print("Ok, você está dentro do kg pescados permitidos diários")



# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
porHora: float = float(input('Quanto você recebe por hora? '))
porDia: float = float(input('Quantas horas você trabalha por dia? '))
DiaMes: float = float(input('Qauntas dias você trabalha ao mês? '))

# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# [X] salário bruto.
calcBruto= porHora * porDia *DiaMes
print('Seu salário bruto é R${:.2f}'.format(calcBruto))
# quanto pagou ao IR.
calcIR = calcBruto * 0.11
print('Você paga R${} ao INSS'.format(calcIR))
# quanto pagou ao INSS.
calcInss = calcBruto * 0.08
print('Você paga R${} ao INSS'.format(calcInss))
# quanto pagou ao sindicato
calcSind = calcBruto * 0.05
print('Você paga R${} ao sindicato'.format(calcSind))
# o salário líquido.
calcLiquido = calcBruto - (calcInss + calcSind + calcIR )
print('Seu salário líquido é R${}'.format(calcLiquido))
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).