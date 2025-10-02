def calcular_imc(peso, altura):
    altura **= 2
    imc = peso / altura
    return imc

def classificar_imc(imc):
    if imc >= 30:
        resultado = "com obesidade"
    elif imc >= 25:
        resultado = "sobre peso"
    elif imc >= 18.5:
        resultado  = "com o peso normal"
    else:
        resultado = "abaixo do peso"
    return resultado

while True:
    try:
        peso = float(input("Qual o seu peso? "))
        altura = float(input("Qual a sua altura? "))
        imc = calcular_imc(peso, altura)
        
        print(f"""O seu imc é {int(imc)}
ou seja você esta {classificar_imc(imc)}""")
        
    except:
        print("Você não colocou um numero invalido! Ex:69.4 e 1.70")