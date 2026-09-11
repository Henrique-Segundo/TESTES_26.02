def calcular_desconto(valor, percentual):
    if valor < 0:
        raise ValueError("O valor não pode ser negativo")

    if percentual < 0 or percentual > 100:
        raise ValueError("Percentual inválido")

    desconto = valor * percentual / 100
    return valor - desconto