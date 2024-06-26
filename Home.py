#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:56:41 2024

Name: Home.py

@author: Team-12

Description: Front-end code for user interface. 

"""

import streamlit as st
from abstraction import AI_test_model, generate_video

#Page Configuration
st.set_page_config(
    page_title="Home - General Interpretation",
    page_icon="🌙",
    initial_sidebar_state="auto"
)
 

#Sidebar Initialization
st.sidebar.success("Select a page above.")

#Initialize top of web application.
st.title("🌙☁️Welcome to the Nocturnal Navigator ☁️🌙")

# User Manual
with st.expander("User Manual / Help Guide"):
    st.write("""
        Welcome to the Dream Interpreter! Here's how to use this application:

        1. **Enter Your Dream**: Start by typing a detailed description of your dream into the input box.
        2. **Acknowledge the Disclaimer**: Check the box to acknowledge that the interpretations provided are generated by AI and intended for entertainment purposes only.
        3. **Generate Interpretation**: Once you have entered your dream and acknowledged the disclaimer, click the 'Generate Dream Interpretation' button to see what your dream might mean.
        4. **View and Download**: After the interpretation is generated, you can view it directly on the page. If you wish to keep a copy, use the 'Download Your Dream Interpretation' button to save it as a text file.

        Enjoy exploring the meanings of your dreams!
    """)
    
# Disclaimer about Technology Used
st.markdown("""
**Powered by:** This application uses Gooey AI and Gemini AI technologies to analyze and generate dream interpretations.
""")

# Disclaimer about AI interpretation
st.markdown("""
**Disclaimer:** This interpretation is generated by AI and should be used for entertainment purposes only.
""")

user_input=st.text_input("Enter your dream here:")
st.write("Your dream description: \t\t"+ user_input)

#Generate User Dream Interpretation and display on app.
# Confirmation checkbox to proceed with the interpretation
if st.checkbox("I understand this is AI-generated and for entertainment only."):
    if st.button('Generate Dream Interpretation'):
        response = AI_test_model.generate_content("Please interpret the following dream: " + user_input)
        st.toast('Your dream was interpreted!', icon='🫡')
        st.write(response.text)
        #Option for user to download interpretation
        st.download_button(
        label="Download Your Dream Interpretation",
        data= response.text ,
        file_name="dream_interpretation.txt",
        mime="text/plain"
    )
        
else:
    st.write('Check the box above if you want to proceed with generating an interpretation.')
    
  






