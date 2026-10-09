import sys
import random

file2 = sys.argv[1]
with open(file2, 'r') as fi:
    lines = fi.readlines()

for l in lines:
    if random.random() < .01:
        print(l)