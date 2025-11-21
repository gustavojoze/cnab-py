from src.utils.validacoes import linha_valida

def test_linha_valida_ok():
    assert linha_valida("1234567890") is True

def test_linha_vazia():
    assert linha_valida("") is False

def test_linha_so_espaco():
    assert linha_valida("   ") is False

def test_linha_menor_que_minimo():
    assert linha_valida("123456789") is False

def test_linha_exatamente_minimo():
    assert linha_valida("1234567890") is True
    
def test_linha_com_espacos_no_fim():
    linha = "1" * 100 + "   "
    assert linha_valida(linha) is True

def test_linha_exatamente_400_chars():
    linha = "1" * 400
    assert linha_valida(linha) is True

def test_linha_com_caracteres_especiais():
    linha = "@@@@"
    assert linha_valida(linha) is False

