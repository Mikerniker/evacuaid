import streamlit as st
import pandas as pd
import datetime
import functions
from fpdf import FPDF
import base64
from datab_reports import Reports, Session


st.title('EvacuAid Hub')

# st.subheader('Map of nearby evacuation centers')

st.header('Situation Report Overview')


session = Session()
reports = session.query(Reports).all()

for report in reports:
    st.write(f"Evacuation Site: {report.evacuation_site}")
    st.write(f"Date: {report.date}")
    st.write(f"Time: {report.time}")
    st.write('I. Situation Overview')
    st.write(f"{report.situation}")
    st.write('II. Status of Affected Areas and Population')
    st.write(f"{report.affected_pop}")
    st.write('III. Status of Displaced Population')
    st.write(f"{report.displaced}")
    st.write('IV. Response Actions and Interventions')
    st.write(f"{report.response}")
    st.write(f"Prepared by: {report.preparer}")
    st.write(f"Released by: {report.releaser}")

session.close()

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



# Table
st.write('Inventory List')
quantities = [80, 25, 70, 120, 65, 70, 54, 140, 15, 45, 30]

df = pd.DataFrame(
    [
        {"Item": "Rice", "Quantity": 50, "is_available": True, "OverUnder": quantities[0]},
        {"Item": "Flour", "Quantity": 25, "is_available": False, "OverUnder": quantities[1]},
        {"Item": "Sugar", "Quantity": 70, "is_available": True, "OverUnder": quantities[2]},
        {"Item": "Powdered Milk", "Quantity": 120, "is_available": True, "OverUnder": quantities[3]},
        {"Item": "Canned Goods", "Quantity": 65, "is_available": True, "OverUnder": quantities[4]},
        {"Item": "Cooking Oil", "Quantity": 70, "is_available": True, "OverUnder": quantities[5]},
        {"Item": "Blankets", "Quantity": 54, "is_available": True, "OverUnder": quantities[6]},
        {"Item": "Clothing", "Quantity": 140, "is_available": True, "OverUnder": quantities[7]},
        {"Item": "Tents", "Quantity": 15, "is_available": True, "OverUnder": quantities[8]},
        {"Item": "Water", "Quantity": 45, "is_available": True, "OverUnder": quantities[9]},
        {"Item": "Hygiene Kits", "Quantity": 30, "is_available": True, "OverUnder": quantities[10]},
   ]
)

edited_df = st.data_editor(
    df,
    column_config={
        "OverUnder": st.column_config.ProgressColumn(
            "Over or Under",
            help="Volume in tons",
            min_value=0,
            max_value=100,
        ),
    }, num_rows="dynamic")


# edited_df = st.data_editor(df, num_rows="dynamic")

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')