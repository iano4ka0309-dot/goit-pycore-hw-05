from pathlib import Path
import sys
import time 
def parse_log_line(line: str):
    paths = line.split(None,3)
    return {
        "data": paths[0],
        "time": paths[1],
        "level": paths[2],
        "message": paths[3]}

def load_logs(file_path:    str):
    with open(file_path, 'r') as file:
        logs = []
        for line in file:
            logs.append(parse_log_line(line))
    return logs


def count_logs_by_level(logs: list):
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts

def filter_logs_by_level(logs: list, level: str):
    return [log for log in logs if log["level"] == level]

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<17} | {'Кількість'}")
    print(f"{'-'*17}-|----------")
    for level, count in counts.items():
        print(f"{level:<17} | {count}")


def main():
    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

if __name__ == "__main__":
    main()