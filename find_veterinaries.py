# import requests

# def find_nearby_veterinaries(location, radius=5000, api_key="YOUR_GOOGLE_API_KEY"):
#     """
#     Find nearby veterinary services based on location.

#     Parameters:
#     - location (str): The latitude and longitude of the search center in "lat,lng" format.
#     - radius (int): The radius to search within in meters (default is 5000).
#     - api_key (str): Your Google Places API key.

#     Returns:
#     - list: A list of dictionaries containing details about each veterinary service.
#     """
#     url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
#     params = {
#         'location': location,
#         'radius': radius,
#         'type': 'veterinary_care',
#         'key': api_key
#     }

#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         if data.get("results"):
#             return [
#                 {
#                     'name': vet.get('name'),
#                     'address': vet.get('vicinity'),
#                     'rating': vet.get('rating', 'N/A'),
#                     'user_ratings_total': vet.get('user_ratings_total', 0),
#                 }
#                 for vet in data['results']
#             ]
#     else:
#         print("Error:", response.status_code, response.text)
#     return []


# # --------------------------------------------------------------------------------------------------------------------




#     # import streamlit as st
#     # from geopy.geocoders import Nominatim
#     # from geopy.distance import geodesic
#     # import requests

#     # def fetch_current_location():
#     #     # Replace with actual API for real-time geolocation or use a mock location
#     #     # Alternatively, you can use 'geocoder' library to fetch location
#     #     response = requests.get("https://ipinfo.io/loc")  # Example using IP-based location API
#     #     if response.status_code == 200:
#     #         lat, lon = response.text.strip().split(',')
#     #         return float(lat), float(lon)
#     #     else:
#     #         st.error("Unable to fetch current location")
#     #         return None, None

#     # def find_nearest_vet(lat, lon):
#     #     # Implement the function to find nearest veterinary services
#     #     # Example logic; replace with actual API or dataset lookup as needed
#     #     geolocator = Nominatim(user_agent="geoapiExercises")
#     #     location = geolocator.reverse((lat, lon), language='en')
#     #     st.write(f"Nearby Veterinary Services near {location.address}")

#     # # Streamlit Interface
#     # st.title("Veterinary Finder")

#     # # Option to Manually Input Location
#     # st.write("Enter Latitude and Longitude or Fetch Current Location")

#     # latitude = st.number_input("Latitude", format="%.6f")
#     # longitude = st.number_input("Longitude", format="%.6f")

#     # if st.button("Fetch Current Location"):
#     #     latitude, longitude = fetch_current_location()
#     #     if latitude and longitude:
#     #         st.success(f"Location fetched: {latitude}, {longitude}")

#     # # Find Nearby Veterinary Services
#     # if st.button("Find Nearest Veterinary"):
#     #     if latitude and longitude:
#     #         find_nearest_vet(latitude, longitude)
#     #     else:
#     #         st.error("Please provide valid latitude and longitude.")




#---------------------------------------------------------


# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import streamlit as st

# def find_nearby_veterinaries(lat, lon):
#     # Initialize geolocator
#     geolocator = Nominatim(user_agent="veterinary_locator")
#     location = geolocator.reverse((lat, lon), language='en')
    
#     # Display the location for reference
#     if location:
#         st.write(f"Your Location: {location.address}")
#     else:
#         st.write("Could not fetch address for the coordinates.")

#     # Here, replace the logic with the API or dataset lookup for vet services
#     # This is a mock example for displaying purposes
#     vet_services = [
#         {"name": "City Vet Clinic", "lat": lat + 0.01, "lon": lon + 0.01},
#         {"name": "Pet Care Hospital", "lat": lat + 0.02, "lon": lon + 0.02}
#     ]
    
#     st.write("Nearby Veterinary Services:")
#     for service in vet_services:
#         distance = geodesic((lat, lon), (service["lat"], service["lon"])).km
#         st.write(f"{service['name']} - {distance:.2f} km away")

#     # Display on map
#     map_data = {
#         "lat": [service["lat"] for service in vet_services],
#         "lon": [service["lon"] for service in vet_services]
#     }
#     st.map(map_data)



#------------------------------------------------------------------------------


import requests
import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("PLACES_KEY")


def find_nearby_veterinaries(lat, lon, radius=5000, keyword="veterinary"):
    # print(lat, lon, radius, keyword)
    # print(lat, lon, radius)
    lat = str(round(float(lat),4))
    lon = str(round(float(lon),4))
    # print(lat, lon)
    url = (
        f"https://maps.gomaps.pro/maps/api/place/nearbysearch/json?location="
        f"{lat},{lon}&radius={radius}&types=food&name={keyword}&key={API_KEY}"

    )
    # print(url)
    try:
        response = requests.get(url)
        results = response.json().get("results", [])
        # print(results)
        if results:
            st.write("Nearby Veterinary Services:")
            for place in results:
                name = place.get("name")
                address = place.get("vicinity")
                st.write(f"{name} - {address}")
        else:
            st.warning("No veterinary services found nearby.")

    except Exception as e:
        st.error(f"Error retrieving data from GoMaps.pro API: {e}")

