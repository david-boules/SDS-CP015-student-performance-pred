# Multiple Linear Regression

# 1.Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns



# 2.Importing the dataset
dataset1 = pd.read_csv('C:/Tejinder/student-mat.csv', sep=';', header=0)  # Header is in the first row
dataset2 = pd.read_csv('C:/Tejinder/student-por.csv', sep=';', header=0)  # Header is in the first row

X = dataset1.iloc[:, :-1].values
y = dataset1.iloc[:, -1].values

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# Features to encode
categorical_features_indices = [ 0,1,3,4,5,8,9,10,11,15,16,17,18,19,20,21,22]
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_features_indices)], remainder='passthrough')
X = np.array(ct.fit_transform(X))

dataset_encd = pd.DataFrame(X)
dataset1.to_csv('C:/Tejinder/SDS/Student Performance Analysis/student+performance/student/output_encd.csv', index=False)