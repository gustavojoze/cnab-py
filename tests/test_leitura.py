from src.infrastructure.leitura import contarTiposLinhas
import pytest
def test_leitura_contagem_basica(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("0HEADER\n1DETALHE\n9TRAILER\n")
    res = contarTiposLinhas(str(arq))
    assert res == {'header': 1, 'detalhes': 1, 'trailer': 1}

def test_leitura_ignora_linhas_invalidas(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("xxx\n\n0H\n1D\n9T\n")
    res = contarTiposLinhas(str(arq))
    assert res == {'header': 1, 'detalhes': 1, 'trailer': 1}

def test_leitura_arquivo_nao_encontrado():
    res = contarTiposLinhas("arquivo_que_nao_existe.txt")
    assert "erro" in res
    assert res["erro"].startswith("Arquivo não encontrado")

def test_leitura_com_linhas_muito_curtas(tmp_path):
    arq = tmp_path / "cnab.txt"
    arq.write_text("0\n1\n9\n")
    res = contarTiposLinhas(str(arq))
    assert res == {'header': 0, 'detalhes': 0, 'trailer': 0}

def test_arquivo_sem_header(tmp_path):
    cnab = tmp_path / "sem_header.txt"
    cnab.write_text("1" + "x" * 239 + "\n9" + "x" * 239)

    resultado = contarTiposLinhas(str(cnab))
    assert resultado["header"] == 0
    assert resultado["detalhes"] == 1
    assert resultado["trailer"] == 1

def test_arquivo_sem_trailer(tmp_path):
    cnab = tmp_path / "sem_trailer.txt"
    cnab.write_text("0" + "x" * 239 + "\n1" + "x" * 239)

    resultado = contarTiposLinhas(str(cnab))
    assert resultado["trailer"] == 0

def test_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        contarTiposLinhas("arquivo_inexistente.txt")
