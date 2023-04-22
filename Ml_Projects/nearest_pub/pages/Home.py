import streamlit as st
import pandas as pd
import numpy as np
import os 
pub_data =pd.read_csv(r'C:\Users\ASUS\Desktop\Internship\Ml_Projects\resources\data\open_pubs.csv')
pub_data.dropna(subset=['latitude', 'longitude'], inplace=True)
pub_data['longitude']=pd.to_numeric(pub_data['longitude'],errors='coerce')
pub_data['latitude']=pd.to_numeric(pub_data['latitude'],errors='coerce')
st.title(':red[Welcome to the UK Pub Finder App!]')
st.write("This app helps you  to find pubs in the United Kingdom.")
st.write("Use the navigation menu on the left to get started.")
    
# Show basic statistics about the dataset
st.header(":orange[Basic Information about the Data Set]")
st.write(f'**_:blue[Total number of pubs in dataset]_**: {len(pub_data)}')
st.write(f"**_:blue[Number of unique local authorities]_**: {pub_data['local_authority'].nunique()}")
st.write(f"**_:blue[Most common local authority]_**: {pub_data['local_authority'].mode()[0]}")

st.markdown(":orange[Dash Board Of Pub Data]")
st.dataframe(pub_data)

st.markdown(':orange[Areas with the most pubs]:')
top_areas = pub_data['local_authority'].value_counts().head(10)
st.bar_chart(top_areas)
    