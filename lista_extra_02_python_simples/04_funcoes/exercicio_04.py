def quem_bateu_meta(vendedores, meta):
    for nome in vendedores:
        if vendedores[nome] >= meta:
            print("Vendedor", nome, "bateu a meta!")


equipe_vendas = {
    "João": 12000,
    "Maria": 9500,
    "Ricardo": 10000,
    "Fernanda": 15200,
    "Paulo": 5000
}

meta_objetivo = 10000

quem_bateu_meta(equipe_vendas, meta_objetivo)
