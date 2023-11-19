import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium

st.set_page_config(
    page_title="Location Map",
)


st.title('EvacuAid Hub')

# st.subheader('Map of nearby evacuation centers')

st.header('Sites Needing Aid')


df = pd.read_csv('marikina_evacuation_centers.csv',
                  usecols=['CENTER_M', 'LAT', 'LONG'])

# df.columns = ['Evacuation Center', 'latitude', 'longitude']
lat = list(df["LAT"])
long = list(df["LONG"])
evacuation_site = list(df["CENTER_M"])

map = folium.Map(location=[14.650068, 121.102258], zoom_start=16)


for lt, ln, ev in zip(lat, long, evacuation_site):
    folium.Marker(location=[lt, ln], popup=str(ev)).add_to(map)

st_date = st_folium(map, width=800)


# st.map(df,
#     latitude='latitude',
#     longitude='longitude',
#     color='#0044ff')