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


def pesquisar():{

}
def excluir():{

}

def listar():{

}