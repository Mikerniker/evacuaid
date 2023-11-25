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



