import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class StreamingDataProcessor:
    def __init__(self, window_size=100, model=RandomForestRegressor()):
        self.window_size = window_size
        self.model = model
        self.data_window = pd.DataFrame()
        self.scaler = StandardScaler()

    def process_data(self, data):
        # Append new data to the data window
        self.data_window = self.data_window.append(data)

        # If the data window is full, remove the oldest data point
        if len(self.data_window) > self.window_size:
            self.data_window = self.data_window.iloc[1:]

        # Scale the data using the StandardScaler
        self.scaler.fit(self.data_window)
        scaled_data = self.scaler.transform(self.data_window)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(scaled_data[:-1], scaled_data[-1], test_size=0.2, random_state=42)

        # Train the model on the training data
        self.model.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = self.model.predict(X_test)

        # Calculate the mean squared error of the predictions
        mse = mean_squared_error(y_test, y_pred)

        return mse
