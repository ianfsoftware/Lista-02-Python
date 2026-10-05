def converter_para_real(preco_dolar, cotacao):
    return preco_dolar * cotacao


def processar_lista_precos(precos, cotacao):
    for preco in precos:
        valor = converter_para_real(preco, cotacao)
        print("O item custa R$", valor)


precos_usd = [100, 50, 250]
cotacao = 5.20

processar_lista_precos(precos_usd, cotacao)
