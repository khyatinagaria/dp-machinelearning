import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
st.title('😶‍🌫️ machine learning app')

st.info('This is app builds a machine learning model!')
with st.expander('Data'):
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  st.write('**x**')
  x_raw = df.drop('species',axis=1)
  x_raw
  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data visulaization'):
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')
