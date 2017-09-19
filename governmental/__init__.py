import csv
import json
import numpy as np
import matplotlib.pyplot as plt

with open('NHIS_OPEN_GJ_2015.csv', newline=' ') as makefile:
    reader = csv.reader(makefile, delimiter=' ', quotechar='|')
    for row in reader:
        print(row)
    print(reader)
