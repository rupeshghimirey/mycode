#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import time
from geopy.geocoders import Nominatim

URL = "http://api.open-notify.org/iss-now.json"


def main():
    resp = requests.get(URL).json()
    geolocator = Nominatim(user_agent="MyApp")
    lon = resp['iss_position']['longitude']
    lat = resp['iss_position']['latitude']
    coordinates = f"{lat} , {lat}"
    location = geolocator.reverse(coordinates)
    city = location.raw['address']['city']
    country = location.raw['address']['country']
    print(f"City: {city}\nCountry: {country}")

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"Current time: {current_time}")
    print(
    f"CURRENT LOCATION OF ISS:\nLon: {lon}\nLat: {lat}")

if __name__ == "__main__":
    main()

