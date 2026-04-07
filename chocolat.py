def ChocoSplit(n, m):
    c = (n * m) - 1
    if n == 0 or m == 0:
        return 0
    else:
        return c

cho = ChocoSplit(9, 3)
print(cho)
