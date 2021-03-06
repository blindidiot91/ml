__author__ = 'joe'
from collections import Counter, defaultdict
import sys, os
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
)

rocksVMines=pd.read_csv(target_url,header=None,prefix="V")

#calculate correlations between real-valued attributes
dataRow2=rocksVMines.iloc[1,0:rocksVMines.shape[1]-1]
dataRow3=rocksVMines.iloc[2,0:rocksVMines.shape[1]-1]

plot.scatter(dataRow2,dataRow3)

plot.xlabel("2nd Attribute")
plot.ylabel(("3rd Attribute"))
plot.show()