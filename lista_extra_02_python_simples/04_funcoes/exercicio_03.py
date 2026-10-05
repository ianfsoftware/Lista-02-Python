def analisar_margem(faturamento, custo):
    lucro = faturamento - custo
    margem = lucro / faturamento

    if margem >= 0.30:
        return "Margem Saudável"
    else:
        return "Margem Baixa"


print(analisar_margem(10000, 6000))
