texto = input("Eu irei analizar o seu texto!!! ")
total = len(texto)

base = texto.split()
base = len(''.join(base))

print(f"O tamanho total da seu texto é de {total} "
    f"e se desconsiderar-mos os espaços são {base}")