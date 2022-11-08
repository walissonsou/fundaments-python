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

# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5  como "Assassino". Caso contrário, ele será classificado como "Inocente".

pessoa = []
def investig(nome,telefone,local,mora,dinheiro,trabalho):
    cadastro = {'nome': nome, 'telefone': telefone, 'local': local, 'mora': mora, 'dinheiro': dinheiro, 'trabalho': trabalho}
    pessoa.append(cadastro['nome'])
    pessoa.append(cadastro['telefone'])
    pessoa.append(cadastro['local'])
    pessoa.append(cadastro['mora'])
    pessoa.append(cadastro['dinheiro'])
    pessoa.append(cadastro['trabalho'])
    print(pessoa)

nome = str(input("Qual seu nome? "))
telefone = int(input("Telefonou para vítima?  1/Sim ou 0/Não: "))
local = int(input("Esteve no local do crime?  1/Sim ou 0/Não: "))
mora = int(input("Mora perto da vítima?  1/Sim ou 0/Não: "))
dinheiro = int(input("Devia para a vítima?  1/Sim ou 0/Não: "))
trabalho = int(input("Já trabalhou com a vítima?  1/Sim ou 0/Não: "))
soma_respostas = telefone + local + mora + dinheiro + trabalho

investig(nome,telefone,local,mora,dinheiro,trabalho)
print(nome, soma_respostas)
if (soma_respostas < 2):
 print("\nInocente")
elif (soma_respostas == 2):
 print("\nSuspeita")
elif (3 <= soma_respostas <= 4):
 print("\nCúmplice")
elif (soma_respostas == 5):
 print("\nAssassino")


