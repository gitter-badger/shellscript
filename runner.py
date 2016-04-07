index = 0
file = 'example.ss'
data = ''
commands = []
import subprocess

with open(file, 'r') as myfile:
    data=myfile.read().replace('\n', '')
    
print data
sTagFound = False
eTagFound = False
rangeStart = 0
rangeEnd = 0

if '<shellscript>' in data and sTagFound = False:
    while sTagFound = False:
        
elif '<shellscript>' not in data:
    print 'Error: No starting tag was found.'
    
cmd = ['ssh', 'user@machine2',
       'mkdir -p output/dir; cat - > output/dir/file.dat']

p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

your_inmem_data = 'foobarbaz\0' * 1024 * 1024

for chunk_ix in range(0, len(your_inmem_data), 1024):
    chunk = your_inmem_data[chunk_ix:chunk_ix + 1024]