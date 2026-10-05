vendas_regiao = {
    "Norte": 15000,
    "Sul": 22000,
    "Leste": 18000,
    "Oeste": 25000
}

valores = list(vendas_regiao.values())

total = sum(valores)
media = total / len(valores)

print("Faturamento total:", total)
print("Faturamento médio:", media)
