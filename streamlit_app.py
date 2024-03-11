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
  
  
input ="lapin"
list_possibilities=["rabbit","ratatouille","pig","rat"]
correct_answer="rabbit"
st.write("Traduis" + input)
for i in range (len(list_possibilities)):
  st.button(list_possibilities[i])

  
