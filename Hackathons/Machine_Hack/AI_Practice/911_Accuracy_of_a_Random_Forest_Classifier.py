"""
Find the accuracy of a random forest classifier given a fixed test size when getting trained on the SKLearn Wine Dataset.

Example 1:

Input:

N=0.33
Output:

0.9661016949152542
Example 2:

Input:

N=0.4
Output:

0.9444444444444444
"""


from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
def randomforest(N):
    # Load the Wine dataset
    wine = load_wine()
    X, y = wine.data, wine.target

    # Define the number of samples for the test set
    test_size = int(N * len(X))

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Create a Random Forest Classifier
    clf = RandomForestClassifier(random_state=42)

    # Fit the classifier on the training data
    clf.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy
  
  
# Test
N = 0.33
accuracy = randomforest(N)
print(accuracy)