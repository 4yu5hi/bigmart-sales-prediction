import streamlit as st
import numpy as np
import pickle

st.title("Big Mart Sales Prediction")

# inputs
item_weight = st.number_input("Item Weight", value=10.0)
item_visibility = st.number_input("Item Visibility", value=0.05)
item_mrp = st.number_input("Item MRP", value=100.0)
outlet_year = st.number_input("Outlet Establishment Year", value=2000)

# load model
model = pickle.load(open("model.pkl", "rb"))

if st.button("Predict"):
    input_data = np.zeros(model.n_features_in_)
    
    # manually set important features
    input_data[0] = item_weight
    input_data[1] = item_visibility
    input_data[2] = item_mrp
    input_data[3] = outlet_year

    input_data = input_data.reshape(1, -1)

    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: {round(prediction[0],2)}")
