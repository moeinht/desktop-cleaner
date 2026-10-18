from pathlib import Path

FILE_CATEGORIES = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",
    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".doc": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mkv": "Videos",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".m4a": "Audio",
    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
}


def get_file_category(file):
    file = Path(file)
    suffix = file.suffix

    category = FILE_CATEGORIES.get(suffix.lower())

    if category == None:
        return None

    return category
