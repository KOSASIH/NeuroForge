# Load a GeoDataFrame from a file
data = gpd.read_file("path/to/your/data.geojson")

# Perform spatial analysis
result = spatial_analysis(data, eps=0.5, min_samples=5)

# Plot the result
fig, ax = plt.subplots()
result.plot(column='cluster', ax=ax)
plt.show()
