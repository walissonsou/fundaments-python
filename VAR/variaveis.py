nome=input("Digite seu nome: ")
isaluno=input("Está matriculado em uma faculdade? ").upper()
nomeDaFaculdade=input("Qual sua faculdade? ")
mediaAnualDeTodosAlunos=float(input("Digite a média "))
if isaluno=="SIM":
    print("Ok, você é aluno")
if isaluno=="NAO":
    print("Ok, você não é aluno")
elif mediaAnualDeTodosAlunos>= 5:
    print("Beleza", nome, "a sua faculdade ", nomeDaFaculdade, "está nos padrões do mec")

else:
    print("Que pena", nome, "a", nomeDaFaculdade, "está baixo do requisitado pelo MEC")
