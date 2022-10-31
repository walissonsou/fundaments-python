valores=[]
equipamentos=[]
seriais=[]
departamentos=[]
resposta="S"
while resposta == "S":
    equipamentos.append((input("Equipamento: ")))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero serial: ")))
    departamentos.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar e aperte ENTER para imprimir os resultados: ").upper()
                        # range(start, stop, step)
for indice in range (0,len(equipamentos)):
    print("\nEquipamento...: ",(indice+1))
    print("Equipamento...: ", equipamentos[indice])
    print("valores...: ",valores[indice])
    print("seriais...: ",seriais[indice])
    print("departamentos...: ",departamentos[indice])

