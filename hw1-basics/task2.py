"""
Задание 2. Парсинг лога.

В расшифрованном в задании 1 отчёте указано, для какого пользователя и с
какого времени искать подозрительную активность. Нужно найти в логе все
события этого пользователя, случившиеся строго позже указанного времени.
"""


def filter_events_after(log_lines: list[str], user: str, after_time: str) -> list[str]:
    """
    Вернуть строки лога log_lines, относящиеся к пользователю user, время
    которых строго позже after_time.

    Формат каждой строки лога: "<время> <пользователь> <событие>",
    например "19:05 alice export". Время - часы:минуты в 24-часовом
    формате; часы могут быть записаны без ведущего нуля (например, "9:05").

    Порядок строк в результате должен совпадать с их порядком во входных
    данных log_lines.

    Пример:
        filter_events_after(["10:00 alice login", "14:30 alice click"], "alice", "12:00")
        -> ["14:30 alice click"]
    """
    answer = []
    for line in log_lines:
        log_user = line.split(' ')[1]
        time= line.split(' ')[0]
        minute = int(time.split(':')[1])
        hour = int(time.split(':')[0])
        after_hour = int(after_time.split(":")[0])
        after_minute = int(after_time.split(":")[1])
        if user == log_user and ((hour > after_hour)  or (hour == after_hour and minute > after_minute)) :
            answer.append(line)

    return answer

    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("hw1-basics/data/task2_log.txt", encoding="utf-8") as f:
        log_lines = [line.strip() for line in f if line.strip()]

    result = filter_events_after(log_lines, "mktbot7", "19:00")
    print(result)
