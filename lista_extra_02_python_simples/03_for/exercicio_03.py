estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
estoque_quantidades = [5, 12, 2, 8, 15]

for i in range(len(estoque_produtos)):
    if estoque_quantidades[i] < 8:
        print("ALERTA: O produto", estoque_produtos[i],
              "está com apenas", estoque_quantidades[i],
              "unidades no estoque!")
