
from collections import Counter
from pathlib import Path
import re


print("\n\n==================================================\n")

# Your text file path
file_path = Path(r"D:\mamun\test.txt")

print("File path:", file_path)

# Read the text file
file_text = file_path.read_text(encoding="utf-8")

print("\n\n..........\n")
print("\n\n Start of text:\n", type(file_text),"\n\n")

# Extract words and ignore capitalization

words_list = re.findall(r"\b[a-zA-Z0-9']+\b", file_text.lower())

print("\n\n................\n")
words_list.sort()
print("\n\nwords_list : ", words_list)


#words= re.findall(r"\b", file_text.lower())

# Count total words
print( "type(words_list) : " , type(words_list) , "\nMemory address:", id(words_list), "\nTotal words:", len(words_list))


# Count unique words
word_dis_counts = Counter(words_list)
print( "\n\nCounter(words_list): ",  Counter(words_list) )

print( "\n\nCword_dis_counts: ",  word_dis_counts )

print( "\ntype(word_dis_counts): ", type(word_dis_counts) , "\nUnique/Distinct words len(word_dis_counts) :", len(word_dis_counts))

print( "\n\nWord_dis_counts.most_common() : ", word_dis_counts.most_common())

# Display each word and its count
print("\nWord List:\n")

for word, count in word_dis_counts.most_common():
    print(f"{word}: {count}")


# for word, count in word_dis_counts:
#    print(f"{word}: {count}")


data_set1 = set(word_dis_counts.most_common())
print("\n--------------------------------------" )
print("data_set ::", data_set1, "\nMemory address:", id(data_set1), "\nUnique/Distinct words len(data_set1) :", len(data_set1))


print("\n--------------------------------------" )
data_set2 = sorted(set(word_dis_counts))    
print("data_set ::",data_set2, "\n\nCount/len : " , len(data_set2),"\n")

