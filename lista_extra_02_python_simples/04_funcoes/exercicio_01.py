def padronizar_texto(texto):
    return texto.strip().title()


produtos_baguncados = [
    " iphone 13 ",
    "MACBOOK PRO ",
    " aIrPoDs Pro",
    "iPad mini ",
    " caixa de som bluetooth "
]

for produto in produtos_baguncados:
    print(padronizar_texto(produto))
