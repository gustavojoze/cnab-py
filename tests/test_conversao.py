from src.services.conversao import conversao_simples

def test_conversao_valida(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("112345678000199202501010000001000\n")
    res = conversao_simples(str(arq))
    assert len(res) == 1
    linha = res[0]
    assert linha["cnpj"] == "12.345.678/0001-99"
    assert linha["data"] == "01/01/2025"
    assert linha["valor"] == 10.0

def test_conversao_cnpj_invalido(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("1ABCDEFGHIJKLM202501010000001000\n")
    res = conversao_simples(str(arq))
    assert "CNPJ contém caracteres inválidos" in res[0]["cnpj"]

def test_conversao_data_invalida(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("112345678000199202513550000001000\n")
    res = conversao_simples(str(arq))
    assert "Data inválida" in res[0]["data"]

def test_conversao_valor_invalido(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("11234567800019920250101ABCDEF1234\n")
    res = conversao_simples(str(arq))
    assert "Valor contém caracteres inválidos" in res[0]["valor"]

def test_conversao_ignora_linha_nao_detalhe(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("0HEADER\n9TRAILER\n")
    res = conversao_simples(str(arq))
    assert res == []

def test_conversao_arquivo_inexistente(capfd):
    res = conversao_simples("nao_existe.txt")
    assert res == []
    capturado = capfd.readouterr().out
    assert "Arquivo não encontrado." in capturado
