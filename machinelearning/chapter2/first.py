__author__ = 'mike_bowles'

from urllib import request
import numpy as np
import pylab
import scipy.stats as stats
# read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = request.urlopen(target_url)

# arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
    line = line.decode('utf-8')

# split on comma
    row = line.strip().split(",")

    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])
type = [0] * 3
colCounts = []
# generate summary statistics for column 3 (e.g.)
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))
stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()
