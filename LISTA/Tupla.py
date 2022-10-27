usuarios = {}
emails = ["xcvbn@gmail.com", "qweasd@hotmail.com"]


tupla = list(enumerate(emails))
print(tupla)

for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
  # dicionario com a chave da tupla.
    usuarios[tupla[chave]]=[input("Digite o nome"), input("Digite o nível")]

for (chave, valor) in usuarios.items():
    print("Usuário...:", chave[0])
    print("Email...:", chave[1])
    print("Nome...:", chave[0])
    print("Nível...:", chave[1])