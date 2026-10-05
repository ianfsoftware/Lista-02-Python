vendas = [2000, 5000, 1000, 8000, 3000]

total = 0

for venda in vendas:
    if venda > 4000:
        total = total + venda * 0.10
    else:
        total = total + venda * 0.05

print("Total de comissão:", total)
