

import streamlit as st
import pandas as pd
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/1jH6kJJISFA0Ye4gE4CzG7ZEjBJhCRelGOZN-HnxyZBQ/edit?usp=sharing')
st.dataframe(voc)
