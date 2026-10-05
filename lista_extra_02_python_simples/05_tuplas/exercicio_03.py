vendas_dia = [
    ("Monitor", 900, 2),
    ("Teclado", 150, 5),
    ("Mouse", 80, 10)
]

for produto, preco, quantidade in vendas_dia:
    total = preco * quantidade
    print("Produto:", produto, "| Total: R$", total)
