index = 0
file = 'example.ss'
data = ''

with open(file, 'r') as myfile:
    data=myfile.read().replace('\n', '')
    
print data

import subprocess

cmd = ['ssh', 'user@machine2',
       'mkdir -p output/dir; cat - > output/dir/file.dat']

p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

your_inmem_data = 'foobarbaz\0' * 1024 * 1024

for chunk_ix in range(0, len(your_inmem_data), 1024):
    chunk = your_inmem_data[chunk_ix:chunk_ix + 1024]