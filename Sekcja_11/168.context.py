'''
with open(r'E:\Python\00 Python_DC\temp\file.txt', 'w+') as file:   # context menager
    file.writelines('SUKCES')
'''
import time

class time_measure:

    def __init__(self):
        pass

    def __enter__(self):
        print('entering...')
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting...')
        self.__stop = time.time()
        self.__difference = self.__stop - self.__start
        print('Execution time: {}'.format(self.__difference))

with time_measure () as my_timer:       # context menager
    time.sleep(3)
