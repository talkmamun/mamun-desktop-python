
from collections import Counter
from pathlib import Path
import re


print("\n\n.....................................\n")

# Your text file path
file_path = Path(r"D:\mamun\test.txt")

print("File path:", file_path)

# Read the text file
file_text = file_path.read_text(encoding="utf-8")

print("\n\n..........\n")
print("\n\nStart of text:\n", type(file_text),"\n\n")

# Extract words and ignore capitalization

words = re.findall(r"\b[a-zA-Z0-9']+\b", file_text.lower())

print("\nWords", words)
#words= re.findall(r"\b", file_text.lower())

# Count total words
print( "type(words) : " , type(words) , "\nMemory address:", id(words), "\nTotal words:", len(words))

file_set = set(words)

print("\nUnique/Distinct words:", len(file_set), "\nMemory address:", id(file_set))

print("\n",file_set)

      