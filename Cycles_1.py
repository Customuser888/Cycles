n = int(input('Введите n: '))
for i in range(1, n + 1):
    s = i * i
    if s <= n:
        print(s, end=' ')