def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f"Некорректный тип данных для подсчета суммы - {number}")
            incorrect_data +=1
    return  (result, incorrect_data)

def calculate_average(numbers):
    try:
        if not(type(numbers) is list or type(numbers) is tuple or type(numbers) is str):
            raise TypeError
        summ = personal_sum(numbers)
        return summ[0] / (len(numbers) - summ[1])
    except ZeroDivisionError:
        return 0
    except TypeError as exc:
        print("В numbers записан некорректный тип данных")
        return None


personal_sum([1, 3141, 241])

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
