import sys
import random

file = sys.argv[1]
with open(file, 'r') as f:
    lines = f.readlines()

for line in lines:
    if random.random() < .01:
        print(line)