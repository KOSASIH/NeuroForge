from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform automated machine learning
best_model, best_score = automated_machine_learning(X_train, X_test, y_train, y_test, task='classification')

# Print the best model and its score
print("Best Model:", best_model)
print("Best Score:", best_score)
