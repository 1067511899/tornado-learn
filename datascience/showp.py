import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X = []
f = open('dlzbnew.txt', encoding='UTF-8')

for v in f:
    tmp = v.strip().split(',')
#     print(tmp, tmp[2], tmp[3])
    if float(tmp[3]) > 1000:
        print(tmp[3])
    X.append([float(tmp[2]), float(tmp[3])])
f.close()
X = np.array(X)
print(X)
n_clusters = 5
cls = KMeans(n_clusters).fit(X)
cls.labels_
markers = ['^', 'x', 'o', '*', '+']

for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c='b', alpha=0.5)

plt.title('')
plt.show()
