import streamlit as st
import pandas as pd
import numpy as np
import os 
import folium
from folium.plugins import MarkerCluster
import math
from streamlit_folium import folium_static
from scipy.spatial import distance




# Define function to clean the pub data and remove any rows with null values in Latitude and Longitude columns

pub_data =pd.read_csv(r'C:\Users\ASUS\Desktop\Internship\Ml_Projects\resources\data\open_pubs.csv')
pub_data.dropna(subset=['latitude', 'longitude'], inplace=True)
pub_data=pub_data.replace('\\N',np.nan)
pub_data['longitude']=pd.to_numeric(pub_data['longitude'],errors='coerce')
pub_data['latitude']=pd.to_numeric(pub_data['latitude'],errors='coerce')    
# Define function to calculate Euclidean distance between two coordinates
st.title(":orange[Find the Nearest Pubs]\U0001F37A ")
st.markdown(":red[Enter your location to find the nearest pubs.]")

# Get user input
lat = st.number_input("Latitude:", value=51.5074, step=0.0001)
lon = st.number_input("Longitude:", value=-0.1278, step=0.0001)

 # Find nearest pubs
pub_data["distance"] = pub_data.apply(lambda row: ((lat-row["latitude"])**2 + (lon-row["longitude"])**2)**0.5, axis=1)
nearest_pubs = pub_data.sort_values("distance").head(5)
st.markdown(f":red[The nearest pubs to your location are:]")
st.table(nearest_pubs[["name", "address", "local_authority"]])

# Create map with nearest pubs markers
m = folium.Map(location=[lat, lon], zoom_start=13)
for _, pub in nearest_pubs.iterrows():
    folium.Marker(location=[pub["latitude"], pub["longitude"]], tooltip=pub["name"]).add_to(m)
    folium_static(m)

st.write('\U0001F37A Cheers! Enjoy your beer!')