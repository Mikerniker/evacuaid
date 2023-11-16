import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.title('EvacuAid Hub')

# st.subheader('Map of nearby evacuation centers')


st.header('Situation Report Overview')

# date = st.date_input("Add date", value=None)
# st.write('Date of Report:', date)
#
# time = st.time_input('Add time', value=None)
# st.write('Time:', time)
#
# st.write('I. Situation Overview')
# situation = st.text_input('Give a short description of the situation')
# st.write(situation)
#
# st.write('II. Status of Affected Areas and Population')
# affected_population = st.text_input('Describe the affected areas and population')
# st.write(affected_population)
#
# st.write('III. Status of Displaced Population')
# displaced = st.text_input('Describe displaced population')
# st.write(displaced)
#
# st.write('IV. Damaged Houses')
# housing = st.text_input('Describe housing conditions of those affected')
# st.write(housing)
#
# st.write('V. Cost of Humanitarian Assistance Provided')
# assistance = st.text_input('Describe allocation of assistance provided')
# st.write(assistance)
#
# st.write('VI. Response Actions and Interventions')
# response = st.text_input('Describe standby funds and prepositioned reliefe stockpile, food and nonfood items, other activities')
# st.write(response)

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