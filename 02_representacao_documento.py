import json

pedido = {
    "id_pedido": 1,
    "cliente": {"nome": "Ana", "telefone": "..."},
    "itens": [
        {"produto": "Marmita", "qtd": 2, "valor_unit": 25.0},
        {"produto": "Suco", "qtd": 1, "valor_unit": 8.0}
    ],
    "valor_total": 58.0
}

print(json.dumps(pedido, indent=2, ensure_ascii=False))
