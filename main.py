import collections
import re

pattern = r"^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(INFO|ERROR|WARNING)\s+(.*)$"


def analyzer(file_path):
    data = collections.defaultdict(list)

    with open(file_path) as file:
        for line in file:
            print(line)
            line = line.strip()
            print(line)
            match = re.match(pattern, line)

            if not match is None:
                _, _, request_type, description = match.groups()
                data[request_type].append(description)

    for log_type, messages in data.items():
        print(f"{log_type}: ")
        for message in messages:
            print(f"  - {message}")


if __name__ == "__main__":
    analyzer("./server.log")
