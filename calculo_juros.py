# calculo_juros.py
from datetime import datetime

valor_original = float(input("Digite o valor original: R$ "))
data_venc = input("Digite a data de vencimento (dd/mm/aaaa): ")

data_venc = datetime.strptime(data_venc, "%d/%m/%Y")
data_hoje = datetime.now()

dias_atraso = (data_hoje - data_venc).days

print("\n===== CÁLCULO DE JUROS =====")

if dias_atraso > 0:
    multa = valor_original * 0.025 * dias_atraso
    valor_final = valor_original + multa
    print(f"Dias de atraso: {dias_atraso}")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
else:
    print("Pagamento dentro do prazo. Valor a pagar: R$ {:.2f}".format(valor_original))
