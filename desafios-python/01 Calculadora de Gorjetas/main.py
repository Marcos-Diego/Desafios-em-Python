dinheiro = round(float(input('valor da conta: ')))
gorgeta = round(float(input("valor da porcentagem: ")))

gorgeta = gorgeta / 100 * dinheiro
dinheiro += gorgeta

print(f"O valor da gorjeta é R$ {gorgeta:.2f} e o total é R$ {dinheiro:.2f}")