import pytest
from notas import calcular_media, verificar_situacao

def test_a(): # calcular_media de três notas iguais
    assert calcular_media(7,7,7) == 7
def test_b(): # calcular_media de notas diferentes
    assert calcular_media(6,7,8) == 7
def test_c(): # calcular_media com todas as notas iguais a zero
    assert calcular_media(0,0,0) == 0
def test_d(): # calcular_media com todas as notas iguais a dez
    assert calcular_media(10,10,10) == 10
def test_e(): # calcular_media com nota negativa
    with pytest.raises(ValueError, match="As notas devem estar entre 0 e 10"):
        calcular_media(-7,7,7)
def test_f(): # calcular_media com nota maior que dez
    with pytest.raises(ValueError, match="As notas devem estar entre 0 e 10"):
        calcular_media(11,10,10)

def test_g(): # verificar_situacao de média 7
    assert verificar_situacao(7) == "Aprovado"
def test_h(): # verificar_situacao de média maior que 7
    assert verificar_situacao(10) == "Aprovado"
def test_i(): # verificar_situacao de média 5
    assert verificar_situacao(5) == "Recuperação"
def test_j(): # verificar_situacao de média entre 5 e 7
    assert verificar_situacao(6) == "Recuperação"
def test_k(): # verificar_situacao de média menor que 5
    assert verificar_situacao(4) == "Reprovado"