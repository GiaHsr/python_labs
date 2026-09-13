price, discount, vat = map(int, input().split())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print('База после скидки:', '{:.2f}'.format(base), '₽')
print('НДС:              ', '{:.2f}'.format(vat_amount), '₽')
print('Итого к оплате:   ', '{:.2f}'.format(total), '₽')
