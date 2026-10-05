def analisar_vendas(vendas):
    total = sum(vendas)
    media = total / len(vendas)
    return total, media


dados_filiais = {
    "Matriz": [10000, 15000, 20000],
    "Filial Sul": [5000, 7000]
}

for nome in dados_filiais:
    total, media = analisar_vendas(dados_filiais[nome])
    print("Filial", nome, "-> Total: R$", total, ", Média: R$", media)
