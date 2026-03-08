import os
from pathlib import Path

file_path = Path(__file__).parent / "sample.txt"

os.remove(file_path)
print("File delete ho gayi!")