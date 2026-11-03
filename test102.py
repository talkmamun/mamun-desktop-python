

from collections import Counter
from pathlib import Path
import re



print("============================================")

# Your text file path
file_path = Path(r"G:\Python-Ostad-2026\file1.txt")

print("Reading file:", file_path)

# Read the text file
file_text = file_path.read_text(encoding="utf-8")

print("File_test Type: ", type(file_text))

# Extract words and ignore capitalization
words = re.findall(r"\b[a-zA-Z0-9']+\b", file_text.lower())
print("words Type: ", type(words))
print("words  ::" , words ,"\n" ) 


# Create a set containing unique words
thisset = set(words)
 
print("................................................\nthisset ::", thisset ) 

print("\nthisset(len) ::", len(thisset) ) 


#print("\nthisset(count) ::", count(thisset) ) 


print("................................................")

# Count total words
print("Total words:", len(words))

# Count unique words
word_counts = Counter(words)
print("Unique words:", len(word_counts))




# Display each word and its count
print("\nWord List:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}")



