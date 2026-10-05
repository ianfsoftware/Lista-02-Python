def resumo_chamados(tempos):
    quantidade = len(tempos)
    maior_tempo = max(tempos)
    return quantidade, maior_tempo


tempos = [15, 45, 10, 120, 30]

quantidade, maior_tempo = resumo_chamados(tempos)

print("Quantidade de chamados:", quantidade)
print("Tempo máximo de espera:", maior_tempo, "minutos")
print("Atenção: o tempo máximo foi", maior_tempo, "minutos.")
