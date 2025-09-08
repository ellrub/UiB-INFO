import pandas as pd
from pandas import read_csv, get_dummies
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
url = "/Users/ruben/Development/UiB-INFO/info180/Oblig2/data/party_data.csv"
names = ['gender', 'age', 'study', 'activity', 'music', 'is dancer', 'ok guest']
dataset = read_csv(url, names=names, header=0)

# One-hot encode categorical columns (excluding 'age')
categorical_columns = ['gender', 'study', 'activity', 'music', 'is dancer', 'ok guest']
dataset_encoded = get_dummies(dataset, columns=categorical_columns)

print(dataset_encoded.head(20))  # Print the first 20 lines

# Ensure all columns are numeric
dataset_encoded = dataset_encoded.apply(pd.to_numeric, errors='coerce')

# Handle NaN values by filling them with 0
dataset_encoded = dataset_encoded.fillna(0)

# Check data types
print(dataset_encoded.dtypes)

# Visualize the dataset
dataset_encoded.plot(kind='box', subplots=True, layout=(4, 4), sharex=False, sharey=False)
plt.show()

dataset_encoded.hist()
plt.show()

scatter_matrix(dataset_encoded)
plt.show()

# Split the dataset into features and target variable
X = dataset_encoded.drop('age', axis=1)
y = dataset_encoded['age']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# K-Nearest Neighbors Classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"KNN Accuracy: {accuracy_knn}")

# Logistic Regression with regularization (penalty='l2')
log_reg_l2 = LogisticRegression(penalty='l2', solver='liblinear')
log_reg_l2.fit(X_train, y_train)
y_pred_log_reg_l2 = log_reg_l2.predict(X_test)
accuracy_log_reg_l2 = accuracy_score(y_test, y_pred_log_reg_l2)
print(f"Logistic Regression with L2 penalty Accuracy: {accuracy_log_reg_l2}")

# Logistic Regression without regularization (penalty=None)
log_reg_none = LogisticRegression(penalty='none', solver='lbfgs', max_iter=1000)
log_reg_none.fit(X_train, y_train)
y_pred_log_reg_none = log_reg_none.predict(X_test)
accuracy_log_reg_none = accuracy_score(y_test, y_pred_log_reg_none)
print(f"Logistic Regression without penalty Accuracy: {accuracy_log_reg_none}")



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

# dataset.plot(kind = 'box', subplots = True, layout = (2, 2), sharex = False, sharey = False)
# plt.show()
# dataset.hist()
# plt.show()
# scatter_matrix(dataset)
# plt.show()

