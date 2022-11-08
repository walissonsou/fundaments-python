# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
# em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas
# temperaturas acima da média anual,# e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
temperatura = []
def cadastrar_temperaturas(jan,fev,mar,abr,maio,jun):
    cadastro = {'lugar': lugar, "jan": jan, "fev": fev, "mar": mar, 'abr': abr, "maio": maio, "jun": jun}
    temperatura.append(cadastro['jan'])
    temperatura.append(cadastro['fev'])
    temperatura.append(cadastro['mar'])
    temperatura.append(cadastro['abr'])
    temperatura.append(cadastro['maio'])
    temperatura.append(cadastro['jun'])

lugar = input(f'Digite o nome do lugar: ').strip()
jan = float(input('Digite a temperatura de janeiro: '))
fev = float(input('Digite a temperatura de fevereiro: '))
mar = float(input('Digite a temperatura de março: '))
abr = float(input('Digite a temperatura de abril: '))
maio = float(input('Digite a temperatura de maio: '))
jun = float(input('Digite a temperatura de junho: '))

cadastrar_temperaturas(jan,fev,mar,abr,maio,jun)
media = sum(temperatura) / len(temperatura)
print(f'A média da cidade digitada é {media:.2f}')
print(temperatura)