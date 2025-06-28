from pathlib import Path
from collections import Counter

def parse_log_line(line: str) -> dict:
    date_error, time_error, what_error, *info = line.split()
    info_error = " ".join(info)
    return {
        "date": date_error,
        "time": time_error,
        "what_error": what_error,
        "info_error": info_error
     } #результат в словник

def load_logs(path_log) -> list: # Зчитування файлу
    if not path_log.exists():
        print(f"Файлу '{path_log}' не існує.")
        return []
    dict_log = []
    with open(path_log, 'r', encoding='utf-8') as fh:
        while True:
            try: 
                line = fh.readline()
                if not line:
                    break
                dict_log.append(parse_log_line(line))
            except ValueError:
                print(f"Увага !!!! Помилка обробки файлу. В файлі наявний рядок з помилковими даними - {line}")
        #print (dict_log)
        return (dict_log) #результат в список
    fh.close()

def filter_logs_by_level(logs: list, level: str) -> list: #Функція відбіру списку по помилці
    dict_log_list=[]
    info_logs = [log for log in logs if log['what_error'] == level] #відбір списку по помилці
    dict_log_list.append(info_logs)
    return (dict_log_list) 


def count_logs_by_level(logs: list) -> dict: # рахуємо кількість помилок
    dict_log_num = {}
    dict_log_num = dict(Counter(log['what_error'] for log in logs))
    return dict_log_num

def display_log_counts(counts: dict): #Функція іиіоду таблиці
    print(f"{'Рівень логування':^20} | {'Кількість':^15}")
    print(f"{'-'*20:^20} | {'-'*15:^15}")
    for level, count in counts.items():
        print(f"{level:^20} | {count:^15}")

def main():
    path_input = input("Введіть шлях до файлу (та додаткові параметри якщо необхідно): ")

    log_path_str, *args = path_input.split(' ') # Перевірка наявності додаткового параметру
    if args:
        level_str = args[0] 
    else:
        level_str = None

    # print (log_path_str, *args)
    # Конвертуємо введений текст у об'єкт типу Path
    log_path = Path(log_path_str)
    all_dict_error=load_logs(log_path) # Зчитування файлу та створення словника

    # print(all_dict_error)
    #print(count_logs_by_level(all_dict_error))

    display_log_counts(count_logs_by_level(all_dict_error)) # Створення таблиці по результату розрахунку

    if level_str != None: #Вивід списку по додатковому параметру
        dict_log = filter_logs_by_level (all_dict_error, level_str)
        print()
        print(f'Деталі логів для рівня {level_str}:')
        for log in dict_log[0]:
            print(f"{log['date']} {log['time']} — {log['info_error']}")

if __name__ == "__main__":
    main()



