import streamlit as st
import sys
import os

from src.recommendation_engine import recommend_restaurants


st.title("BiteFinder")
location = st.text_input("Enter City")
cuisine = st.text_input("Enter Cuisine")
rating = st.slider("Select Minimum Rating", 1.0, 5.0, 4.0)

if st.button("Find Restaurants"):
    recommendations = recommend_restaurants(location, cuisine, rating)
    st.write(recommendations)

# Define a function to clear inputs
def clear_inputs():
    st.session_state.location = ""
    st.session_state.cuisine = ""
    st.session_state.rating = 4.0

# "Clear" button
if st.button("Clear"):
    clear_inputs()

 
