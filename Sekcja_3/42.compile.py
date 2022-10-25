
from numpy import source
import time

source = 'reportLine += 1'

reportLine = 0
start = time.time()         # pobieram aktualny czas
for i in range (100000):    # za pomocą for 1000 razy wykonuję polecenie
    exec(source)
stop = time.time()          # żeby obliczyć czas
time_not_compiled = stop - start    # liczę ile minęło czasu

start = time.time()
# kompilacja (co należy skompilować, plik -ścieżka, tryb exec lub eval, single)
sourceCompiled = compile(source, 'Źródło zmiennej wewnętrzej', 'exec')
for i in range(100000):
    exec(sourceCompiled)
stop = time.time() 
time_compiled = stop - start  

print(time_not_compiled)
print(time_compiled)
print(time_not_compiled / time_compiled)
