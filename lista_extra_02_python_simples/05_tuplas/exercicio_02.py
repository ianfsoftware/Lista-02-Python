def calcular_folha(salario):
    desconto = salario * 0.10
    liquido = salario - desconto
    return desconto, liquido


desconto, salario_liquido = calcular_folha(5000)

print("Desconto: R$", desconto, "| Salário Líquido: R$", salario_liquido)
