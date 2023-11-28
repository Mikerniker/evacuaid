import streamlit as st
from datab_reports import Reports, Session
from password_check import check_password
from functions import read_inventory, search_inventory_by_site, \
    read_reports, search_report_by_site
import pandas as pd

# def read_reports():
#     session = Session()
#     all_reports = session.query(Reports).all()
#     session.close()
#     return all_reports
#
#
# def search_report_by_site(site):
#     session = Session()
#     check_site = site.title()
#     relevant_report = session.query(Reports).filter(Reports.evacuation_site == check_site).all()
#     session.close()
#     return relevant_report


if check_password():

    reports = read_reports()
    inventory = read_inventory()

    # Search functionality
    st.header('Search Report by Evacuation Site')
    search_name = st.text_input('Enter site name:', key='original_search').strip()

    if st.button('Search'):
        if search_name:
            found_report = search_report_by_site(search_name)
            found_inventory = search_inventory_by_site(search_name)
            if found_report:
                st.write(f'### {search_name.title()} Reports')
                st.write(f'Total Reports Found: {len(found_report)}')
                for index, report in enumerate(found_report):
                    with st.expander(f"Evacuation Site Report {index + 1}: {report.evacuation_site}"):
                        st.write(f"### Evacuation Site: {report.evacuation_site}")
                        st.write(f"Date: {report.date}")
                        st.write(f"Time: {report.time}")
                        st.write('### I. Situation Overview')
                        st.write(f"{report.situation}")
                        st.write('### II. Status of Affected Areas and Population')
                        st.write(f"{report.affected_pop}")
                        st.write('### III. Status of Displaced Population')
                        st.write(f"{report.displaced}")
                        st.write('### IV. Response Actions and Interventions')
                        st.write(f"{report.response}")
                        st.write(f"Prepared by: {report.preparer}")
                        st.write(f"Released by: {report.releaser}")
            else:
                st.warning(f"No available reports for '{search_name}'.")
            if found_inventory:
                st.write(f'### {search_name.title()} Inventory')
                with st.expander(f"{search_name.title()} Inventory"):
                    inventory_df = pd.DataFrame([
                        {'Item': item.item.title(), 'Quantity': item.quantity}
                        for item in found_inventory
                    ])
                    inventory_df["Inventory"] = inventory_df['Quantity']

                    st.dataframe(inventory_df,
                                 width=500,
                                 height=420,
                                 column_config={
                                     "Inventory": st.column_config.ProgressColumn(
                                         "Inventory",
                                         help="Volume in tons",
                                         min_value=0,
                                         max_value=100)},
                                 hide_index=True,
                                 use_container_width=True
                                 )

            else:
                st.warning(f"No inventory for '{search_name}'.")


    #DELETE
    # Display items in Streamlit for TESTING
# reports = read_items()
# st.write('## Items from Database')
# for item in reports:
#     st.write(
#         f"**ID:** {item.id}, **Name:** {item.evacuation_site}, **Description:** {item.situation}")

    # clear_search_button = st.button('Clear Search')
    # if st.button('Clear Search'):
    #     search_name = st.text_input('Enter site name:', key='updated_search')

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

    # session.close()

