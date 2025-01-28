import osmnx as ox
import pandas as pd

# Define the place name for Greater London
place_name = "Greater London, United Kingdom"

# Query OpenStreetMap for all pharmacies in the area
print("Fetching pharmacy data from OpenStreetMap...")
pharmacies = ox.features_from_place(place_name, tags={"amenity": "pharmacy"})

# Filter relevant columns (name, geometry, and address if available)
pharmacies = pharmacies[["name", "geometry"]]

# Convert geometries to latitude and longitude
pharmacies["Latitude"] = pharmacies.geometry.centroid.y
pharmacies["Longitude"] = pharmacies.geometry.centroid.x

# Save to a CSV file
file_path = './data/osm_london_pharmacies.csv'
pharmacies.to_csv(file_path, index=False)

print(f"Successfully fetched {len(pharmacies)} pharmacies. Data saved to '{file_path}'")
