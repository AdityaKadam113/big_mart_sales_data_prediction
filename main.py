import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Big Mart Sales Prediction App")

# Input fields
Item_Identifier = st.number_input("Item Identifier", value=1000)
Item_Weight = st.number_input("Item Weight", value=12.5)
Item_Fat_Content = st.selectbox("Item Fat Content", [0, 1])
Item_Visibility = st.slider("Item Visibility", 0.0, 0.4, 0.1)
Item_Type = st.selectbox("Item Type", list(range(0, 17)))  # assuming it's label encoded
Item_MRP = st.number_input("Item MRP", value=100.0)
Outlet_Identifier = st.selectbox("Outlet Identifier", list(range(0, 10)))  # adjust range as needed
Outlet_Establishment_Year = st.selectbox("Outlet Establishment Year", [1985, 1987, 1997, 1999, 2002, 2004, 2007, 2009])
Outlet_Size = st.selectbox("Outlet Size", [0, 1, 2])  # encoded
Outlet_Location_Type = st.selectbox("Outlet Location Type", [0, 1, 2])
Outlet_Type = st.selectbox("Outlet Type", [0, 1, 2, 3])

# Collect input
input_data = np.array([[Item_Identifier, Item_Weight, Item_Fat_Content, Item_Visibility,
                        Item_Type, Item_MRP, Outlet_Identifier, Outlet_Establishment_Year,
                        Outlet_Size, Outlet_Location_Type, Outlet_Type]])

# Predict
if st.button('Predict Sales'):
    prediction = model.predict(input_data)
    st.success(f"Predicted Sales: ₹ {prediction[0]:.2f}")
