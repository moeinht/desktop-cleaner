import logging
import time
from pathlib import Path


def wait_until_ready(
    file_path: str,
    check_interval: int = 2,
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
