my_list = list(map(int, input("Введите числа в списке через пробел: ").split()))
i = 0
while i < len(my_list):
    if my_list[i] < 0 :
        break
    if my_list[i] == 0:
        continue
    print(my_list[i])
    i+=1