import streamlit as st

def apply_ui_customizations():
    st.set_page_config(page_title="Sales Forecasting", layout="centered")
    
    custom_css = """
    <style>
        body {
            background: linear-gradient(to right, #e0eafc, #cfdef3);
            color: #000000;
        }
        .stApp {
            font-family: 'Segoe UI', sans-serif;
        }
        .css-18e3th9 {
            padding: 2rem;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.6em 1.2em;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 500;
        }
        .stRadio > div {
            background: white;
            padding: 0.8em;
            border-radius: 10px;
        }
        .stFileUploader {
            padding: 1em;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
