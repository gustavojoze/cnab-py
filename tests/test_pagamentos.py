from src.services.pagamentos import validar_pagamento

def test_pagamento_cnpj_invalido():
    res = validar_pagamento("123", 5000)
    assert res["status"] == "rejeitado"

def test_pagamento_aprovado_limite_inferior():
    res = validar_pagamento("12345678000199", 10)
    assert res["status"] == "aprovado"

def test_pagamento_pendente_faixa_media():
    res = validar_pagamento("12345678000199", 20000)
    assert res["status"] == "pendente_validacao"

def test_pagamento_rejeitado_valor_acima():
    res = validar_pagamento("12345678000199", 60000)
    assert res["status"] == "rejeitado"
