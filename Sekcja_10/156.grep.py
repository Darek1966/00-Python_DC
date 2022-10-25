
import os

path = r'E:\Python\00 Python_DC\Sekcja_7'
search_string = 'Ford'
file_extension = '.py'

for dir_name, subdirs, filenames in os.walk(path):
    #print(dir_name, subdirs, filenames)
    for filename in filenames:
        if filename.endswith(file_extension):
            fullFileName = os.path.join(dir_name, filename)
            for line in open(fullFileName):
                if search_string in line:
                    print(filename)

def generate_files(base_dir, file_extension):       # generator
    for dir_name, subdirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullFileName = os.path.join(dir_name, filename)
                yield fullFileName

def grep_files(search_string, files):               # drugi generator
    for file in files:
        with open(file) as text:
            if search_string in text.read():
                yield file

files_generator = generate_files(path, file_extension)

for file in grep_files(search_string, files_generator):
    print(file)
