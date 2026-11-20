pip install matplotlib scikit-learn
Aim: Implement the classification model using clustering for the following
techniques with K means clustering
Code:
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
######
from sklearn.cluster import KMeans
data = list(zip(x, y))
inertias = []
for i in range(1,11):
 kmeans = KMeans(n_clusters=i)
 kmeans.fit(data)
 inertias.append(kmeans.inertia_)
plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters&#39')
plt.ylabel('Inertia')
plt.show()
#####
data = list(zip(x, y))
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
plt.scatter(x, y, c=kmeans.labels_)
plt.show()
