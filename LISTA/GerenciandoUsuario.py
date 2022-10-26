from LISTA.Funcoes import *

usuarios = {}
usuario = [{"Caio":{"foo":"bar"}}, {"Tx":{"x":"y"}}, {"Kdu":{"a":"b"}}]
opcao = perguntar()




while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L" or opcao =="PE":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        print("Jaja eu faço")
    if opcao == "E":
        excluir(usuarios)
    if opcao == "L":
        listar(usuarios)

    opcao = perguntar()
