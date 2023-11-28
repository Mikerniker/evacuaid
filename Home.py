import streamlit as st
import pandas as pd
from datab_reports import Reports, Session, Inventory
from PIL import Image


st.set_page_config(
    page_title="Evacuaid",
    page_icon="📦",
    layout="wide",
)


image = Image.open('evacuaid2.png')

st.image(image, width=900)


st.title('EvacuAid Hub')

st.header('Situation Report Overview')

def read_inventory():
    session = Session()
    all_inventory = session.query(Inventory).all()
    session.close()
    return all_inventory

def search_inventory_by_site(site):
    session = Session()
    check_site = site.title()
    relevant_inventory = session.query(Inventory).filter(Inventory.evacuation_site == check_site).all()
    session.close()
    return relevant_inventory

inventory = read_inventory()

search_name = st.text_input('Enter site name:', key='original_search').strip()

if st.button('Search'):
    if search_name:
        found_inventory = search_inventory_by_site(search_name)
        if found_inventory:
            st.write("## Sites needing aid")
            with st.expander(f"{search_name.title()} Inventory"):

                inventory_df = pd.DataFrame([
                    {'item': item.item.title(), 'quantity': item.quantity,
                     'is_available': item.is_available}
                    for item in found_inventory
                ])
                inventory_df["inventory"] = inventory_df['quantity']

                st.dataframe(inventory_df,
                             width=500,
                             height=420,
                             column_config={
                                 "inventory": st.column_config.ProgressColumn(
                                     "inventory",
                                     help="Volume in tons",
                                     min_value=0,
                                     max_value=100)},
                             )

        else:
            st.warning(f"No item found with name '{search_name}'.")

# PDF
# report_text = st.text_input("Report Text")
#
# export_as_pdf = st.button("Export Report")
#
#
# def create_download_link(val, filename):
#     b64 = base64.b64encode(val)  # val looks like b'...'
#     return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'
#
#
# if export_as_pdf:
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font('Arial', 'B', 16)
#     pdf.cell(40, 10, report_text)
#
#     html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
#
#     st.markdown(html, unsafe_allow_html=True)



