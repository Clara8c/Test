import streamlit as st
name = st.text_input("Your name")
st.write ("Hello" + name)
import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

import streamlit as st
import pandas as pd
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/1jH6kJJISFA0Ye4gE4CzG7ZEjBJhCRelGOZN-HnxyZBQ/edit?usp=sharing')
st.dataframe(voc)
