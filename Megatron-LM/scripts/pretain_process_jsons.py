import sys
import json
import os

def file_names(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root,file))
    return L

input_dir = sys.argv[1]
output_file = sys.argv[2]

L = file_names(input_dir)

substring = '"text": ""'

with open(output_file, "w") as ofile:
    for input_file in L:
       with open(input_file, 'r') as ifile: 
           for doc in ifile.readlines():
               if substring not in doc:
                   ofile.write(doc)
