import pandas as pd
import numpy as np
from geopy.distance import geodesic

# Load traffic data from CSV file
data = pd.read_csv('traffic_data.csv')

# Preprocessing (remove missing values)
data.dropna(subset=['latitude', 'longitude', 'speed'], inplace=True)

# Function to check traffic at a given point
def check_traffic(latitude, longitude, threshold=20, radius=0.5):
    """
    latitude: Latitude of the point to check
    longitude: Longitude of the point to check
    threshold: Speed threshold (traffic is heavy if below this value)
    radius: Search radius in kilometers
    """
    point = (latitude, longitude)
    speeds = []
    
    for _, row in data.iterrows():
        traffic_point = (row['latitude'], row['longitude'])
        distance = geodesic(point, traffic_point).km
        
        if distance <= radius:  # Check points within the radius
            speeds.append(row['speed'])
    
    if speeds:
        avg_speed = np.mean(speeds)
        print(f"Average speed in this area: {avg_speed:.2f} km/h")
        if avg_speed < threshold:
            return "Heavy traffic."
        else:
            return "Traffic is smooth."
    else:
        return "No data available within the specified radius."

# Get user input
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

# Check traffic status
result = check_traffic(latitude, longitude)
print(result)
