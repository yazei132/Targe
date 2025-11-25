# controle_estoque.py

estoque = [
    {"codigo": 101, "descricao": "Caneta Azul", "estoque": 150},
    {"codigo": 102, "descricao": "Caderno Universitário", "estoque": 75},
    {"codigo": 103, "descricao": "Borracha Branca", "estoque": 200},
    {"codigo": 104, "descricao": "Lápis Preto HB", "estoque": 320},
    {"codigo": 105, "descricao": "Marcador de Texto Amarelo", "estoque": 90}
]

movimentos = []
id_movimento = 1

def movimentar_estoque(codigo_produto, qtde, descricao_mov):
    global id_movimento
    for prod in estoque:
        if prod["codigo"] == codigo_produto:
            prod["estoque"] += qtde

            movimento = {
                "id": id_movimento,
                "descricao": descricao_mov,
                "produto": prod["descricao"],
                "quantidade": qtde,
                "estoque_final": prod["estoque"]
            }
            movimentos.append(movimento)
            id_movimento += 1

            return movimento
    return "Produto não encontrado!"


# Exemplo de uso:
print(movimentar_estoque(101, 30, "Entrada de canetas"))
print(movimentar_estoque(102, -10, "Saída de cadernos"))
print(movimentar_estoque(105, -5, "Venda de marcadores"))
