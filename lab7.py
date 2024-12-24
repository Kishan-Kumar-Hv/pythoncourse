import geopandas as gpd
import matplotlib.pyplot as plt

# Load the world shapefile from GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for India
india = world[world['name'] == 'India']

# Plot India's map
fig, ax = plt.subplots(figsize=(10, 12))
india.boundary.plot(ax=ax, color='black', linewidth=1)
ax.set_title("Map of India", fontsize=16)
plt.show()
