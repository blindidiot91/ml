__author__ = 'joe'
from collections import Counter, defaultdict
import sys, os
import pandas as pd
# from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked Weight', 'Viscera weight',
                   'Shell weight', 'Rings']

print abalone.head()
print abalone.tail()

summary = abalone.describe()
print summary

# box plot the real-valued attributes, convert to array for plot routine
array = abalone.iloc[:, 1:9].values
boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
show()

# the last column(rings) is out of scale with the rest
array2 = abalone.iloc[:, 1:8].values
boxplot(array2)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
show()

# removing an array is alright but the optimal feature is to renormalize values by plotting them
# as std deviations of the mean
abaloneNormalized = abalone.iloc[:, 1:9]

for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]

abaloneNormalized.iloc[:, i:(i + 1)] = (abaloneNormalized.iloc[:, i:(i + 1)]-mean) / sd

array3=abaloneNormalized.values
boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized"))
show()