import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
import pydeck as pdk
from pretty_notification_box import notification_box
from datab_reports import Reports, Session, Inventory
from functions import read_inventory, search_inventory_by_site
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datab_reports import Reports, Inventory


#ORIGNAL
st.set_page_config(
    page_title="Evacuaid",
    page_icon="📦",
    layout="wide",
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


def read_active_sites():
    session = Session()
    try:
        # Read names of active evacuation sites
        active_sites = session.query(Reports.evacuation_site).filter(
            Reports.activate == True).all()
        return list(set(site[0] for site in active_sites))
    finally:
        session.close()


def search_active_inventory(site):
    selected_site = site

    session = Session()
    try:
        # Search inventory for the specified site if it is activated
        inventory_items = session.query(Inventory).join(Reports).filter(
            Reports.evacuation_site == selected_site,
            Reports.activate == True
        ).all()

        return inventory_items
    finally:
        session.close()

active_sites = read_active_sites()

st.write("## Sites needing aid")
for site in active_sites:
    active_inventory = search_active_inventory(site)
    if active_inventory:
        with st.expander(f"{site.title()} Inventory"):
            inventory_df = pd.DataFrame([
                {'Item': item.item.title(), 'Quantity': item.quantity}
                for item in active_inventory
            ])
            inventory_df["Inventory"] = inventory_df['Quantity']

            st.dataframe(inventory_df,
                         width=500,
                         height=420,
                         column_config={
                             "Inventory": st.column_config.ProgressColumn(
                                 "Inventory",
                                 help="Volume in tons",
                                 min_value=0,
                                 max_value=100)},
                         hide_index=True,
                         use_container_width=True
                         )

    else:
        st.warning(f"No item found with name '{site.title()}'.")

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


# Display inventory_items or use them as needed


# Assuming you have a valid engine created
# engine = create_engine("your_database_connection_string")
# Session = sessionmaker(bind=engine)

# def read_active_inventory():
#     session = Session()
#     try:
#         # Read inventory for activated reports
#         activated_sites = session.query(Reports.evacuation_site).filter(Reports.activate == True).all()
#         all_activated_sites = [site[0] for site in activated_sites]
#         return all_activated_sites
#     finally:
#         session.close()

# def search_inventory_by_site(site_name):
#     session = Session()
#     try:
#         # Search inventory for the specified site if it is activated
#         inventory_items = session.query(Inventory).join(Reports).filter(
#             Reports.evacuation_site == site_name,
#             Reports.activate == True
#         ).all()
#
#         return inventory_items
#     finally:
#         session.close()
