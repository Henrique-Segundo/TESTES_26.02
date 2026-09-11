from regra import classificar_idade

def test_a(): #idade 5
    assert classificar_idade(5) == "criança"
def test_b(): #idade 12
    assert classificar_idade(12) == "adolescente"
def test_c(): #idade 17
    assert classificar_idade(17) == "adolescente"
def test_d(): #idade 18
    assert classificar_idade(18) == "adulto"
def test_e(): #idade 30
    assert classificar_idade(30) == "adulto"