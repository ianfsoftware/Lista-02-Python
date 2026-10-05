metas = {"jan": 1000, "fev": 1200, "mar": 1100}
gastos = {"jan": 900, "fev": 1350, "mar": 1100}

for mes in metas:
    if gastos[mes] <= metas[mes]:
        print("Mês", mes, ": Dentro do orçamento.")
    else:
        diferenca = gastos[mes] - metas[mes]
        print("Mês", mes, ": Orçamento estourado em R$", diferenca)
