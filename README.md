# 🧮 Exercícios de lógica em Python

Três scripts curtos que resolvem problemas comuns do dia a dia de uma empresa: comissão de vendas, juros por atraso e movimentação de estoque.

Não precisam de nenhuma biblioteca externa, só do Python 3.

## Scripts

### `calculo_comissao.py`: comissão de vendas

Soma a comissão de cada vendedor a partir de uma lista de vendas, com estas faixas:

| Valor da venda | Comissão |
| --- | --- |
| Abaixo de R$ 100,00 | 0% |
| De R$ 100,00 até R$ 499,99 | 1% |
| A partir de R$ 500,00 | 5% |

```bash
python calculo_comissao.py
```

```text
===== COMISSÕES CALCULADAS =====
João Silva: R$ 495.68
Maria Souza: R$ 465.95
Carlos Oliveira: R$ 379.37
Ana Lima: R$ 404.98
```

### `calculo_juros.py`: juros por atraso

Pede o valor original e a data de vencimento (`dd/mm/aaaa`), conta os dias de atraso até hoje e aplica um acréscimo de 2,5% do valor original por dia de atraso.

```bash
python calculo_juros.py
```

Exemplo: R$ 1.000,00 com 4 dias de atraso fica R$ 1.100,00. Se o pagamento está dentro do prazo, o valor não muda.

### `controle_estoque.py`: movimentação de estoque

Registra entradas (quantidade positiva) e saídas (quantidade negativa) de produtos. Cada movimentação recebe um número, a descrição e o estoque final do produto. Se o código não existir, avisa que o produto não foi encontrado.

```bash
python controle_estoque.py
```

```text
{'id': 1, 'descricao': 'Entrada de canetas', 'produto': 'Caneta Azul', 'quantidade': 30, 'estoque_final': 180}
{'id': 2, 'descricao': 'Saída de cadernos', 'produto': 'Caderno Universitário', 'quantidade': -10, 'estoque_final': 65}
{'id': 3, 'descricao': 'Venda de marcadores', 'produto': 'Marcador de Texto Amarelo', 'quantidade': -5, 'estoque_final': 85}
```
