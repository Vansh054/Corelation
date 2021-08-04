import csv 
import numpy as np
from numpy.lib.function_base import corrcoef

f = open("data.csv")
object = csv.reader(f)
data = list(object)
data.pop(0)

marks = []
dayspresent = []

for i in range(len(data)):
    m = float(data[i][1])
    marks.append(m)
    d = float(data[i][2])
    dayspresent.append(d)

actualData = {"x" : marks, "y" : dayspresent}
correlation = np.corrcoef(actualData['x'],actualData['y'])
print(correlation)