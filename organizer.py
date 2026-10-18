import logging
import shutil
from pathlib import Path


def check_existing_file(target_file: Path) -> bool:
    return target_file.exists()


def move_file(source_file: Path, target_file: Path) -> bool:
    try:
        shutil.move(str(source_file), str(target_file))
        logging.info("File moved successfully: %s", target_file)
        return True
    except OSError:
        logging.exception("Failed to move file: %s", source_file)
        return False


def file_organizer(file: str, category: str) -> bool:
    source_file = Path(file)
    target_dir = source_file.parent / category

    if not source_file.is_file():
        logging.warning("Source file does not exist: %s", source_file)
        return False

    target_dir.mkdir(parents=True, exist_ok=True)

    target_file = target_dir / source_file.name

    if check_existing_file(target_file):
        name_without_extension = target_file.stem
        extension = target_file.suffix
        counter = 1

        while check_existing_file(target_file):
            new_file_name = f"{name_without_extension}_{counter}{extension}"
            target_file = target_dir / new_file_name
            counter += 1

    return move_file(source_file, target_file)
