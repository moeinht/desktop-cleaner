import logging
from pathlib import Path

from watcher import watch_directory


def main():
    print("===Automated Fiel Organizer===")
    source_input = input("Enter the directory to watch: ").strip()

    if not source_input:
        print("Error: Directory path cannot be empty.")
        return

    path = Path().home() / source_input
    path = path.resolve()

    if not path.exists():
        print(f"Error: Directory does not exist: {path}")
        return

    if not path.is_dir():
        print(f"Error: Path is not a directory: {path}")
        return

    try:
        watch_directory(str(path))
    except OSError:
        logging.exception("Failed to start the file watcher.")
        print("Could not start watching this directory.")


if __name__ == "__main__":
    main()
