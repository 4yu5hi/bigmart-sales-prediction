import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Big Mart Sales Prediction")

# Example inputs (you can expand later)
item_weight = st.number_input("Item Weight", value=10.0)
item_visibility = st.number_input("Item Visibility", value=0.05)
item_mrp = st.number_input("Item MRP", value=100.0)
outlet_year = st.number_input("Outlet Establishment Year", value=2000)

if st.button("Predict"):
    st.success("Prediction logic will go here")
