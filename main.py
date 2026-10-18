import logging
from pathlib import Path

from scanner import scan_directory
from watcher import watch_directory


def main():
    print("===Automated Fiel Organizer===")
    source_input = input("Enter the directory to watch: ").strip()

    if not source_input:
        print("Error: Directory path cannot be empty.")
        return

    directory = Path().home() / source_input
    directory = directory.resolve()

    if not directory.exists():
        print(f"Error: Directory does not exist: {directory}")
        return

    if not directory.is_dir():
        print(f"Error: Path is not a directory: {directory}")
        return

    try:
        scan_directory(str(directory))
        watch_directory(str(directory))
    except OSError:
        logging.exception("Failed to start the file watcher.")
        print("Could not start watching this directory.")


if __name__ == "__main__":
    main()
