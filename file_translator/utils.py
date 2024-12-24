import os
import shutil
import uuid
from pathlib import Path

from file_translator.config import CACHE_DIR


def make_directory(filename):
    os.makedirs(CACHE_DIR, exist_ok=True)

    unique_id = str(uuid.uuid4())
    base_filename = Path(filename).stem
    dst_dir = os.path.join(CACHE_DIR, f"{base_filename}_{unique_id}")
    os.makedirs(dst_dir, exist_ok=True)
    return dst_dir


def remove_directory(dst_dir):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
