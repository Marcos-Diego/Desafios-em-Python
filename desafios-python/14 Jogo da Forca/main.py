import random

def numero(x, y):
    return [index for index, elemento in enumerate(y)
            if x == elemento]
    #for index, elemento in enumerate(y):
     #   tente = (index, elemento)
      #  if x == elemento:
       #     return [index]

palavras = ["amar", "chorar", "cantar", "cão", "gato", "coelho", "lagarto", "blusa", "escola", "praia", "floresta"]
while True:
    visto = []
    tentativas = 5
    escolha = list(random.choice(palavras))
    tamanho = len(escolha)
    espaços = ["_"] * tamanho

    while True:
        if espaços != escolha:
            print(" ".join(espaços))
            
            chute = ((input("Chute uma letra! ")).lower()).strip()
            
            if chute in visto:
                print("Você já fez essa tentativa! ")

            elif chute in escolha:
                visto.append(chute)
                achado = numero(chute, escolha)
                
                for x in achado:
                    espaços[x] = chute
                
            else:
                print("Você errou!")
                tentativas -= 1
                if tentativas == 0:
                    print("E perdeu! Vamos de novo")
                    break
        else:
            print("Você ganhou! Vamos de novo")
            break
    
