while True:
    escolha = input('''1. Adicionar
2. Pesquisar
3. Remover
4. Sair
 ''')
    
    try:
        escolha = int(escolha)
        if escolha > 4:
            raise
        
        match escolha:
            case 1:
                nome = input("Nome do contato: ")
                numero = int(input("Numero: "))
                nome = {"Nome do contato": "???",
                        "Numero do contato": "???"}
                
                info["Nome do contato"] = nome
                info["Numero do contato"] = numero
                
            case 2:
                dica = input("Nome? ")
                
                
            case 3:
                quem = input("Quem você quer deletar? ")
                
                
            case 4:
                break
    except:
        print("Esta não é uma escolha valida! Escolha novamente!")
