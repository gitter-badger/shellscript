'''
Created by Baran Skistad, bjskistad on GitHub. 
Please give credit to Baran Skistad if you use this.
'''
index = 0
file = 'example.shs'
data = ''
loop = 0
loopString = ''
commands = []
command = 0
done = False
import subprocess

with open(file, 'r') as myfile:
    data=myfile.read().replace('\n', '')
    
sTagFound = False
eTagFound = False
rangeStart = 0
rangeEnd = 0

if '<shellscript>' in data and sTagFound == False:
    while sTagFound == False:
        if loop == 10:
            loop = 0
            loopString = 0
        while loop < 9:
            loopString = loopString + data[index + loop]
            if loopString == '<shellscript>':
                sTagFound = True
elif '<shellscript>' not in data:
    print 'Error: No starting tag was found.'

while not done and sTagFound:
    done = False # had to put something there
    

if done:
    while command <= len(commands):
        subprocess.call(commands[command], shell=True)
        command = command + 1
