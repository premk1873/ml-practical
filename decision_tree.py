pip install pandas scikit-learn
Aim: Write a program to implement Decision Tree.

from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

# Load data
url = "C:/Users/Lenovo/Downloads/pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(url, names=names)
array = dataframe.values

X = array[:, 0:8]
Y = array[:, 8]

# Create and train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X, Y)

# Display feature importance
print(names)
print(model.feature_importances_)
