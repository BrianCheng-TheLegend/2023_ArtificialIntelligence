# Random Forest Classification for iris data
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
x, y = iris.data, iris.target

RFC_10 = RandomForestClassifier(n_estimators=10, oob_score=True)
RFC_10.fit(x,y)
RFC_20 = RandomForestClassifier(n_estimators=20, oob_score=True)
RFC_20.fit(x,y)
RFC_30 = RandomForestClassifier(n_estimators=30, oob_score=True)
RFC_30.fit(x,y)
print(' Out-of-Bag errors with 10 : ',RFC_10.oob_score_)
print(' Out-of-Bag errors with 20 : ',RFC_20.oob_score_)
print(' Out-of-Bag errors with 30 : ',RFC_30.oob_score_)

# # Results
#  Out-of-Bag errors with 10 :  0.9466666666666667
#  Out-of-Bag errors with 20 :  0.9333333333333333
#  Out-of-Bag errors with 30 :  0.9533333333333334
