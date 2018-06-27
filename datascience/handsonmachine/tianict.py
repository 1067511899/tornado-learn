import csv
import numpy as np

with open('titanic.txt', 'r') as csvfile:
    titanic_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
#     row = titanic_reader.next()
#     row = titanic_reader[0]
#     feature_names = np.array(row)
    titanic_X, titanic_y = [], []
    for row in titanic_reader:
        titanic_X.append(row)
        titanic_y.append(row[2])
    titanic_X = np.array(titanic_X)
    titanic_y = np.array(titanic_y)
    feature_names = titanic_X[0]
    print(feature_names)
# print(titanic_X)
titanic_X = titanic_X[:, [1, 4, 10]]
print(titanic_X)
