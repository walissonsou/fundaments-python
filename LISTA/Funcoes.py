def perguntar():
   return input("O que deseja realizar?\n" +
                   "<I> - Para Inserir um usuário\n" +
                   "<P> - Para Pesquisar um usuário\n" +
                   "<E> - Para Excluir um usuário\n" +
                   "<L> - Para Listar um usuário\n" +
                   "<ENTER> - Para sair pressione enter\n").upper()
def inserir(dicionario):
   dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                    input("Digite a ultima data de acesso "),
                                                    input("Qual a última estação acessada: ").upper()]

   salvar(dicionario)
def pesquisar(dicionario):
    busca = input("\n Digite o o usuário que você quer pesquisar de acordo com o login: ").upper()
    for elemento in dicionario.copy():
        if busca in elemento:
            print(dicionario[busca])
def listar(dicionario):
        with open("bd.txt", "r") as arquivo:
            for linha in arquivo.readlines():
                print(linha)
def excluir(dicionario):
    excluir=input("\n Digite o o usuário que você quer excluir de acordo com o login: ").upper()
    try:
        with open("bd.txt", "r") as arquivo:
            lines = arquivo.readlines()
            with open('bd.txt', "w") as arquivo:
                for line in lines:
                    if line.strip(excluir):
                        arquivo.write('')
        print("Arquivo {} removido".format(excluir))

    except:
        print("Oops! someting error")

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write("\n" + chave + ":" + str(valor))



