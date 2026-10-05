precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]

nome = input("Digite o nome do produto: ").strip().title()

if nome in vinhos:
    novo_preco = float(input("Digite o novo preço: ").replace(",", "."))
    posicao = vinhos.index(nome)
    precos[posicao] = novo_preco

    print(vinhos)
    print(precos)
else:
    print("Produto não encontrado.")
