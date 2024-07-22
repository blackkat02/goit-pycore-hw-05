from collections import defaultdict
from datetime import datetime


def parse_log_line(line: str) -> dict:
    """
    Parses a single log line into a dictionary with keys 'Date', 'Time', 'Log', and 'Message'.
    Args:
        line (str): The log line to parse.
    Returns:
        dict: A dictionary containing parsed data from the log line.
              A dictionary {"Date": "None", "Time": "None", "Log": "None", "Message": "None"} if the line format
              is invalid.
    """
    try:
        date, time, log_level, message = line.split(maxsplit=3)
        datetime.strptime(date, '%Y-%m-%d')
        datetime.strptime(time, '%H:%M:%S')
    except ValueError:
        print(f"Error: The line format doesn't match the expected pattern: {line}")
        return {"Date": "None", "Time": "None", "Log": "None", "Message": "None"}
    except Exception as e:
        print(f"Error: {e}")
        return None

    log_dict = {"Date": date, "Time": time, "Log": log_level, "Message": message}
    return log_dict


def load_logs(file_path: str) -> list[dict]:
    """
   Loads log entries from a given file path and parses them into a list of dictionaries.
   Args:
       file_path (str): The path to the log file.
   Returns:
       list[dict]: A list of dictionaries, each containing parsed data from a log line.
                   None if errors occur during file access or parsing.
    """
    list_dict = []
    try:
        with open(file_path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
            for line in lines:
                parse_log_line(line)
                list_dict.append(parse_log_line(line))
            return list_dict
    except NameError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters a list of log entries based on a specific log level.
    Args:
        logs (list): A list of dictionaries containing parsed log data.
        level (str): The log level to filter by.
    Returns:
        list: A new list containing only entries with the specified log level.
    """
    filter_list = [x for x in logs if x["Log"] == level]
    """ 
    Приклад використання альтернативного способу за допомогою lambda - функції
    filter_list = filter(lambda x: x["Log"] == level, logs) 
    return list(filter_list)
    """
    return filter_list


def count_logs_by_level(logs: list) -> dict:
    """
    Counts the occurrences of each log level in a list of log entries.

    Args:
        logs (list): A list of dictionaries containing parsed log data.

    Returns:
        dict: A dictionary where keys are log levels and values are their corresponding counts.
              An empty defaultdict if errors occur during counting.
    """
    counts_log_default_dict = defaultdict(list)
    try:
        for log in logs:
            level = log['Log']
            count_level = len(filter_logs_by_level(path, level))

            if not counts_log_default_dict[level]:
                counts_log_default_dict[level].append(count_level)
    except TypeError:
        print('Файл не існує')

    return counts_log_default_dict


def display_log_counts(counts: dict):
    """
    Formats and prints the log level counts to the console.
    Args:
        counts (dict): A dictionary containing log level counts.
    """
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print("-" * 32)

    for level, count in counts.items():
        print(f"{level:<17} | {count[0]:<8}")

    print(' ')
    if "None" in counts:
        print("None - не_валідний запис з файлу log_file.log")
    return


path = load_logs(r"C:\Users\Admin\PycharmProjects\goit-pycore-hw-05\log_file.log")
display_log_counts(count_logs_by_level(path))

#print(path)

# filter_logs = filter_logs_by_level(path, level)
# print(filter_logs)

# count_logs = count_logs_by_level(path)
# print(count_logs)
