#tải và giải nén dataset

import os
from pathlib import Path

DATA_DIR = "data"
URL = "https://www.openslr.org/resources/12/dev-clean.tar.gz"

def download_and_extract():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.chdir(DATA_DIR)

    if not os.path.exists("dev-clean.tar.gz"):
        os.system(f"wget {URL}")

    if not os.path.exists("LibriSpeech"):
        os.system("tar -xvf dev-clean.tar.gz")

def keep_subset(limit=1000):
    base_path = Path("LibriSpeech/dev-clean")
    all_files = list(base_path.rglob("*.flac"))

    for f in all_files[limit:]:
        os.remove(f)

    print(f"Kept {limit} files")

if __name__ == "__main__":
    download_and_extract()
    keep_subset()