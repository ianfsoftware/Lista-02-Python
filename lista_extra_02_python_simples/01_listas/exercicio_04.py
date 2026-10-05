rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]

rota.extend(novas_cidades)
posicao = rota.index("Sorocaba")

print(rota)
print(posicao)
print("Sorocaba é a", posicao + 1, "ª cidade da rota")
