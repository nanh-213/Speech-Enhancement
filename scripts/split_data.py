#chia thành train set và validation set

def split(input_file, train_out, val_out, ratio=0.9):
    with open(input_file, "r") as f:
        lines = f.readlines()

    split_idx = int(len(lines) * ratio)

    with open(train_out, "w") as f:
        f.writelines(lines[:split_idx])

    with open(val_out, "w") as f:
        f.writelines(lines[split_idx:])

    print(f"{input_file} → Train: {split_idx}, Val: {len(lines)-split_idx}")

if __name__ == "__main__":
    # 8k
    split(
        "data/train_list_8k.txt",
        "data/train_8k.txt",
        "data/val_8k.txt"
    )

    # 16k
    split(
        "data/train_list_16k.txt",
        "data/train_16k.txt",
        "data/val_16k.txt"
    )

