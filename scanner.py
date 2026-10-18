import logging
import time
from pathlib import Path

from organizer import file_organizer
from rules import get_file_category


def wait_until_ready(
    file_path: str,
    check_interval: float = 2,
    stable_checks: int = 3,
    timeout: int = 60,
) -> bool:
    path = Path(file_path)
    deadline = time.monotonic() + timeout

    previous_size = None
    consecutive_stable_checks = 0

    while time.monotonic() < deadline:
        try:
            current_size = path.stat().st_size
        except (FileNotFoundError, PermissionError, OSError):
            logging.warning("Cannot access file: %s", path)
            return False

        if current_size == previous_size:
            consecutive_stable_checks += 1
        else:
            consecutive_stable_checks = 0

        if consecutive_stable_checks >= stable_checks:
            logging.info("File appears ready: %s", path.name)
            return True

        previous_size = current_size
        time.sleep(check_interval)

    logging.warning("Timed out waiting for file: %s", path.name)
    return False


def scan_directory(directory: str) -> None:
    folder = Path(directory).expanduser().resolve()

    logging.info("Starting initial scan: %s", folder)

    for file_path in list(folder.iterdir()):
        if not file_path.is_file():
            continue

        logging.info("Checking existing file: %s", file_path.name)

        if not wait_until_ready(str(file_path), check_interval=0):
            logging.warning("Skipping file that is not ready: %s", file_path.name)
            continue

        category = get_file_category(file_path)

        if category is None:
            logging.info("Unknown file type, skipping: %s", file_path.name)
            continue

        moved = file_organizer(str(file_path), category)

        if moved:
            logging.info("File organized successfully: %s", file_path.name)
        else:
            logging.warning("Could not organize file: %s", file_path.name)

    logging.info("Initial scan completed.")
