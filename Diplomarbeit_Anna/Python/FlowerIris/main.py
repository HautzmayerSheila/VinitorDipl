# Load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB

from sklearn.svm import SVC

# Step 1 = Auslesen
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
flower_data = pd.read_csv(url, names=names)

# STEP 2 = Clean = erledigt

# NOTE Methoden
# (Zeile, Spalten)
# print(flower_data.shape)

# print(flower_data.head(10))

# print(flower_data.describe())

# print(flower_data.groupby('class').size())

# NOTE Plots

# flower_data.plot(kind='box',
#                  subplots=True,
#                  layout=(2,2),
#                  sharex=False,
#                  sharey=False)
# pyplot.show()
#
# flower_data.hist()
# pyplot.show()

# df = flower_data.drop(columns=["sepal-length", "sepal-width"])
#
# scatter_matrix(df)
# pyplot.show()

# STEP 3 Split Data

X = flower_data.drop(columns="class")
y = flower_data["class"]

X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Step 3.5 Create Models and choose

# models = []
# models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
# models.append(('LDA', LinearDiscriminantAnalysis()))
# models.append(('KNN', KNeighborsClassifier()))
# models.append(('CART', DecisionTreeClassifier()))
# models.append(('NB', GaussianNB()))
# models.append(('SVM', SVC(gamma='auto')))
# # evaluate each model in turn
# results = []
# names = []
#
# for name, model in models:
#     kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
#     cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
#     results.append(cv_results)
#     names.append(name)
#     print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# STEP 4 Create Model

model = SVC(gamma='auto')

#STEP 5 Train the model
model.fit(X_train, Y_train)

#STEP make predictions
predictions = model.predict(X_validation)

#print(accuracy_score(Y_validation, predictions))

#TODO herausfinden
#print(confusion_matrix(Y_validation, predictions))
#print(classification_report(Y_validation, predictions))

#TODO k-fold cross validation

