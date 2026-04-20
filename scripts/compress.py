#nén opus 8k & 16k

from pydub import AudioSegment
import os
import glob

INPUT_DIR = "data/LibriSpeech/dev-clean"

def compress(output_folder, bitrate):
    os.makedirs(output_folder, exist_ok=True)

    files = glob.glob(os.path.join(INPUT_DIR, "**/*.flac"), recursive=True)

    print(f"Compressing {len(files)} files to {bitrate}...")

    for file_path in files:
        try:
            name = os.path.basename(file_path).replace(".flac", "")

            audio = AudioSegment.from_file(file_path)
            audio = audio.set_frame_rate(16000).set_channels(1)

            audio.export(
                os.path.join(output_folder, f"{name}.opus"),
                format="opus",
                bitrate=bitrate
            )
        except Exception as e:
            print(f"Error: {file_path} - {e}")

if __name__ == "__main__":
    compress("data/compressed_8k", "8k")
    compress("data/compressed_16k", "16k")