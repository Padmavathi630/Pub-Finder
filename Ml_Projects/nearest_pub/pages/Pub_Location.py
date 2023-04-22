import streamlit as st
import pandas as pd
import numpy as np
import os 
import folium
from folium.plugins import MarkerCluster
import math
from streamlit_folium import folium_static




# Define function to clean the pub data and remove any rows with null values in Latitude and Longitude columns

pub_data =pd.read_csv(r'C:\Users\ASUS\Desktop\Internship\Ml_Projects\resources\data\open_pubs.csv')
pub_data.dropna(subset=['latitude', 'longitude'], inplace=True)
pub_data['longitude']=pd.to_numeric(pub_data['longitude'],errors='coerce')
pub_data['latitude']=pd.to_numeric(pub_data['latitude'],errors='coerce')
st.set_page_config(page_title="Pub Finder APP", page_icon=":beers:")
st.title(":orange[Find Pubs By Location]\U0001F37A ")

#user input
location_type = st.radio(":orange[Choose a location type]", ["Postal Code", "Local Authority"])

if location_type == "Postal Code":
    postal_code = st.text_input("Enter a postal code")
    filtered_data = pub_data[pub_data["postcode"].str.startswith(postal_code)]

elif location_type == "Local Authority":
    local_authority = st.selectbox("Enter a local authority:",pub_data["local_authority"].unique())
    filtered_data = pub_data[pub_data["local_authority"] == local_authority]

    # Display map
    if len(filtered_data) > 0:
        st.write(":red[Number of pubs found]:", len(filtered_data))

        # Create map
        m = folium.Map(location=[filtered_data["latitude"].mean(), filtered_data["longitude"].mean()], zoom_start=12)
        marker_cluster = MarkerCluster().add_to(m)
        for index, row in filtered_data.iterrows():
            if not math.isnan(row['latitude']) and not math.isnan(row['longitude']):
                folium.Marker([row['latitude'], row['longitude']]).add_to(marker_cluster)

        # Display map
        folium_static(m)
else:
    st.write("No pubs found")