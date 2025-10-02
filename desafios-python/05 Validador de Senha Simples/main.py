senha = input("Escolha um senha: ")

while senha != 1:
    senha = len(senha)
    if senha >= 8:
        print("senha valida")
        break
    else:
        print("senha invalida")
        senha = input("Escolha um senha: ")