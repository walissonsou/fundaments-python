# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
base = int(input("Qual a base do quadrado? "))
altura = int(input("Qual a altura do quadrado?"))
area = base * altura
areadobro = area * 2
print('A area do quadrado é: {}'.format(area))
print('A dobro da area é: {}'.format(areadobro))
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
porHora = int(input("Quanto você recebe por hora? "))
horasPorDia = int(input("Quantas horas você trabalha por dia? "))
diasPorMes = int(input("Quantos dias você trabalha ao mês? "))
calc = porHora * horasPorDia * diasPorMes
print('Você recebe R${} por mês'.format(calc))
# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
temperaturef = float(input("Digite a temperatura que você quer transformar em Celsius: "))
calcf = 5 * ((temperaturef-32)/9)
print('A temperatura em Celsius é {:.2f}'.format(calcf))
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temperaturec = float(input("Digite a temperatura que você quer transformar em Fahrenheit: "))
calcc = temperaturec * 1.8 + 32
print('A temperatura em Celsius é {:.2f}'.format(calcc))
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
real1 = float(input("Digite outro número real: "))
# o produto do dobro do primeiro com metade do segundo .
calc1 = (num1*2) * (num2/2)
print(calc1)
# a soma do triplo do primeiro com o terceiro.
calc2 = num2*3 + real1
print(calc2)
# o terceiro elevado ao cubo.
calc3 = real1**3
print(calc3)
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Qual a sua altura? "))
pesoIdeal = (72.7 * altura) - 58
print('Seu peso ideal é {}'.format(pesoIdeal))