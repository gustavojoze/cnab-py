from src.services.totais import calcular_totais

def test_totais_apenas_linhas_validas(tmp_path):
    arq = tmp_path / "cnab.txt"
    # dois detalhes, 10.00 e 5.50
    arq.write_text("112345678000199202501010000001000\n112345678000199202501010000000550\n")
    res = calcular_totais(str(arq))
    assert res["total_registros"] == 2
    assert res["total_valores"] == 15.5

def test_totais_com_valor_invalido(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("1XXXX20250101000000ABCD\n")
    res = calcular_totais(str(arq))
    assert isinstance(res["total_registros"], str)
    assert "Campo de valor possui caracteres inválidos" in res["total_registros"]
    assert res["total_valores"] == 0

def test_totais_ignora_linha_nao_detalhe(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("0HEADER\n9TRAILER\n")
    res = calcular_totais(str(arq))
    assert res["total_registros"] == 0
    assert res["total_valores"] == 0

def test_arquivo_vazio(tmp_path):
    cnab = tmp_path / "vazio.txt"
    cnab.touch()

    resultado = calcular_totais(str(cnab))
    assert resultado["total_registros"] == 0
    assert resultado["total_valores"] == 0

def test_apenas_linhas_invalidas(tmp_path):
    cnab = tmp_path / "invalidos.txt"
    cnab.write_text("0INVALIDO\nTRAILER\nABC\n")

    resultado = calcular_totais(str(cnab))
    assert resultado["total_registros"] == 0
    assert resultado["total_valores"] == 0

def test_multiplos_erros_valor(tmp_path):
    cnab = tmp_path / "erros.txt"
    cnab.write_text(
        "1" + "x" * 239 + "\n"
        "1" + "y" * 239 + "\n"
    )

    resultado = calcular_totais(str(cnab))
    assert "invalidos" in str(resultado["total_registros"]).lower()
