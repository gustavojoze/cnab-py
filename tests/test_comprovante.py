import os
from unittest.mock import patch
from src.infrastructure.comprovantes import gerar_comprovante
from src.services.pagamentos import validar_pagamento


def test_gera_comprovante_valido(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    res = gerar_comprovante("12345678000199", 150.75)
    assert "mensagem" in res
    assert res["status"] == "aprovado"
    assert os.path.exists(res["arquivo"])

def test_gera_comprovante_cnpj_invalido(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    res = gerar_comprovante("123", 150.75)
    assert res["status"] == "rejeitado"
    assert os.path.exists(res["arquivo"])



def test_comprovante_caminho_seguro():
    # CNPJ formatado com caracteres especiais
    resultado = gerar_comprovante("12345678000199", 100)

    assert "12345678000199" in os.path.basename(resultado["arquivo"])

def test_comprovante_com_cnpj_invalido():
    resultado = gerar_comprovante("000", 100)
    assert resultado["status"] == "rejeitado"

@patch("infrastructure.comprovantes.os.makedirs")
def test_comprovante_permissionerror(mock_makedirs):
    mock_makedirs.side_effect = PermissionError

    resultado = gerar_comprovante("12345678000199", 100)
    assert "temp" in resultado["arquivo"].lower() or "tmp" in resultado["arquivo"].lower()
