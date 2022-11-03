

# Faça um programa que leia e valide as seguintes informações:
listadeusuarios = []

def cadastrar_usuario(nome, idade, salario, sexo, estadocivil):
  cadastro = {"nome": nome, "idade": idade, "sexo": salario, "estadocivil": estadoc, 'salario':salario}
  listadeusuarios.append(cadastro)

nome = input("Digite seu nome: ")
while len(nome) <= 3:
  print("Erro! seu nome tem menos de 3 caracteres ")
  nome = str(input("Digite um nome válido: "))
  continue
idade = int(input("Digite sua idade: "))
while (idade>150) or (idade<0):
    print("Erro! Idade inválida.")
    idade = int(input("Digite uma idade válida: "))
    continue
sexo = str(input("Diogite seu sexo: ")).upper()
while sexo != 'F' and sexo != 'M':
  print('Digite uma opção válida')
  sexo = str(input('Digite um sexo válido: ')).upper()
  continue
salario = float(input("Digite seu salário "))
while salario <0:
    salario = float(input("Salário negativo, digite um salário válido: "))
    # Sexo: 'f' ou 'm';
estadoc = str(input("Digite seu estado civil (s,c,v,d)")).upper()
while estadoc != 'S' and estadoc != 'C' and estadoc != 'v' and estadoc != 'd':
    print("Estado civil inválido")
    estadoc = str(input("Digite seu estado civil (s,c,v,d)")).upper()
    print("Ok, você está {}".format(estadoc))
    continue
cadastrar_usuario(nome, idade, sexo, estadoc, salario)
print(listadeusuarios)




# Nome: maior que 3 caracteres;




# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.