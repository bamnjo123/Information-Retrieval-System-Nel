import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "pyproject.toml",
    
]


for filepath in list_of_files:
    path = Path(filepath)

    # create parent directory if needed
    parent = path.parent
    if parent and parent != Path('.'):
        parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created/verified directory: {parent}")

    # create empty file if missing
    if not path.exists() or path.stat().st_size == 0:
        path.touch(exist_ok=True)
        logging.info(f"Created empty file: {path}")
    else:
        logging.info(f"{path.name} already exists")