def calcular_cashback(valor_compra, desconto, vip):
    valor_final = valor_compra - desconto
    
    if valor_final <= 0:
        return 0, valor_final, 0, 0, vip
    cashback = valor_final * 0.05
    
    if valor_final > 500:
        cashback *= 2
    bonus_vip = cashback * 0.10 if vip else 0
   
    cashback_total = cashback + bonus_vip
   
    return cashback_total, valor_final, cashback, bonus_vip, vip


print("\n--- Calculo de Cashback ---\n")

try:
    valor_compra = float(input("Valor da compra: "))
except ValueError:
    print("Por favor, digite um número válido.")
    exit()

try:
    desconto_porcentagem = float(input("Desconto aplicado(%): "))
    desconto = valor_compra * (desconto_porcentagem / 100)
except ValueError:
    print("Por favor, digite um número válido.")
    exit()

vip = input("Cliente VIP? (s/n): ").strip().lower() == "s"

cashback_total, valor_final, cashback, bonus_vip, vip = calcular_cashback(valor_compra, desconto, vip)

print(f"\n{'=================================='}")
print(f"RESUMO DA COMPRA")
print(f"{'=================================='}")
print(f"Valor da compra:   R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto_porcentagem:.1f}% (R$ {desconto:.2f})")
print(f"Valor final:       R$ {valor_final:.2f}\n")
print(f"Cashback (5%):     R$ {cashback:.2f}", end="")
if valor_final > 500:
    print(" (dobrado pela promoção!)")
else:
    print()
if vip:
    print(f"Bônus VIP (10%):   R$ {bonus_vip:.2f}")
print(f"{'=================================='}")
print(f"CASHBACK TOTAL:     R$ {cashback_total:.2f}")
