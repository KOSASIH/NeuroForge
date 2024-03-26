import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.stattools import ccf
from statsmodels.graphics.tsaplots import plot_ccf

def time_series_analysis(data, target_variable, seasonal_period=12, plot=True):
    """
    Perform time series analysis on the given data.
    
    Parameters:
    data (pd.DataFrame): The input data.
    target_variable (str): The target variable for analysis.
    seasonal_period (int): The seasonal period of the data.
    plot (bool): Whether to plot the results.
    
    Returns:
    dict: A dictionary containing the results of the time series analysis.
    """
    
    # Decompose the time series data
    decomposition = seasonal_decompose(data[target_variable], model='multiplicative', period=seasonal_period)
    
    # Perform the Dickey-Fuller test for stationarity
    dftest = adfuller(data[target_variable], autolag='AIC')
    df_summary = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        df_summary['Critical Value (%s)' % key] = value
    
    # Plot the autocorrelation function (ACF) and the partial autocorrelation function (PACF)
    if plot:
        plot_acf(data[target_variable])
        plot_pacf(data[target_variable])
        plot_ccf(data[target_variable], data[target_variable].shift(1))
    
    # Return the results
    return {'Decomposition': decomposition, 'Dickey-Fuller Test': df_summary}
