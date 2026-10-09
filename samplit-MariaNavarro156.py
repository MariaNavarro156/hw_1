import sys
import random

file20 = sys.argv[1]
with open(file20, 'r') as f1:
    lines = f1.readlines()

for line in lines:
    if random.random() < .01:
        print(line)