import sys
import random

<<<<<<< HEAD
file20 = sys.argv[1]
with open(file20, 'r') as f1:
    lines = f1.readlines()
=======
file2 = sys.argv[1]
with open(file2, 'r') as fi:
    lines = fi.readlines()
>>>>>>> hw_1b

for l in lines:
    if random.random() < .01:
        print(l)