tarefas = []
    
while True:
    #\r não estava funcionando
    escolha = input('''1. Adicionar tarefa
2. Listar tarefas
3. Remover tarefa
4. Sair
 ''')
    
    try:
        escolha = int(escolha)
        if escolha > 4:
            raise
    
    except:
        print("Esta não é uma escolha valida! Escolha novamente!")
        
    else:
        match escolha:
            case 1:
                texto = input("Qual é sua nova terefa? ")
                tarefas.append(texto)
            case 2:
                for index, elemento in enumerate(tarefas, start=1):
                    print(index, elemento)
                print("")
                    
            case 3:

                delet = int(input("Qual o numero da terefa "
                "que você deseja apagar? "))
                
                tarefas.pop(delet - 1)
            case 4:
                break