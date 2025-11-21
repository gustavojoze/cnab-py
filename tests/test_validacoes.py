from src.utils.validacoes import linha_valida, validar_cnpj, validar_data, validar_valor


def test_linha_valida_ok():
    linha = "1".ljust(240, "0")
    assert linha_valida(linha) is True


def test_linha_valida_vazia():
    assert linha_valida("") is False


def test_linha_valida_curta():
    assert linha_valida("1") is False


def test_linha_valida_maior_400():
    linha = "1".ljust(401, "0")
    assert linha_valida(linha) is False


def test_validar_cnpj_ok():
    assert validar_cnpj("12345678000199", 1) is None


def test_validar_cnpj_invalido():
    assert "inválido" in validar_cnpj("1234ABC0000123", 2)


def test_validar_data_ok():
    assert validar_data("20250101", 1) == "01/01/2025"


def test_validar_data_invalida():
    assert "inválida" in validar_data("20251350", 2)


def test_validar_valor_ok():
    assert validar_valor("0000012500", 1) == 125.00


def test_validar_valor_invalido():
    assert "inválido" in validar_valor("ABCDE12345", 1)
