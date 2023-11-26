import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
import pydeck as pdk
from pretty_notification_box import notification_box

#ORIGNAL
st.set_page_config(
    page_title="Location Map",
)


st.title('EvacuAid Hub')

st.header('Sites Needing Aid')


df = pd.read_csv('marikina_evacuation_centers.csv',
                  usecols=['CENTER_M', 'LAT', 'LONG'])

lat = list(df["LAT"])
long = list(df["LONG"])
evacuation_site = list(df["CENTER_M"])


st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=14.650068,
        longitude=121.102258,
        zoom=13,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[LONG, LAT]',
            get_color='[200, 30, 0, 160]',
            get_radius=100,
            pickable=True,
            auto_highlight=True,
        ),
    ], tooltip={
        "text": "{CENTER_M}",
        "style": {
            "backgroundColor": "steelblue",
            "color": "white"
        },
    }
))

notice = "Please note that any data or information here is for " \
         "demonstration purposes only, as part of submission " \
         "for the MLH Hackathon"

styles = {'material-icons':{'color': 'red'},
          'title': {'font-weight':'bold'},
          'notification-content-container': {'':''},
          'title-text-url-container': {'',''},
          'notification-text-link-close-container': {'',''},
          'external-link': {'',''},
          'close-button': {'',''}}

notification_box(icon='warning', title='Note', textDisplay=f'{notice}',
                 externalLink='', url='', styles=None, key='foo')

# THIS WORKS
# st.map(df,
#     latitude='LAT',
#     longitude='LONG',
#     zoom=13,
#     color='#0044ff')


#PYDECK TEST
# scatterplot_layer = pdk.Layer(
#     'ScatterplotLayer',
#     data=df,
#     get_position='[LONG, LAT]',
#     get_color='[200, 30, 0, 160]',
#     get_radius=200,
#     pickable=True,
#     auto_highlight=True,
#     tooltip='CENTER_M',
# )


# Create a pydeck Deck
# deck = pdk.Deck(
#     map_style=None,
#     initial_view_state=pdk.ViewState(
#         latitude=14.650068,
#         longitude=121.102258,
#         zoom=13,
#         pitch=50,
#     ),
#     layers=[scatterplot_layer],
# )
#
# # Display the pydeck chart in Streamlit
# st.pydeck_chart(deck)
# FOLIUM ISSUE:
# map = folium.Map(location=[14.650068, 121.102258], zoom_start=16)
#
# for lt, ln, ev in zip(lat, long, evacuation_site):
#     folium.Marker(location=[lt, ln], popup=str(ev)).add_to(map)


# st_date = st_folium(map, width=800)


# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(df, columns=['LAT', 'LONG'])