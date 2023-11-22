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
    all_reports.append(date, time, situation, population, response)
    functions.write_reports(all_reports)
    return date, time, situation, population, response


# @st.cache_data()
# def get_data():
#     return []


date = st.date_input("Add date", value=None)

time = st.time_input('Add time', value=None)

st.write('I. Situation Overview')
situation = st.text_input('Give a short description of the situation',
                          on_change=add_report, key="new_report")

st.write('II. Status of Affected Areas and Population')
affected_population = st.text_input('Describe the affected areas and population')

st.write('III. Status of Displaced Population')
displaced = st.text_input('Describe displaced population')

# st.write('IV. Damaged Houses')
# housing = st.text_input('Describe housing conditions of those affected')
# # st.write(housing)
#
# st.write('V. Cost of Humanitarian Assistance Provided')
# assistance = st.text_input('Describe allocation of assistance provided')
# # st.write(assistance)

st.write('IV. Response Actions and Interventions')
response = st.text_input('Describe standby funds, food and nonfood items, other activities')

if st.button("Save report"):
    # get_data().append({"Date": date, "Time": time,
    #                    "Situation Overview": situation,
    #                    "Affected Population": affected_population,
    #                    "Actions and Interventions": response})
    add_report(date, time, situation, affected_population, response)
    st.write(date, time, situation, affected_population, response)

st.write(pd.DataFrame(add_report()))
