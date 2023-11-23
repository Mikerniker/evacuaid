import streamlit as st
import pandas as pd
import functions

st.header('Situation Report')

all_reports = functions.get_reports()

@st.cache_data()
def add_report(date, time, situation, population,
               displaced, response, preparer, releaser):
    report = f"{date}, {time}, {situation}, " \
             f"{population}, {displaced}, {response}," \
             f" {preparer}, {releaser}\n"
    all_reports.append(report)
    functions.write_reports(all_reports)
    return report


date = st.date_input("Add date", value=None)

time = st.time_input('Add time', value=None)

situation = st.text_input('Give an overview of the situation')

affected_population = st.text_input('Describe the status of affected areas and population')

displaced = st.text_input('Describe the status of displaced population')

response = st.text_input('Describe reponse actions and interventions, i.e.'
                         ' standby funds, food and nonfood items, other activities')

preparer = st.text_input('Prepared by')

releaser = st.text_input('Released by')


if st.button("Save report"):
    add_report(date, time, situation, affected_population,
               displaced, response, preparer, releaser)
    # st.write(date, time, situation, affected_population, response)
    st.write(f"Date: {date}")
    st.write(f"Time: {time}")
    st.write('I. Situation Overview')
    st.write(f"{situation}")
    st.write('II. Status of Affected Areas and Population')
    st.write(f"{affected_population}")
    st.write('III. Status of Displaced Population')
    st.write(f"{displaced}")
    st.write('IV. Response Actions and Interventions')
    st.write(f"{response}")
    st.write(f"Prepared by: {preparer}")
    st.write(f"Released by: {releaser}")

# st.write(pd.DataFrame(add_report()))
