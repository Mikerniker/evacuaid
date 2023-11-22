import streamlit as st
import pandas as pd
import functions

st.header('Situation Report')

# st.set_page_config(layout="wide")


all_reports = functions.get_reports()  # to modify

@st.cache_data()
def add_report(date, time, situation, population, response):
    # report = st.session_state[] + "\n"
    # print(report)
    report = date, time, situation, population, response + "\n"
    all_reports.append(report)
    functions.write_reports(all_reports)
    return date, time, situation, population, response

date = st.date_input("Add date", value=None)

time = st.time_input('Add time', value=None)

st.write('I. Situation Overview')
situation = st.text_input('Give a short description of the situation')

st.write('II. Status of Affected Areas and Population')
affected_population = st.text_input('Describe the affected areas and population')

st.write('III. Status of Displaced Population')
displaced = st.text_input('Describe displaced population')

st.write('IV. Response Actions and Interventions')
response = st.text_input('Describe standby funds, food and nonfood items, other activities')

if st.button("Save report"):
    add_report(date, time, situation, affected_population, response)
    st.write(date, time, situation, affected_population, response)

# st.write(pd.DataFrame(add_report()))
