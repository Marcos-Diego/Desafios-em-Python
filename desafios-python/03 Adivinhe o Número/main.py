import random
ram = random.randint(1, 100)
numero = input('Em qual numero eu estou pensando???  ')

while numero != 0.1:
    try:
        numero = int(float(numero))
    except:
        print("Isto é um numero?")
        print("Tente de novo")
        numero = input('Em qual numero eu estou pensando???  ')
        
    else:
        if numero == ram:
            print("Parabens você acerou!!!")
            print("Vamos jogar de novo!")
            ram = random.randint(1, 100)
            
        elif numero > ram:
            print("O numero que eu estou pensando é menor(-)...")
            
        elif numero < ram:
            print("O numero que eu estou pensando é maior(+)...")
                
        numero = input('Em qual numero eu estou pensando???  ')
