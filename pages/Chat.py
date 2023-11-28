import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI
import pandas as pd



df = pd.read_csv('marikina_evacuation_centers.csv')

st.title("EvacuAid Assistant")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("How can I help you?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # # Display assistant response in chat message container
    # with st.chat_message("assistant"):
    #     message_placeholder = st.empty()
    #     full_response = ""

    # Process user query and extract information from the CSV file
    response_text = "I'm sorry, I couldn't find the information you requested."

    if "address" in prompt.lower():
        site_name = prompt.split("address of")[1].strip()
        site_info = df[df['CENTER_M'] == site_name, 'LOCATION']
        if not site_info.empty:
            response_text = f"The address of {site_name} is {site_info.LOCATION[0]}."

        elif "contact information" in prompt.lower() or "contact info" in prompt.lower():
            site_name = prompt.split("contact information of")[1].strip()
            site_info = df[df['CENTER_M'] == site_name]
            if not site_info.empty:
                response_text = f"The contact information of {site_name} is {site_info.CONTACT_NUMBER[0]}."

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response_text)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_text})



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
#             "Hi, can I help you with?",
#             "Do you need help?",
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