from pandas import read_csv, get_dummies
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OrdinalEncoder

# Load the dataset
url = 'D:/Web/Projects/UiB-INFO/info180/Oblig2/data/party_data.csv'
names = ['gender', 'age', 'study', 'activity', 'music', 'is dancer', 'ok guest']
dataset = read_csv(url, names = names)

# ============ Nearest Neighbors ============ #
target = dataset['ok guest']
features = dataset.drop('ok guest', axis = 1)

# One-Hot Encoding for features
features_encoded = get_dummies(features)

# Ordinal Encoding for the remaining categorical variables
encoder = OrdinalEncoder()
features_encoded = encoder.fit_transform(features_encoded)

# Combine the encoded features and target
X = features_encoded
y = target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 1)

# Function to train and evaluate KNN model
def train_evaluate_knn(k):
    model = KNeighborsClassifier(n_neighbors = k)
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    conf_matrix = confusion_matrix(y_test, y_pred_test)
    precision = precision_score(y_test, y_pred_test, pos_label = 'ok')
    print(f'K = {k}:')
    print(f'  Accuracy (Train): {accuracy_train}')
    print(f'  Accuracy (Test): {accuracy_test}')
    print(f'  Confusion Matrix:\n{conf_matrix}')
    print(f'  Precision (ok): {precision}')
    print(f'  Overfitting: {accuracy_train - accuracy_test}\n')

# Train and evaluate KNN model with different values of k
for k in [3, 5, 11, 17]:
    train_evaluate_knn(k)

# ============ Logistic Regression ============ #
features_encoded_lr = get_dummies(features, drop_first = True)

# Split the dataset into features (X) and target (y)
X_lr = features_encoded_lr
y_lr = target

# Split the dataset into training and testing sets
X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size = 0.20, random_state = 1)

# Function to train and evaluate Logistic Regression model
def train_evaluate_lr(penalty):
    model = LogisticRegression(penalty=penalty, solver='liblinear' if penalty else 'newton-cg')
    model.fit(X_train_lr, y_train_lr)
    y_pred_train = model.predict(X_train_lr)
    y_pred_test = model.predict(X_test_lr)
    accuracy_train = accuracy_score(y_train_lr, y_pred_train)
    accuracy_test = accuracy_score(y_test_lr, y_pred_test)
    conf_matrix = confusion_matrix(y_test_lr, y_pred_test)
    precision = precision_score(y_test_lr, y_pred_test, pos_label = 'ok')
    print(f'Logistic Regression (penalty={penalty}):')
    print(f'  Accuracy (Train): {accuracy_train}')
    print(f'  Accuracy (Test): {accuracy_test}')
    print(f'  Confusion Matrix:\n{conf_matrix}')
    print(f'  Precision (ok): {precision}')
    print(f'  Overfitting: {accuracy_train - accuracy_test}\n')

# Train and evaluate Logistic Regression model with different penalties
train_evaluate_lr('l2')
train_evaluate_lr(None)

# ============ Decision Tree ============ #
def train_evaluate_dt(criterion):
    model = DecisionTreeClassifier(criterion = criterion)
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    conf_matrix = confusion_matrix(y_test, y_pred_test)
    precision = precision_score(y_test, y_pred_test, pos_label='ok')
    print(f'Decision Tree (criterion={criterion}):')
    print(f'  Accuracy (Train): {accuracy_train}')
    print(f'  Accuracy (Test): {accuracy_test}')
    print(f'  Confusion Matrix:\n{conf_matrix}')
    print(f'  Precision (ok): {precision}')
    print(f'  Overfitting: {accuracy_train - accuracy_test}\n')

# Train and evaluate Decision Tree model with different criteria
train_evaluate_dt('gini')
train_evaluate_dt('entropy')