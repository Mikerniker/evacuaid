import streamlit as st
import pandas as pd
import functions
from datab_reports import Reports, Session

st.header('Situation Report')

all_reports = functions.get_reports()

@st.cache_data()
def add_report(date, time, situation, population,
               displaced, response, preparer, releaser):
    # report = f"{date}, {time}, {situation}, " \
    #          f"{population}, {displaced}, {response}," \
    #          f" {preparer}, {releaser}\n"

    session = Session()

    date_str = str(date)
    time_str = str(time)

    new_report = Reports(date=date_str, time=time_str, situation=situation,
                         affected_pop=population, displaced=displaced,
                         response=response, preparer=preparer,
                         releaser=releaser)
    session.add(new_report)
    session.commit()
    session.close()
    # all_reports.append(report)
    # functions.write_reports(all_reports)
    # return report


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
    st.success("Report added successfully!")
    # st.write(date, time, situation, affected_population, response)


session = Session()
reports = session.query(Reports).all()

for report in reports:
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
# st.write(pd.DataFrame(add_report()))
