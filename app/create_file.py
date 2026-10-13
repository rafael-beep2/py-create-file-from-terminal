import datetime
import os
import sys
from typing import List


def create_directories(directories: List[str]) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_content_lines() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: List[str]) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else len(args)
        directories = args[d_index + 1:f_index]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    path = ""
    if directories:
        path = create_directories(directories)

    if file_name:
        full_path = os.path.join(path, file_name) if path else file_name
        lines = get_content_lines()
        write_to_file(full_path, lines)


if __name__ == "__main__":
    main()
