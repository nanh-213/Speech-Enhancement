#tạo list theo đúng định dạng yêu cầu trong wave u net

import os
import glob

CLEAN_ROOT = "data/LibriSpeech"

def create_list(noisy_dir, output_file):
    clean_files = glob.glob(os.path.join(CLEAN_ROOT, "**/*.flac"), recursive=True)
    clean_map = {os.path.splitext(os.path.basename(f))[0]: f for f in clean_files}

    noisy_files = [f for f in os.listdir(noisy_dir) if f.endswith(".opus")]

    pairs = []
    for f in noisy_files:
        name = os.path.splitext(f)[0]
        if name in clean_map:
            noisy_path = os.path.join(noisy_dir, f)
            clean_path = clean_map[name]
            pairs.append(f"{noisy_path} {clean_path}")

    with open(output_file, "w") as f:
        f.write("\n".join(pairs))

    print(f"{output_file}: {len(pairs)} pairs")

if __name__ == "__main__":
    create_list("data/compressed_8k", "data/train_list_8k.txt")
    create_list("data/compressed_16k", "data/train_list_16k.txt")