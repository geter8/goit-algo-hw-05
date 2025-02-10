import sys
import os
import re
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    """Розбирає рядок логу на компоненти: дата, час, рівень, повідомлення."""
    match = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (INFO|ERROR|DEBUG|WARNING) (.+)", line)
    if match:
        return {"date": match.group(1), "time": match.group(2), "level": match.group(3), "message": match.group(4)}
    return None


def load_logs(file_path: str) -> list:
    """Завантажує логи з файлу та парсить їх."""
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed_log = parse_log_line(line.strip())
                if parsed_log:
                    logs.append(parsed_log)
    except FileNotFoundError:
        print(f"Помилка: Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за рівнем логування."""
    return [log for log in logs if log["level"].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів для кожного рівня логування."""
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts


def display_log_counts(counts: dict):
    """Виводить підрахунок логів у вигляді таблиці."""
    print("Рівень логування | Кількість")
    print("-" * 25)
    for level, count in sorted(counts.items()):
        print(f"{level:<15} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень_логування]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()