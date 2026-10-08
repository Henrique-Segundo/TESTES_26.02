from temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius

def test_a(): # 0 °C = 32 °F
    assert celsius_para_fahrenheit(0) == 32
def test_b(): # 100 °C = 212 °F
    assert celsius_para_fahrenheit(100) == 212

def test_c(): # 32 °F = 0 °C
    assert fahrenheit_para_celsius(32) == 0
def test_d(): #  212 °F = 100 °C
    assert fahrenheit_para_celsius(212) == 100