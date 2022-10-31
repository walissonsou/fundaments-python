inventario=[]
resposta="S"
while resposta == "S":
    inventario.append((input("Equipamento: ")))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Numero serial: ")))
    inventario.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

    for itens in inventario:
        print(itens)