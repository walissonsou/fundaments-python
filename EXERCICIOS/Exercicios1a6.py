print("Alo Mundo")
# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero=input("Qual número você escolhe? ")
# print("O número informado foi: ", numero)
# Faça um Programa que peça dois números e imprima a soma.
sum1 = int(input("Escolha um número qualquer: "))
sum2 = int(input("Escolha outro número outro qualquer: "))
s = sum1 + sum2
print(' A soma entre {} e {} é {}'.format(sum1,sum2,s))
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
b1 = int(input("Nota 1 bimestre: "))
b2 = int(input("Nota 2 bimestre: "))
b3 = int(input("Nota 3 bimestre: "))
b4 = int(input("Nota 4 bimestre: "))
media = (b1+b2+b3+b4)/4
print(media)
# Faça um Programa que converta metros para centímetros.
metro = int(input("Digite o metro que você quer em centímetros: "))
convert = metro*100
print(convert)
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input("Digite o raio de um círculo em centimetros: "))
calc = 3.14 * raio**2
print(calc)