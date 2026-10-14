import pytest
from cacaAsBruxas import potencial_teste, busca_binaria, obter_aprovacao, fib, bubble_sort, q6

#Testes do primeiro algoritimo potencial_teste

def test_q1a():
    assert potencial_teste(2,-1) == 0.5

def test_q1b():
    assert potencial_teste(2,3) == 8

def test_q1c():
    with pytest.raises(ValueError, match="A potência é um valor finito"):
        potencial_teste(0,0)

def test_q1d():
    assert potencial_teste(5,0) == 1

def test_q1e():
    with pytest.raises(ValueError, match="A potência é um valor finito"):
        potencial_teste(0,-1)

#Testes do segundo algoritimo busca_binaria

def test_q2a():
    assert busca_binaria([],5) == -1

def test_q2b():
    assert busca_binaria([4],4) == 0

def test_q2c():
    assert busca_binaria([4],9) == -1

def test_q2d():
    assert busca_binaria([4],2) == -1

#Testes do terceiro algoritimo obter_aprovação

def test_q3a():
    assert obter_aprovacao(None,4,50,50) == False

def test_q3b():
    assert obter_aprovacao(None,4,50,80) == True

def test_q3c():
    assert obter_aprovacao(None,4,80,None) == True

def test_q3d():
    assert obter_aprovacao(2,4,80,None) == True

#Testes do quarto algoritimo fib

def test_q4a():
    assert fib(0) == 0

def test_q4b():
    assert fib(2) == 1

def test_q4c():
    assert fib(3) == 2

def test_q4d():
    assert fib(4) == 3

#Testes do quinto algoritimo bubble_sort

def test_q5a():
    assert bubble_sort([1]) == [1] 

def test_q5b():
    assert bubble_sort([2,1]) == [1,2]

def test_q5c():
    assert bubble_sort([1,2]) == [1,2]

def test_q5d():
    assert bubble_sort([3,2,1]) == [1,2,3]

#Testes do sexto algoritimo q6

def test_q6a():
    assert q6(2,-2) == 0.25

def test_q6b():
    assert q6(2,2) == 4

def test_q6c():
    assert q6(2,0) == 1

def test_q6d():
    assert q6(2,-1) == 0.5