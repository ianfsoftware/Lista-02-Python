estoque = {"teclado": 50, "mouse": 120, "monitor": 30}

produto = input("Digite o nome do produto: ").strip().lower()

if produto in estoque:
    print("Quantidade disponível:", estoque[produto])
else:
    print("Produto não encontrado no sistema")
