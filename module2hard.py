n = int(input("Введите n: "))
s = ""
for i in range(1, n):
    for j in range(i+1, n - i + 1):
        if n % (i + j) == 0:
            s += str(i) + str(j)
print(s)
