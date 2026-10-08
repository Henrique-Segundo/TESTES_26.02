from validacao import senha_valida

def test_a_oito_caracteres():
    assert senha_valida("ABCDEFGH") == True

def test_b_mais_caracteres():
    assert senha_valida("ABCDEFGHIJK") == True

def test_c_menos_caracteres():
    assert senha_valida("ABC") == False

def test_d_senha_vazia():
    assert senha_valida("") == False