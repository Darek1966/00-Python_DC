
import os
 
def CountWords(path):
    with open(path,'r', encoding='utf-8') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count
 
 
path = r'E:\Python\00 Python_DC\Sekcja_2\test.txt'
if os.path.isfile(path):
    print("There are {} words in the file {}".format(CountWords(path), path))
 
 
os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))
