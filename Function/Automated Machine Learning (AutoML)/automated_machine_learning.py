import numpy as np
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, mean_squared_error

def automated_machine_learning(X_train, X_test, y_train, y_test, task='classification', n_jobs=-1):
    """
    Automated Machine Learning function that handles the entire process of building, training, and tuning machine learning models.
    
    Parameters:
    X_train (array): Training data features
    X_test (array): Testing data features
    y_train (array): Training data labels
    y_test (array): Testing data labels
    task (str): 'classification' or 'regression'
    n_jobs (int): Number of parallel jobs to run. -1 means using all processors.
    
    Returns:
    best_model (object): The best model found after automated tuning
    best_score (float): The best score achieved by the best model
    """
    
    # Define the models to be used for the task
    if task == 'classification':
        models = [
            ('logistic_regression', LogisticRegression()),
            ('random_forest', RandomForestClassifier()),
            ('k_neighbors', KNeighborsClassifier()),
            ('svm', SVC())
        ]
    elif task == 'regression':
        models = [
            ('linear_regression', LinearRegression()),
            ('random_forest', RandomForestRegressor()),
            ('k_neighbors', KNeighborsRegressor()),
            ('svm', SVR())
        ]
    else:
        raise ValueError("Invalid task. Choose either 'classification' or 'regression'.")
    
    # Define the parameters for each model
    parameters = {
        'logistic_regression': {'C': [0.001, 0.01, 0.1, 1, 10, 100]},
        'random_forest': {'n_estimators': [10, 50, 100, 200], 'max_depth': [None, 10, 20, 30]},
        'k_neighbors': {'n_neighbors': [3, 5, 7, 9]},
        'svm': {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
    }
    
    # Initialize the best score and model
    best_score = float('-inf') if task == 'classification' else float('inf')
    best_model = None
    
    # Iterate over the models and perform automated tuning
    for model_name, model in models:
        # Perform a randomized search for hyperparameter tuning
        search = RandomizedSearchCV(model, parameters[model_name], n_jobs=n_jobs, cv=5)
        search.fit(X_train, y_train)
        
        # Evaluate the model on the test set
        y_pred = search.predict(X_test)
        score = accuracy_score(y_test, y_pred) if task == 'classification' else mean_squared_error(y_test, y_pred)
        
        # Update the best score and model if necessary
        if (task == 'classification' and score > best_score) or (task == 'regression' and score < best_score):
            best_score = score
            best_model = search.best_estimator_
    
    return best_model, best_score
