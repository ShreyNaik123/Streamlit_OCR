import streamlit as st 
import pandas as pd
from io import StringIO


st.header("_OCR Application using Gemini Api_ is :blue[cool] :sunglasses:")
uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)


@st.dialog("Cast your vote")
def vote():
    st.write(f"Have your own api key?")
    apiKey = st.text_input("Gemini API Key")
    if st.button("Submit"):
        # st.session_state.vote = {"item": item, "reason": reason}
        # st.rerun()
        st.write(f"Sending api call to gemini with {apiKey}")
        

if st.button("Add API KEY", type="primary"):
  vote()