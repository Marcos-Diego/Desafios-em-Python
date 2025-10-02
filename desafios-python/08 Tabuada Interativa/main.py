numero = input("Qual a tabuada que você gostaria de ver? ")

while numero != 0.1:
    try:
        numero = int(numero)
        for x in range(1, 11):
            print(f"{numero} X {x} = {numero * x}")
    except:
        numero = input("Por favor digite um numero valido(EX: -1, 0.5, 21)! ")
    
    teste = input("Quer ver outra tabuada? ")
    teste = teste.lower()
    if teste in ["sim", "s", "y", 'yes']: #chatGPT (com "or" so retornava true)
        numero = input("Qual a tabuada que você gostaria de ver? ")
    elif teste in ["não", "n"]: #chatGPT
        break
