

import streamlit as st
import pandas as pd
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTaUESVFbUnxC9q5-d-BiQXk6JD4r--bTZ3lNcryvfCeKqJq-tnz3VLhPwS_bZ5WXsRGYkOrtgkLlTU/pub?output=csv')
st.dataframe(voc)
l=voc.shape(voc)
i=hp.random.choice(range(l))
word_fr=voc['Definition'].values[i]
word_chi=voc['Pinyin'].values[i]
st.write(word_fr+" "+word_chi)
