import logging
import time
from pathlib import Path

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


class FileHandler(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return

        raw_path = event.src_path

        if isinstance(raw_path, bytes):
            raw_path = raw_path.decode()

        file_path = Path(raw_path)
        logging.info("New file detected: %s", file_path.name)


def watch_directory(directory: str) -> None:
    folder = Path(directory).expanduser().resolve()

    if not folder.exists():
        raise FileNotFoundError(f"Directory not found: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    observer = Observer()
    observer.schedule(FileHandler(), str(folder), recursive=False)
    observer.start()

    logging.info("Watching directory: %s", folder)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Stopping watcher...")
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    watch_directory("test_folder")
