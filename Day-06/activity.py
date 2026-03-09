from pathlib import Path

file_path = Path(__file__).parent/"sample.txt"


data = True
line = 1
word = "python"

with open(file_path , "r") as f:
     while data:
          data = f.readline()

          if(word in data):
               print(f"{word} found at line {line}")
               break
          line += 1
