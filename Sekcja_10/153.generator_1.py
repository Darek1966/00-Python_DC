'''
file = open(r'E:\Python\00 Python_DC\temp\data.txt')    # tak robić nie zalecane

data = file.read()

for line in data.splitlines():
    if line.startswith('ACTION'):
        print(line)
'''
'''
file = open(r'E:\Python\00 Python_DC\temp\data.txt')    # inny sposób - lepszy

for line in file:
    if line.startswith("ACTION"):
        print(line.replace('\n', ''))

file.close()
'''
'''
file = open(r'E:\Python\00 Python_DC\temp\data.txt')    # inny sposób

records = []

for line in file:
    if ':'in line:
        type, action = line.rstrip('\n').split(':', 1)
        record = (type, action)
        records.append(record)

print(records)

file.close()
'''
def get_records(filePath):      # użycie generatora
    print('---opening file---')
    file = open(filePath)

    for line in file:
        if ':' in line:
            type, action = line.rstrip("\n").split(':', 1)
            record = (type, action)
            yield record

    print('---closing file---')
    file.close()

for record in get_records(r'E:\Python\00 Python_DC\temp\data.txt'):
    print('The type is {} and the action is {}'.format(record[0], record[1]))
