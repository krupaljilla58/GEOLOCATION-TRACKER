import requests
import folium

# Step 1: Get public IP address
ip_response = requests.get("https://api.ipify.org?format=json")
ip_address = ip_response.json()["ip"]

print("Your IP Address:", ip_address)

# Step 2: Get location details using IP
location_response = requests.get(f"https://ipinfo.io/{ip_address}/json")
location_data = location_response.json()

# Extract latitude and longitude
lat, lon = map(float, location_data["loc"].split(","))

city = location_data.get("city", "Unknown")
region = location_data.get("region", "Unknown")
country = location_data.get("country", "Unknown")

print(f"Location: {city}, {region}, {country}")
print(f"Latitude: {lat}, Longitude: {lon}")

# Step 3: Create map
user_map = folium.Map(location=[lat, lon], zoom_start=10)

# Add marker
folium.Marker(
    [lat, lon],
    popup=f"{city}, {region}, {country}",
    tooltip="Your Location"
).add_to(user_map)

# Step 4: Save map to HTML file
user_map.save("user_location_map.html")

print("Map saved as user_location_map.html")
