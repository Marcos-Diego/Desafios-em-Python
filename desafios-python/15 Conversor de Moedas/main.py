moedas = {
    "USD": 1,
    "BRL": 5.33,
    "EUR": 0.85,
    "JPY": 147.04,
    "GBT": 0.74}


def converter(v, o, c):
    x = v / moedas[o]
    y = x * moedas[c]
    print(round(y, 2))

while True:
    try:
        origem = (input("Qual a sua moeda para seu convertida? ")).upper()
        if origem not in moedas: raise print("Moeda não encontrada. ex:BRL")
        
        valor = float(input("Qual o valor que você quer converter: "))
        
        converçao = (input("Para qual moeda você quer converter? ")).upper()
        if converçao not in moedas: raise print("Moeda não encontrada. ex:EUR")
    except:
        if valor is not float: raise print("Este não é valor valido. ex:27.30")
    else:
        converter(valor, origem, converçao)