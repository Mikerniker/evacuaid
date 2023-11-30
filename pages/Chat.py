from openai import OpenAI
import streamlit as st
import pandas as pd
import random
import time
from datab_reports import Reports, Session, Inventory
from functions import search_inventory_by_site
from functions import search_active_inventory, read_active_sites


contact = 'Find a contact for an Evacuation Site'
evacuation_site = 'Find an Evacuation Site in need of aid'
inventory = 'Find the inventory of an active site'

active_sites = read_active_sites()
df = pd.read_csv('marikina_evacuation_centers.csv',
                  usecols=['CENTER_M', 'LAT', 'LONG', 'LOCATION',
                           'CONTACT_PERSON', 'CONTACT_NUMBER'])

# def find_active_site_inventory():
#     inventories = []
#     for site in active_sites:
#         active_inventory = search_active_inventory(site)
#         if active_inventory:
#             with st.expander(f"{site.title()} Inventory"):
#                 inventory_df = pd.DataFrame([
#                     {'Item': item.item.title(), 'Quantity': item.quantity}
#                     for item in active_inventory
#                 ])
#                 inventory_df["Inventory"] = inventory_df['Quantity']
#
#                 #ADD CONTCTS
#                 # st.write(f"**Address:** {location}")
#                 # st.write(f"**Contact Person:** {contact_person}")
#                 # st.write(f"**Contact Number:** {contact_number}")
#
#                 return st.dataframe(inventory_df,
#                              width=500,
#                              height=420,
#                              column_config={
#                                  "Inventory": st.column_config.ProgressColumn(
#                                      "Inventory",
#                                      help="Volume in tons",
#                                      min_value=0,
#                                      max_value=100)},
#                              hide_index=True,
#                              use_container_width=True
#                              )
#
#         else:
#             return st.warning(f"No item found with name '{site.title()}'.")

def find_active_site_inventory():
    inventories = []
    for site in active_sites:
        active_inventory = search_active_inventory(site)
        if active_inventory:
            inventory_df = pd.DataFrame([
                {'Item': item.item.title(), 'Quantity': item.quantity}
                for item in active_inventory
            ])
            inventory_df["Inventory"] = inventory_df['Quantity']
            inventories.append((site, inventory_df))
        else:
            st.warning(f"No item found with name '{site.title()}'.")

    return inventories



    # Find the corresponding row in the dataframe for the current active site
    # site_row = df[df['CENTER_M'] == site]  #ADDED
    #
    # location = site_row['LOCATION'].iloc[0]
    # contact_person = site_row['CONTACT_PERSON'].iloc[0]
    # contact_number = site_row['CONTACT_NUMBER'].iloc[0]



st.title("EvacuAid Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.chat_message("assistant"):
    st.write("Hello!")
    option = st.selectbox(
        'Which of the following can I help you with today?',
        ('',
         contact,
         evacuation_site,
         inventory,))


# React to user input
if prompt := option:
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = ""
    if option == contact:
        pass
    elif option == evacuation_site:
        response = "The sites currently looking for aid are:\n" +\
                   "\n".join([f"- {site}" for site in active_sites])
        with st.chat_message("assistant"):
            st.markdown(response)

    elif option == inventory:
        inventories = find_active_site_inventory()
        response = "These are the current inventories of active sites ⇩"
        with st.chat_message("assistant"):
            st.markdown(response)

        for site, inventory_df in inventories:
            with st.expander(f"{site.title()} Inventory"):
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
                             use_container_width=True)
    # else:
    #     response = "Please bear with me I am still learning."
    #     with st.chat_message("assistant"):
    #         st.markdown(response)

    # Display assistant response in chat message container
    # with st.chat_message("assistant"):
    #     st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


# session = Session()
# # conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with the actual database file
#
#
#
# df_evacuation_sites = pd.read_csv('marikina_evacuation_centers.csv')
# # df = pd.read_csv('marikina_evacuation_centers.csv')
#
# st.title("EvacuAid Assistant")
#
# # Load data from SQLite database
# # session = Session()
#
#
# def get_contact_info(evacuation_site):
#     contact_info = df_evacuation_sites.loc[df_evacuation_sites['evacuation_site'] == evacuation_site, 'contact_info'].values[0]
#     return f"The contact information for {evacuation_site} is: {contact_info}"
#
#
# def get_donation_items():
#     return f"We are currently accepting the following donation items:"
#
#
# def get_sites_needing_aid():
#     location_info = df_evacuation_sites['location_info'].unique()
#     return f"The locations of sites that need aid are: {', '.join(location_info)}"
#
#
# def get_active_sites():
#     try:
#         # Read names of active evacuation sites
#         active_sites = session.query(Reports.evacuation_site).filter(
#             Reports.activate == True).all()
#         return list(set(site[0] for site in active_sites))
#     finally:
#         session.close()
#
#
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
# # Accept user input
# if prompt := st.chat_input("Hello, how can I help you?"):
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#
#     # Process user input and provide assistant response
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#
#         # Process user input and generate assistant response
#         if any(keyword in prompt.lower() for keyword in ['location', 'contact', 'active sites']):
#             if 'location' in prompt.lower():
#                 response = get_contact_info("Marikina")  # Replace "Marikina" with extracted evacuation site
#             elif 'contact' in prompt.lower():
#                 response = get_contact_info("Marikina")  # Replace "Marikina" with extracted evacuation site
#             elif 'active sites' in prompt.lower():
#                 response = f"The active sites are: {', '.join(get_active_sites())}"
#         else:
#             response = "I'm sorry, I didn't understand your request. How can I assist you today?"
#
#         # Simulate stream of response with milliseconds delay
#         for chunk in response.split():
#             response += chunk + " "
#             time.sleep(0.05)
#             # Add a blinking cursor to simulate typing
#             message_placeholder.markdown(response + "▌")
#         message_placeholder.markdown(response)
#
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": response})




