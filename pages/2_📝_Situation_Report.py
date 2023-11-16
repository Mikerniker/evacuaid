import streamlit as st
import pandas as pd

st.header('Situation Report')

date = st.date_input("Add date", value=None)
st.write('Date of Report:', date)

time = st.time_input('Add time', value=None)
st.write('Time:', time)

st.write('I. Situation Overview')
situation = st.text_input('Give a short description of the situation')
st.write(situation)

st.write('II. Status of Affected Areas and Population')
affected_population = st.text_input('Describe the affected areas and population')
st.write(affected_population)

st.write('III. Status of Displaced Population')
displaced = st.text_input('Describe displaced population')
st.write(displaced)

st.write('IV. Damaged Houses')
housing = st.text_input('Describe housing conditions of those affected')
st.write(housing)

st.write('V. Cost of Humanitarian Assistance Provided')
assistance = st.text_input('Describe allocation of assistance provided')
st.write(assistance)

st.write('VI. Response Actions and Interventions')
response = st.text_input('Describe standby funds and prepositioned reliefe stockpile, food and nonfood items, other activities')
st.write(response)
