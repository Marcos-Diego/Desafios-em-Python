import random

lista = ["ola", "mundo", "cruel", "asqueroso", "triste"]

enter = input("Aperte em enter para gerar uma citação: ")
citacao = random.choice(lista)

while enter != 1:
    if enter == "":
        citacao = random.choice(lista)
        enter = input(f"{citacao} ")
    else:
        enter = input("Aperte em enter para gerar uma citação: ")