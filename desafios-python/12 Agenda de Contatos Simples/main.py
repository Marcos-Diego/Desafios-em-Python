contatos = {}
def new(x, y):
    NoNu = f"{x} {y}"
    contatos[NoNu] = {f"Nome: {x}": f"Numero: {y}"}
    contatos.update(contatos)

def deletar():
    while True:
        quem = input("Quem você quer deletar? ")
        quantos = []
        for x in contatos:
            if quem in x: quantos.append(x)

        else:
            chave = len(quantos)
            match chave:
                case 0:
                    print("Contato não encontrada")
                    break
                case 1:
                    quantos = quantos[0]
                    contatos.pop(quantos)
                    break
                case _:
                    print("Por favor seja mais especifico! "
                          "Qual desses você deseja deletar?")
                    for x in quantos:
                        print(contatos[x])
                    confirm = input('''Seu contato esta aqui?
1. Sim/Continuar
*. Não/Sair
 ''')
                    if confirm != "1": break
                    
while True:
    escolha = input('''1. Adicionar
2. Pesquisar
3. Remover
4. Sair
 ''')
    
    try:
        escolha = int(escolha)
        if escolha > 4: raise
        
    except:
        print("Esta não é uma escolha valida! Escolha novamente!")
        
    else:
        match escolha:
            case 1:
                nome = input("Nome do contato: ")
                numero = int(input("Numero: "))
                new(nome, numero)
                
            case 2:
                achar = input("Qual o numero ou nome do contato? ")
                for x in contatos:
                    if achar in x:
                        print(contatos[x])
                        
            case 3:
                deletar()
      
            case 4:
                break