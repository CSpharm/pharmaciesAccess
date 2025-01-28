import pandas as pd

# Step1: Load the CSV file
file_path = './data/osm_london_pharmacies.csv'
pharmacies = pd.read_csv(file_path)

# Preview the dataset
print(pharmacies.head())

# Step 2: Create a Folium Map
import folium

# Initialize a Folium map centered at London
map_london = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# Add markers for each pharmacy
for _, row in pharmacies.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['name']}</b>",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(map_london)

# Save the map to an HTML file
map_london.save("london_pharmacies_map.html")
