from pathlib import Path

# Same folder mein hai sample.txt
file_path = Path(__file__).parent / "sample.txt"


f = open(file_path,"w") #file Object
data = f.write("Text to overwrite \n the complete data.")
print(data)

f.close()