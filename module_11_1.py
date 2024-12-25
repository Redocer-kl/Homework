import requests
import pandas as pd
import numpy as np


#работа с requests
url = 'https://google.com'
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f'Ошибка: {response.status_code}')

#работа с pandas
data = pd.read_csv('data.csv')

mean_value = data['числа'].mean()
print(f'Среднее значение: {mean_value}')


#работа с numpy
array = np.array([1, 2, 3, 4, 5])

squared = array ** 2
summed = np.sum(array)

print(f'Квадраты элементов: {squared}')
print(f'Сумма элементов: {summed}')
