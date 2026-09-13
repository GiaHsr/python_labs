print('a:', end = ' ')
a = float(input().replace(',', '.'))

print('b:', end = ' ')
b = float(input().replace(',', '.'))

print('sum=', "{:.2f}".format(a + b), end = '; ')
print('avg=', '{:.2f}'.format((a + b)/2))