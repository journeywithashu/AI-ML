from pathlib import Path

# Same folder mein hai sample.txt
file_path = Path(__file__).parent / "sample.txt"


with open(file_path,"r") as f:
 data = f.read()
 print(len(data))
