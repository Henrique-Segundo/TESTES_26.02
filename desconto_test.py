import pytest
from desconto import calcular_desconto

def test_a(): #Qual deve ser o resultado para uma compra de R$ 100 com desconto de 10%?
    assert calcular_desconto(100,10) == 90 #10 de desconto

def test_b(): #E com desconto de 0%?
    assert calcular_desconto(100,0) == 100 #0 de desconto

def test_c(): #E com desconto de 100%?
    assert calcular_desconto(100,100) == 0 #100 de desconto, produto grátis

def test_d(): #O que deve acontecer com valor negativo?
    with pytest.raises(ValueError, match="O valor não pode ser negativo"):
        calcular_desconto(-100,10) #Erro, não aceita valor negativo pois não possui sentido logico

def test_e(): #O que deve acontecer com percentual maior que 100?
    with pytest.raises(ValueError, match="Percentual inválido"):
        calcular_desconto(100,110) #Erro, geraria o vendedor a pagar o cliente não possui sentido logico