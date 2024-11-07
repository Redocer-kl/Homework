import threading
import time

def write_words(word_count, file_name):
    with open(file_name, "w") as file:
        for i in range(1, word_count  + 1):
            file.write(f"Какое-то слово №{i}")
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

start = time.time()
files_args = [
    (10, 'example1.txt'),
    (30, 'example2.txt'),
    (200, 'example3.txt'),
    (100, 'example4.txt')
]

for args in files_args:
    write_words(*args)
print(time.time() - start)

start = time.time()

threads = []

for args in files_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(time.time() - start)