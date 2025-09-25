visor = 0
print(visor)
commander = input('Qual o seu comando(+, -, x2 ou reset)? ')

while commander != 1:
    if commander == "+":
        visor += 1
        print(visor)
        
    elif commander == "-":
        visor -= 1
        print(visor)
        
    elif commander == "reset":
        visor = 0
        print(visor)
       
    elif commander == "x2":
        visor *= 2
        print(visor)
        
    elif commander == "":
        print(visor)
        print("Isto não é um comando valido! Tente novamente")
        
    else:
        print(visor)
        print("Isto não é um comando valido! Tente novamente")
        
    commander = input('Qual o seu comando(+, -, sair)? ')

