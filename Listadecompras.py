#Lista = dict()
Produtos = list()
Qtdgramas = list()

while True:
    Nomeprod = input("Digite o produto: ")
    if Nomeprod == 'fim':
        break
    else:
        Produtos.append(Nomeprod)
        for Produto in Produtos:
            print("Digite a quantidade DIÁRIA em gramas de", Nomeprod)
            Qtd = int(input())
            Qtdgramas.append(Qtd)
            break

Lista = dict(zip(Produtos, Qtdgramas))
#Lista = {k: v for k, v in zip(Produtos, Qtdgramas)}

print(Lista)
for v,k in Lista.items():
    print('O consumo semanal de',v,'é',Lista[v] * 7,'Gramas')
