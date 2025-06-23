
from ui import apply_ui_customizations
apply_ui_customizations()

import streamlit as st
import pandas as pd
import joblib



# Load trained models and encoder
rf_model = joblib.load("model_rf.pkl")
xgb_model = joblib.load("model_xgb.pkl")

# App title
st.title("Sales Forecaste")

uploaded_file = st.file_uploader("Upload a CSV file for prediction", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file, encoding='cp1252')
    st.subheader("Uploaded Data")
    st.write(input_df.head())

    # === PREPROCESSING MATCHED TO TRAINING ===

    # Create 'Order_Month_Num'
    input_df["Order Date"] = pd.to_datetime(input_df["Order Date"])
    input_df["Order_Month_Num"] = input_df["Order Date"].dt.month

    # Profit Margin
    input_df["Profit_Margin"] = input_df["Profit"] / input_df["Sales"]

    # Fill NA just in case
    input_df.fillna(0, inplace=True)

    # One-hot encode (must match training)
    input_df_encoded = pd.get_dummies(input_df[[
        "Discount", "Quantity", "Profit", "Order_Month_Num", "Profit_Margin",
        "Category", "Region", "Segment"
    ]])

    # Align columns to training model
    model_features = rf_model.feature_names_in_
    for col in model_features:
        if col not in input_df_encoded.columns:
            input_df_encoded[col] = 0  # Add missing columns
    input_df_encoded = input_df_encoded[model_features]  # Ensure correct order

    # === Model Selection ===
    model_choice = st.radio("Choose model:", ("Random Forest", "XGBoost"))

    if st.button("Predict Sales"):
        preds = (
            rf_model.predict(input_df_encoded)
            if model_choice == "Random Forest"
            else xgb_model.predict(input_df_encoded)
        )
        input_df["Predicted Sales"] = preds
        st.subheader("Predicted Results")
        st.write(input_df[["Category", "Region", "Segment", "Predicted Sales"]])
        st.download_button("Download predictions", input_df.to_csv(index=False), "predictions.csv")