# ORIGINAL
# def search_inventory_by_site(site):

# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
# # Accept user input
# if prompt := st.chat_input("Hello, how can I help you?"):
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#
#     # Process user input and provide assistant response
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#
#         # Process user input and generate assistant response
#         if "contact information" in prompt.lower() and "evacuation site" in prompt.lower():
#             # Query contact information for evacuation site
#             # Assume you have a column 'contact_info' in your CSV for contact information
#             evacuation_site = "Marikina"  # You can extract the evacuation site from the user's input
#             contact_info = df_evacuation_sites.loc[df_evacuation_sites['evacuation_site'] == evacuation_site, 'contact_info'].values[0]
#             full_response = f"The contact information for {evacuation_site} is: {contact_info}"
#
#         elif "donation items" in prompt.lower():
#             # Provide information on donation items
#             # Assume you have a column 'donation_info' in your database for donation information
#             # donation_info = df_inventory['donation_info'].unique()  # You can customize this based on your database structure
#             # full_response = f"We are currently accepting the following donation items: {', '.join(donation_info)}"
#             full_response = f"We are currently accepting the following donation items:"
#
#         elif "locations of sites that need aid" in prompt.lower():
#             # Provide information on locations of sites that need aid
#             # Assume you have a column 'location_info' in your CSV for location information
#             location_info = df_evacuation_sites['location_info'].unique()  # You can customize this based on your CSV structure
#             full_response = f"The locations of sites that need aid are: {', '.join(location_info)}"
#
#         else:
#             full_response = "I'm sorry, I didn't understand your request. How can I assist you today?"
#
#         # Simulate stream of response with milliseconds delay
#         for chunk in full_response.split():
#             full_response += chunk + " "
#             time.sleep(0.05)
#             # Add a blinking cursor to simulate typing
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": full_response})








# Set OpenAI API key from Streamlit secrets
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
#
# # Accept user input
# if prompt := st.chat_input("How can I help you?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     response_text = "I'm sorry, I couldn't find the information you requested."
#
#     if "address" in prompt.lower():
#         site_name = prompt.split("address of")[1].strip()
#         site_info = df[df['CENTER_M'] == site_name, 'LOCATION']
#         if not site_info.empty:
#             response_text = f"The address of {site_name} is {site_info.LOCATION[0]}."
#
#         elif "contact information" in prompt.lower() or "contact info" in prompt.lower():
#             site_name = prompt.split("contact information of")[1].strip()
#             site_info = df[df['CENTER_M'] == site_name]
#             if not site_info.empty:
#                 response_text = f"The contact information of {site_name} is {site_info.CONTACT_NUMBER[0]}."
#
#         # Display assistant response in chat message container
#         with st.chat_message("assistant"):
#             st.markdown(response_text)
#
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": response_text})



# for response in client.chat.completions.create(
#         model=st.session_state["openai_model"],
#         messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#         stream=True,):
#     full_response += (response.choices[0].delta.content or "")
#     message_placeholder.markdown(full_response + "▌")
#     message_placeholder.markdown(full_response)
#
# st.session_state.messages.append({"role": "assistant", "content": full_response})

# ORIGINAL
# Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
# # Accept user input
# if prompt := st.chat_input("Hello, how can I help you?"):
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#
#
# # Display assistant response in chat message container
# with st.chat_message("assistant"):
#     message_placeholder = st.empty()
#     full_response = ""
#     assistant_response = random.choice(
#         [
#             "Hello! How can I assist you today?",
#             # "Hi, wecan I help you with?",
#             # "Do you need help?",
#         ]
#     )
#     # Simulate stream of response with milliseconds delay
#     for chunk in assistant_response.split():
#         full_response += chunk + " "
#         time.sleep(0.05)
#         # Add a blinking cursor to simulate typing
#         message_placeholder.markdown(full_response + "▌")
#     message_placeholder.markdown(full_response)
# # Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": full_response})