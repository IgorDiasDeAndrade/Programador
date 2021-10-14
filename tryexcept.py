nome = input('insira o arquivo: ')
mediador = open(nome)

contar = dict()
for linha in mediador:
    palavras = linha.split()
    for palavra in palavras:
        contar[palavra] = contar.get(palavra,0) + 1

grandeconta = None
grandepalavra = None
for palavra,conta in contar.items():
    if grandeconta is None or conta > grandeconta:
        grandepalavra = palavra
        grandeconta = conta

print(grandepalavra, grandeconta)
print(contar)
