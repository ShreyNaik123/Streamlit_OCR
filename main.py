import streamlit as st 
import pandas as pd
from io import StringIO
from gemini.Gemini import Gemini
from utils.showFile import show_file
import asyncio
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import seaborn as sns



model = Gemini()
model.init_chat(None)




st.header("_OCR Application using Gemini Api_ is :blue[cool] :sunglasses:")
uploaded_file = st.file_uploader("Choose a file")
show_file(uploaded_file)
if uploaded_file:
    if st.button("Send",type="primary"):
        with st.spinner("Analyzing image... ⏳"):
            generated_code = model.visual_yap(uploaded_file)
            # st.write(text)
            # st.subheader("Generated Code:")
            # st.code(generated_code, language="python")
            try:
                exec(generated_code)  # Execute in global scope
                # if not generated_code.startswith("import") or "st." not in generated_code:
                #     st.error("Generated code does not appear to be valid Streamlit code.")
                # else:
                #     exec(generated_code)  
            except SyntaxError as e:
                st.error(f"Syntax error in generated code: {e}")
            except Exception as e:
                st.error(f"Error executing code: {e}")
    
@st.dialog("Cast your vote")
def vote():
    st.write(f"Have your own api key?")
    apiKey = st.text_input("Gemini API Key")
    if st.button("Submit"):
        # st.session_state.vote = {"item": item, "reason": reason}
        # st.rerun()
        st.write(f"Sending api call to gemini with {apiKey}")
        model.init_chat(apiKey)

        

if st.button("Add API KEY", type="primary"):
    vote()
