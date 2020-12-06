import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

data = pd.read_csv('datasets/napa.csv')

X = data.iloc[:, :3]
y = data.iloc[:, -1]

#splitting training and test set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#fitting model with training data
regressor.fit(X, y)
print(regressor)

print('Weight coefficients: ', model.coef_)
print('y-axis intercept: ', model.intercept_) 


pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[20, 35, 65]]))