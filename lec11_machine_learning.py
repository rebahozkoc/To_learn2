from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
names = ['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',
'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
'fractal_dimension_se', 'radius_worst', 'texture_worst',
'perimeter_worst', 'area_worst', 'smoothness_worst',
'compactness_worst', 'concavity_worst', 'concave points_worst',
'symmetry_worst', 'fractal_dimension_worst', 'Unnamed: 32']
df = pd.read_csv(url, names=names)

print(df.shape)
print(df.head())
print(df.describe())

df.drop(["id"], 1, inplace=True)

df.isnull().sum()
#Drop the column with all missing values (na, NAN, NaN)
df = df.dropna(axis=1)
print(df.shape)

#Visualize diagnosis counts
sns.countplot(df['diagnosis'], label="Count")
print(df['diagnosis'].value_counts())

#Transform/Encode the column diagnosis
#Change all 'M' to 1 and all 'B' to 0 in the diagnosis col
dictionary = {'M':1, 'B':0}
df.diagnosis = [dictionary[item] for item in df.diagnosis]

print(df.head())

print(df.corr())

plt.figure(figsize=(20,20))
sns.heatmap(df.iloc[:,1:].corr(), annot=True, fmt='.0%')

#Split the data into independent 'X' and dependent 'Y' variables
X = df.iloc[:, 1:].values
Y = df.iloc[:, 0].values


#Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
X = sc.fit_transform(X)

# Split the dataset into 75% Training set and 25% Testing set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy',random_state = 42)
print(forest.fit(X_train, Y_train))

print('Random Forest Classifier Training Accuracy:', forest.score(X_train, Y_train))
