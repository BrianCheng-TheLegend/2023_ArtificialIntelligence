# Random Forest Classification for iris data
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

print(y)