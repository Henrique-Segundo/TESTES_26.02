def calcular_media(nota1, nota2, nota3):
    notas = [nota1, nota2, nota3]

    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10")
    return sum(notas) / 3

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"