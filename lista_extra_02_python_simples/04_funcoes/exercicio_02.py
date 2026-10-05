def calcular_iss(valor):
    if valor > 5000:
        return valor * 0.05
    else:
        return valor * 0.03


print("ISS de 8000:", calcular_iss(8000))
print("ISS de 2000:", calcular_iss(2000))
