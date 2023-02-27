a, b = sorted(map(int, input().split()))
n1, n2 = b, a
while n1 % n2 > 0:
    n1, n2 = n2, n1 % n2
print('1' * n2)
