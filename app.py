
# Your Streamlit code here
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Assuming df_clean is already prepared in your environment

# Title of the app
st.title("Nicolas Cage Filmography Insights")

# Display dataset preview
st.write("Here is a preview of Nicolas Cage's cleaned filmography dataset:")
st.dataframe(df_clean.head())

# Add the rest of the code here...
