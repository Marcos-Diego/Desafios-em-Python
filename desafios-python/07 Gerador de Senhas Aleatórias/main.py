import random, string

listas = [string.ascii_letters, string.digits,
         string.punctuation]
listas = "".join(listas)
listas = list(listas)

while True:
    try:
        tamanho = int(input("Qual o tamanho da sua senha? "))
        fim = []
    except:
        print("Por favor digite um numero!")
    else:
        random.shuffle(listas)
        for x in range(tamanho):
            fim.append(listas[x])
            if x == (tamanho - 1):
                fim = ''.join(fim)
                print(fim)
                
            