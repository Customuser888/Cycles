a = int(input())
c = 0
while a > 0:
  b = a%10
  a //= 10
  c += b
print(c)
