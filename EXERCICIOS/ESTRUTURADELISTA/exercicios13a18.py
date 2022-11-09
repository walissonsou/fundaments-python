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


# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta
# em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa
# deve ser encerrado quando não for informado o nome do atleta .A saída do programa deve
# ser conforme o exemplo abaixo:

atletas = []

while True:
    nome = input(
        "Digite o nome do atleta ou enter para encerrar: "
    )
    if nome == "":
        break

    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
        "melhor_salto": 0,
        "pior_salto": 0
    }
for i in range(5):
    atleta.get("saltos").append(
        float(input(f'Distancia primeiro salto: {i+1}'))
    )
    atleta.get("saltos").sort()  # ? Ordena a lista
    atleta["pior_salto"] = atleta.get("saltos").pop(0)
    atleta["melhor_salto"] = atleta.get("saltos").pop()
    atleta["media"] = sum(atleta.get("saltos")) / 3
    print(
        f"\nMelhor salto: {atleta.get('melhor_salto'):.1f} m"
        f"\nPior salto: {atleta.get('pior_salto'):.1f} m"
        f"\nMédia dos demais saltos: {atleta.get('media'):.1f} m\n"
    )
    atletas.append(atleta)

print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")
    print('-------------Fim__________')

# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita
# a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
#
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
sistemas = [0] * 6
while True:
    while True:
        opcao = int(input('Digite a opção: '))
        if opcao > 6 or opcao < 0:
            print('Opção inválida.')
        else:
            break
    if opcao == 0:
        break
    sistemas[opcao - 1] = sistemas[opcao - 1] + 1

print('Sistema Operacional     Votos  %')
print('----------------------------------')
contagem = 0
melhor = 0
melhorSistema = ''
percentual = 0

for s in sistemas: ### [11, 7, 4, 6, 0, 0]
    print('%s   %d   %.2f%%' % (opcoes[contagem],  s,(s * 100) / sum(sistemas) ))
    if s > melhor:
        melhor = s
        melhorSis = opcoes[contagem]
        perc = (s * 100) / sum(sistemas)
    contagem += 1

print('----------------------------------')
print('Total   %d' % sum(sistemas))
print('O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f dos votos.' % (melhorSis, melhor, perc))
