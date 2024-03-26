import geopandas as gpd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

def spatial_analysis(data, eps=0.5, min_samples=5):
    """
    Perform spatial analysis on a GeoDataFrame.
    
    Parameters:
    data (GeoDataFrame): The input GeoDataFrame.
    eps (float): The maximum distance between two samples for them to be considered as in the same neighborhood.
    min_samples (int): The number of samples in a neighborhood for a point to be considered as a core point.
    
    Returns:
    GeoDataFrame: The output GeoDataFrame with a new column 'cluster' indicating the cluster to which each point belongs.
    """
    
    # Check if input is a GeoDataFrame
    if not isinstance(data, gpd.GeoDataFrame):
        raise ValueError("Input data must be a GeoDataFrame.")
    
    # Extract coordinates and scale them
    X = data[['x', 'y']].values
    X_scaled = StandardScaler().fit_transform(X)
    
    # Perform DBSCAN clustering
    dbscan = DBSCAN(eps=eps, min_samples=min_samples).fit(X_scaled)
    labels = dbscan.labels_
    
    # Add cluster labels to the GeoDataFrame
    data['cluster'] = labels
    
    return data
