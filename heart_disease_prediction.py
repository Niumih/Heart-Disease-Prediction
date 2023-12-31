# -*- coding: utf-8 -*-
"""Heart Disease Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14j0adRarfBslPSmprazeLsJPIrrXsA6-
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data = pd.read_csv('/content/heart_disease_data.csv')

heart_data.head()

heart_data.tail()

heart_data.shape

heart_data.info()

heart_data.isnull().sum()

heart_data.describe()

heart_data['target'].value_counts()

"""1-> defective heart
0-> healthy heart
"""

A = heart_data.drop(columns='target', axis=1)
B = heart_data['target']

print(A)

print(B)

A_train, A_test, B_train, B_test = train_test_split(A,B, test_size= 0.2, stratify = B, random_state=3)

print(A.shape, A_train.shape, A_test.shape )

model=LogisticRegression()

model.fit(A_train, B_train)

A_train_prediction = model.predict(A_train)
training_data_accuracy = accuracy_score(A_train_prediction, B_train)

print('Accuracy on Training data: ',training_data_accuracy )

A_test_prediction = model.predict(A_test)
test_data_accuracy = accuracy_score(A_test_prediction, B_test)

print('Accuracy on Test data: ',test_data_accuracy )

input_data = (56,1,1,120,236,0,1,178,0,0.8,2,0,2)

#numpy array
input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped )
print(prediction)

if(prediction[0]==0):
  print('The person doesnot have heart disease')
else:
   print('The person has heart disease')

input_data = (70,1,2,160,269,0,1,112,1,2.9,1,1,3)

#numpy array
input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped )
print(prediction)

if(prediction[0]==0):
  print('The person doesnot have heart disease')
else:
   print('The person has heart disease')