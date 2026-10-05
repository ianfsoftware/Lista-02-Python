precos = {"celular": 1500, "tablet": 2500, "notebook": 5000}

aumento = float(input("Digite o percentual de aumento: "))

for produto in precos:
    precos[produto] = precos[produto] + precos[produto] * aumento / 100

print(precos)
