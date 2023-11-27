import streamlit as st
import pandas as pd
import functions
from datab_reports import Reports, Inventory, Session, Base
from password_check import check_password

if check_password():
    st.header('Situation Report')

    all_reports = functions.get_reports()

    @st.cache_data()
    def add_report(evac_site, date, time, situation, population,
                   displaced, response, preparer, releaser, inventory_data):

        session = Session()

        date_str = str(date)
        time_str = str(time)

        new_report = Reports(evacuation_site=evac_site, date=date_str,
                             time=time_str, situation=situation,
                             affected_pop=population, displaced=displaced,
                             response=response, preparer=preparer,
                             releaser=releaser)

        # Link the new Reports entry to Inventory entries
        for item_data in inventory_data:
            is_available = item_data['is_available'].lower() == 'true'
            item = Inventory(
                item=item_data['item'],
                quantity=item_data['quantity'],
                is_available=is_available
            )
            new_report.inventory.append(item)


        session.add(new_report)
        session.commit()
        session.close()

    df = pd.read_csv('marikina_evacuation_centers.csv', usecols=['CENTER_M'])
    evac_sites_list = list(df["CENTER_M"])

    evacuation_site = st.selectbox('Select Evacuation Site', evac_sites_list)

    date = st.date_input("Add date", value=None)

    time = st.time_input('Add time', value=None)

    situation = st.text_input('Give an overview of the situation')

    affected_population = st.text_input('Describe the status of affected areas and population')

    displaced = st.text_input('Describe the status of displaced population')

    response = st.text_input('Describe reponse actions and interventions, i.e.'
                             ' standby funds, food and nonfood items, other activities')

    preparer = st.text_input('Prepared by')

    releaser = st.text_input('Released by')

    # # Table
    # Initialize empty DataFrame for the Inventory data
    inventory_data = pd.DataFrame(columns=["item", "quantity", "is_available"])

    # Display Inventory table using st.data_editor
    edited_inventory_df = st.data_editor(
        inventory_data,
        column_config={"inventory": st.column_config.ProgressColumn("inventory",
                                                                    help="Volume in tons",
                                                                    min_value=0,
                                                                    max_value=100),},
        num_rows="dynamic")

    st.write('Inventory List')


    on = st.toggle('Activate feature')

    if on:
        st.write('Feature activated!')

    if st.button("Save report"):

        # Retrieve user-modified Inventory data
        edited_inventory_data = edited_inventory_df.to_dict(orient="records")

        add_report(evacuation_site, date, time, situation, affected_population,
                   displaced, response, preparer, releaser, edited_inventory_data)
        # Convert the edited_df to SQLite and save it
        conn = st.connection("local_db", type="sql", url="sqlite:///reports.db")
        # cursor = conn.cursor()
        Session().commit()

        # Close the session
        Session().close()


        st.success("Report added successfully!")




 #DELETED
# # Create the table if it doesn't exist
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS all_reports (
#         evacuation_site TEXT,
#         date TEXT,
#         time TEXT,
#         situation TEXT,
#         affected_pop TEXT,
#         displaced TEXT,
#         response TEXT,
#         preparer TEXT,
#         releaser TEXT,
#         item TEXT,
#         quantity INTEGER,
#         is_available INTEGER,
#         inventory INTEGER
#     )
# """)
#
# # Clear existing data from the table
# cursor.execute("DELETE FROM all_reports")
#
# # Insert the values into the table
# for index, row in edited_df.iterrows():
#     cursor.execute("""
#         INSERT INTO all_reports (
#             evacuation_site, date, time, situation, affected_pop,
#             displaced, response, preparer, releaser, item, quantity,
#             is_available, inventory
#         ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """, (
#         evacuation_site, date, time, situation, affected_population,
#         displaced, response, preparer, releaser, row['item'],
#         row['quantity'], row['is_available'], row['inventory']
#     ))


# edited_df = st.data_editor(
#     initial_data,
#     column_config={
#         "inventory": st.column_config.ProgressColumn(
#             "Over or Under",
#             help="Volume in tons",
#             min_value=0,
#             max_value=100,
#         ),
#     }, num_rows="dynamic")


# edited_df = st.data_editor(df, num_rows="dynamic")
# edited_df = st.data_editor(
#     initial_data,
#     column_config={
#         "inventory": st.column_config.ProgressColumn(
#             "Over or Under",
#             help="Volume in tons",
#             min_value=0,
#             max_value=100,
#         ),
#     }, num_rows="dynamic")

# initial_data = pd.DataFrame(
#     [
#         {"item": "Rice", "quantity": 50, "is_available": True, "inventory": 0},
#         {"item": "Flour", "quantity": 25, "is_available": False, "inventory": 0},
#         {"item": "Sugar", "quantity": 70, "is_available": True, "inventory": 0},
#         {"item": "Powdered Milk", "quantity": 120, "is_available": True, "inventory": 0},
#         {"item": "Canned Goods", "quantity": 65, "is_available": True, "inventory": 0},
#         {"item": "Cooking Oil", "quantity": 70, "is_available": True, "inventory": 0},
#         {"item": "Blankets", "quantity": 54, "is_available": True, "inventory": 0},
#         {"item": "Clothing", "quantity": 140, "is_available": True, "inventory": 0},
#         {"item": "Tents", "quantity": 15, "is_available": True, "inventory": 0},
#         {"item": "Water", "quantity": 45, "is_available": True, "inventory": 0},
#         {"item": "Hygiene Kits", "quantity": 30, "is_available": True, "inventory": 0},
#     ]
# )
# conn = st.connection('reports', type='sqlite')


#


    # st.write(date, time, situation, affected_population, response)


# Display the updated data
# st.dataframe(edited_df)

# session = Session()
# reports = session.query(Reports).all()
#
# for report in reports:
#     st.write(f"Evacuation Site: {report.evacuation_site}")
#     st.write(f"Date: {report.date}")
#     st.write(f"Time: {report.time}")
#     st.write('I. Situation Overview')
#     st.write(f"{report.situation}")
#     st.write('II. Status of Affected Areas and Population')
#     st.write(f"{report.affected_pop}")
#     st.write('III. Status of Displaced Population')
#     st.write(f"{report.displaced}")
#     st.write('IV. Response Actions and Interventions')
#     st.write(f"{report.response}")
#     st.write(f"Prepared by: {report.preparer}")
#     st.write(f"Released by: {report.releaser}")
#
# session.close()
# st.write(pd.DataFrame(add_report()))
