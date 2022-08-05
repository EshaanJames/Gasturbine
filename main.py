import streamlit as st
import pandas as pd
import numpy as np

#Importing Files
import plots
import home
import predict


# Configuring  home page by setting its title and icon that will be displayed in a browser tab.


# Loading the dataset.
@st.cache(allow_output_mutation=True)
def load_data():
    # Load the Diabetes dataset into DataFrame.

    df = pd.read_csv('gt_full.csv')
    df = df.drop(columns = "Unnamed: 0")
    df.head()
    return df

hydraulics_df = load_data()

st.title('Gas Turbine Emission')
pages_dict = {"Home": home,
              "Predict Diabetes": predict,
              "Visualise Decision Tree": plots}

st.sidebar.title('Navigation')
user_choice = st.sidebar.radio('Go To', tuple(pages_dict.keys()))
selected_page = pages_dict[user_choice]
selected_page.app(hydraulics_df)


