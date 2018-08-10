# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 17:35:26 2018

@author: madon
The data is checking , Age, Number of Complaints, Monthly Payment in Ksh
Number of contacts the user has, and Swap Agent.
"""

import pandas as pd
import seaborn as sns
sns.set_palette('husl')
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df = pd.read_csv("customer_data.csv")

print(df)

'''
df.describe()

df.info()
'''
 

df['Swap Agent'].value_counts()
tmp = df.drop('Id', axis=1)
g = sns.pairplot(tmp, hue='Swap Agent', markers='+')
plt.show()

print("Predicition trial\n")

X = df.iloc[:,:-1]

y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

lr = LogisticRegression()

lr.fit(X_train, y_train)

prediction_values = lr.predict(X_test)

print(prediction_values)

print("Testing accuracy\n")
plt.xlabel('Swap fraud occurrences')
plt.ylabel('Accuracy Score')
plt.title('Accuracy Scores for Swap Fraud')
plt.show()