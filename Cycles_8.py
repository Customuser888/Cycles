a = int(input())
c = 0
d = 1
while a > 0:
  b = a%10
  a //= 10
  c += b
  d *= b
print(c)
print(d)
