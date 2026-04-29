import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Student Debt Dashboard", layout = 'wide')
st.title('Life After Graduation: The Impact of Student Debt on Earnings and Employment')
st.write('This dashboard explores student debt and post-graduation outcomes using college-level data.")

#Load data
df = pd.read_csv('Most-Recent-Cohorts-Institution_03232026.zip')

st.subheader('Dataset Preview')
st.dataframe(df.head())
st.subheader("Dataset Information")
st.write('Rows:", df.shape[0])
st.write("Columns:", df.shape[1])
st.subheader("Available Columns")
st.write(df.columns.tolist())
