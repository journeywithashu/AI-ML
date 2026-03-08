from pathlib import Path

# Same folder mein hai sample.txt
file_path = Path(__file__).parent / "sample.txt"


f = open(file_path,"r") #file Object
data = f.read()
print(data)

f.close()