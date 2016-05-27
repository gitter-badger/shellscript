#!/usr/bin/env python

import subprocess
import sys

arg = sys.argv[1]
line = 0
data = ''
command = 0
done = True
file = open(arg, 'r')
contents = file.readlines()
while line <= len(contents):
    lin = contents[line-1]
    if line < len(contents):
        if lin == contents[len(contents)-1]:
            lin = lin
        else:
            lin = lin[:-1]
        contents[line-1] = lin
    line = line + 1
print contents
if done:
    while command <= len(contents):
        ccommand = contents[command-1]
        subprocess.call([ccommand], shell=True)
        command = command + 1