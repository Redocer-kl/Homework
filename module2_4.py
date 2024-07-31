numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    f = True
    d = 2
    while d * d <= i:
        if i % d == 0:
            not_primes.append(i)
            f = False
            break
        d+= 1
    if f:
        primes.append(i)

print("Простые числа: ", *primes)
print("Сложносоставные числа: ", *not_primes)