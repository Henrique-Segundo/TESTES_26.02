def classificar_idade(idade):
    if idade < 12:
        return "criança"
    elif idade < 18:
        return "adolescente"
    else:
        return "adulto"