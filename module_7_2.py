import io
from pprint import pprint

def custom_write(file_name, strings):
    f = open(file_name, "a", encoding='utf-8')
    string_positions = {}
    line_number = 1
    for line in strings:
        string_positions[(line_number, f.tell())] = line
        f.write(line + "\n")
        line_number+=1
    f.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
