# Write a function to fit a linear regression model using scikit-learn 
# and predict the target variable for a given dataset.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Sample dataset
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 3 * X.squeeze() + 2 + np.random.randn(100)
df = pd.DataFrame({'X': X.squeeze(), 'y': y})

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the results
print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")