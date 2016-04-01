file = raw_input('file')

with open(file, 'r') as myfile:
    data=myfile.read().replace('\n', '')
