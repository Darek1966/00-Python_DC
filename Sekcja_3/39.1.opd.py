
import os
 

files_to_process = [
    r"E:\Python\00 Python_DC\Sekcja_3\math_sin_square.py",
    r"E:\Python\00 Python_DC\Sekcja_3\math_square_root.py"
    ]
 
# wyświetl nazwę pliku (skorzystaj z funkcji os.path.basename z modułu os)
# otwórz dany plik i wczytaj go do zmiennej source
for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
# Wykonaj ten skrypt
        exec(source)
