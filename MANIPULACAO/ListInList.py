names=[];
resposta = "S";
while resposta == "S":
    print("Bem vindo à central dos planos de saúde")
    planodesaude=[input("nome do Plano: "),
                  float(input("Valor da mensalidade: ")),
                  int(input("Código do plano: ")),
                  input("Nacionalidade do plano: ")]
    names.append(planodesaude)
    resposta = input("Digite \"S\" para continuar e ENTER para sair: ").upper()

for plano in names:
    print("Nome :", plano[0])
    print("Valor da mensalidade :", plano[1])
    print("Código do plano: :", plano[2])
    print("Nacionalidade do plano :", plano[3])

busca: str = input("\nDigite o nome do plano de saúde que deseja buscar: ")
for plano in names:
    if busca == plano[0]:
        print("Valor da mensalidade", plano[1])
        print("Código do plano: ", plano[2])

mensalidade: str = input("\nDigite o nome do plano de saúde que vai sofrer aumento na mensalidade: ")
for plano in names:
    if mensalidade == plano[0]:
        print("Valor antigo: ", plano[1])
        plano[1] = plano[1] * 0.9
        print("O novo valor é: ", plano[1])

serial=int(input("\nDigite o código do plano para remover da nossa lista: "))
for plano in names:
    if plano[2]==serial:
        names.remove(plano)

for plano in names:
    print("Nome: ", plano[0])
    print("Mensalidade: ", plano[1])
    print("Código: ", plano[2])
    print("Nacionalidade: ", plano[3])

valores=[]
for plano in names:
    valores.append(plano[1])
    if len(valores) > 0:
        print("Plano de saúde mais caro", max(valores))
        print("Plano de saúde mais barato", min(valores))
        print("Soma de mensalidades", sum(valores))
