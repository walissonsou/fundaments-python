equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(input("valores: "))
    seriais.append(input("seriais: "))
    departamentos.append(input("departamentos: "))
    resposta = input("Digite \"S\" para continuar ou pressione ENTER para sair: ").upper()

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
        if busca==equipamentos[indice]:
            print("Valor: ", valores[indice])
            print("Serial: ", seriais[indice])
