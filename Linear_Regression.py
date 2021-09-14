import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

house_data = pd.read_csv('./house_data.csv')

house_data.head(5)

house_data.describe()

plt.scatter(house_data['sqft_living'], house_data['price'])

y = house_data['price']
x = house_data.drop(['price','id'],axis=1)

# train linear model on the data 
from sklearn.linear_model import LinearRegression

X = x.apply(pd.to_numeric, errors='coerce')
Y = y.apply(pd.to_numeric, errors='coerce')

X.fillna(0, inplace=True)
Y.fillna(0, inplace=True)

model = LinearRegression()

# split testing and training dataset
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 5)

print('x_train-shape : ',x_train.shape)
print('y_train-shape : ',y_train.shape)
print('x_test-shape : ',x_test.shape)
print('y_test-shape : ',y_test.shape)

print(model.fit(x_train, y_train))

print(model.score(x_test, y_test))