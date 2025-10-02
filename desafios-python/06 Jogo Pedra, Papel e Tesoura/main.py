import random

lista = ["pedra", "papel", "tesouta"]
text = 'Vamos jogar pedra, papel e tesoura!'

print(text)
me = input("(Escolha entre pedra, papel e tesoura) ")
pc = random.choice(lista)

#Error de Escopo
#text = 'Vamos jogar pedra, papel e tesoura!'
#def base(text):
#    print(text)
#   me = input("(Escolha entre pedra, papel e tesoura) ")
#    pc = random.choice(lista)
    
while me != 1:
    me = me.lower()
    #print(me, pc)
    if me == "papel" or me == "pedra" or me == "tesoura":
        if me == pc:
            print("Deu empate...")
            me = input("(Escolha entre pedra, papel e tesoura) ")
            pc = random.choice(lista)
            
        elif me == "papel" and pc == "pedra":
            print("você venceu!!!")
            me = input("(Escolha entre pedra, papel e tesoura) ")
            pc = random.choice(lista)
            
        elif me == "pedra" and pc == "tesoura":
            print("você venceu!!!")
            me = input("(Escolha entre pedra, papel e tesoura) ")
            pc = random.choice(lista)
            
        elif me == "tesoura" and pc == "papel":
            print("você venceu!!!")
            me = input("(Escolha entre pedra, papel e tesoura) ")
            pc = random.choice(lista)
            
        else:
            print("você Perdeu :(")
            me = input("(Escolha entre pedra, papel e tesoura) ")
            pc = random.choice(lista)
    else:
        print("Escolha corretamente!")
        me = input("(Escolha entre pedra, papel e tesoura) ")
        pc = random.choice(lista)