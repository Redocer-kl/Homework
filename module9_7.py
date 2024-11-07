
def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        d = 2
        f = False
        while d * d < result:
            if result % d == 0:
                f = True
                break
            d+= 1
        if f:
            print("Составное")
        else:
            print("Простое")
        return result
    return  wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)