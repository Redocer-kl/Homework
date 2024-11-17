import multiprocessing
import time
def read_info(name):
        all_data = []
        with open(name, "r", encoding="utf-8") as file:
            for line in file.readlines():
                all_data.append(line)
        print(f"файл {name} прочитан")

filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == "__main__":
    # start_time = time.time()
    # for name in filenames:
    #     read_info(name)
    # print("Время выполнения линейно", time.time() - start_time)
    start_time = time.time()
    proceses = []
    for name in filenames:
        proceses.append(multiprocessing.Process(target=read_info, args=(name,)))
    for process in proceses:
        process.start()
    print("Время выполнения в мультипотоке", time.time() - start_time)