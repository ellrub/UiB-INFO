from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import NuSVC

...
# Load dataset
url = "/Users/ruben/Development/UiB-INFO/info180/Oblig2/data/party_data.csv"
names = [ 'gender', 'age', 'study', 'activity', 'music', 'is dancer', 'ok guest' ]
dataset = read_csv(url, names=names)

# print(dataset.shape)
# print(dataset.head(20))
# print(dataset.describe())
# print(dataset.groupby('gender').size())
# print("===================")
# print(dataset.groupby('age').size())
# print("===================")
# print(dataset.groupby('study').size())
# print("===================")
# print(dataset.groupby('activity').size())
# print("===================")
# print(dataset.groupby('music').size())
# print("===================")
# print(dataset.groupby('is dancer').size())
# print("===================")
# print(dataset.groupby('ok guest').size())

dataset.plot(kind = 'box', subplots = True, layout = (2, 2), sharex = False, sharey = False)
plt.show()
dataset.hist()
plt.show()