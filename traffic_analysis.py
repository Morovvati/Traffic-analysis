import requests
from geopy.distance import geodesic

# Google Maps API Key (شما باید این کلید را از Google Cloud Console دریافت کنید)
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

# Function to get traffic data from Google Maps Traffic API
def get_traffic_data(latitude, longitude):
    """
    دریافت وضعیت ترافیک از Google Maps Traffic API بر اساس مختصات
    """
    url = f"https://maps.googleapis.com/maps/api/traffic/traffic.json?latlng={latitude},{longitude}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        traffic_data = response.json()
        # Assuming you have an API returning the traffic data status (example)
        if traffic_data["status"] == "heavy":
            return True
        else:
            return False
    else:
        print("Failed to retrieve traffic data.")
        return False

# Function to check if there is traffic at a given point
def check_traffic(latitude, longitude, radius=0.5):
    """
    latitude: عرض جغرافیایی نقطه
    longitude: طول جغرافیایی نقطه
    radius: شعاع جستجو در کیلومتر
    """
    point = (latitude, longitude)
    
    # فرض بر این است که نقاط ترافیک آنلاین از یک API دریافت می‌شوند
    if get_traffic_data(latitude, longitude):
        return "Heavy traffic detected in this area."
    else:
        return "No traffic detected in this area."

# ورودی مختصات از کاربر
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

# بررسی وضعیت ترافیک
result = check_traffic(latitude, longitude)
print(result)
