import streamlit as st
import pandas as pd
from io import StringIO
from gemini.Gemini import Gemini
from utils.showFile import show_file
import asyncio
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import seaborn as sns

st.set_page_config(
    page_title="OCR Application",
    page_icon="📷",
    layout="centered"
)


st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton button {
        width: 100%;
        border-radius: 8px;
        font-weight: 500;
    }
    .upload-container {
        border: 2px dashed #4B56D2;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    h1 {
        color: #4B56D2;
        font-weight: 700;
    }
    .success-message {
        background-color: #D4EDDA;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


model = Gemini()
model.init_chat(None)

# App header with improved styling
st.markdown("<h1>📷 OCR Application using Gemini API</h1>", unsafe_allow_html=True)
st.markdown("""
<p>Upload any image containing text, and the Gemini API will extract and analyze the content.</p>
<p><small><em>(Psst... Try uploading an image without any text too!)</em></small></p>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose an image file", 
                                type=['png', 'jpg', 'jpeg'])
st.markdown("</div>", unsafe_allow_html=True)


if uploaded_file:
    show_file(uploaded_file)
    

    if 'processing' not in st.session_state:
        st.session_state.processing = False
    

    button_text = "Processing..." if st.session_state.processing else "Analyze Image"
    button_disabled = st.session_state.processing
    
    if st.button(button_text, disabled=button_disabled, type="primary"):

        st.session_state.processing = True
        
        
        try:
            with st.spinner("Analyzing image with Gemini... ⏳"):


                generated_code = model.visual_yap(uploaded_file)
                
                st.markdown("<div class='success-message'>✅ Analysis complete!</div>", 
                           unsafe_allow_html=True)
            
                try:
                    exec(generated_code)
                except SyntaxError as e:
                    st.error(f"Syntax error in generated code: {e}")
                except Exception as e:
                    st.error(f"Error executing code: {e}")
                
      
                
        
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
        
        finally:

            st.session_state.processing = False
else:

    st.info("👆 Upload an image to get started")


st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p>Made with ❤️ using Streamlit and Gemini API</p>
</div>
""", unsafe_allow_html=True)
