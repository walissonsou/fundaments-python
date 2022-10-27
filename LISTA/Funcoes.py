def perguntar():
   return input("O que deseja realizar?\n" +
                   "<I> - Para Inserir um usuário\n" +
                   "<P> - Para Pesquisar um usuário\n" +
                   "<E> - Para Excluir um usuário\n" +
                   "<L> - Para Listar um usuário\n" +
                   "<ENTER> - Para sair pressione enter\n").upper()
def inserir(dicionario):
   dicionario[input("Digite o login: ").upper()] = [input("Digite o nome").upper(),
                                                    input("Digite a ultima data de acesso"),
                                                    input("Qual a última estação acessada: ").upper()]
def pesquisar(dicionario):
    busca = input("\n Digite o o usuário que você quer pesquisar de acordo com o login: ")
    for elemento in dicionario.copy():
        if busca in elemento:
            print(dicionario[busca])

def listar(dicionario):
        print(dicionario)

def excluir(dicionario):
    excluir=input("\n Digite o o usuário que você quer excluir de acordo com o login: ").upper()
    for elemento in dicionario.copy():
      if excluir in elemento:
        del dicionario[excluir]
        print("Usuário {} excluído.".format(excluir))
    print(dicionario)