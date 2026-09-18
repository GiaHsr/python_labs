m = int(input('Минуты: '))

h = m//60
m -= h * 60

print(f'{h}:{m:02d}')