import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
from pandasql import sqldf

st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide")

image = Image.open('HogwartsLogo.png')#.resize((300, 175))
st.markdown('<p style="text-align:center;"><img src="image" alt="Logo"></p>', unsafe_allow_html=True)
#st.image(image)

mainCol1, mainCol2 = st.columns(2)

with mainCol1:
  st.title("Harry Potter Script Analysis")
  st.markdown('This is just some text writing a little bit about the project')
  
with mainCol2:
  st.markdown("<h3 style='text-align: right; color: #000000;'>Author: Mason Lee</h3>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["All 3 Movies", "Sorcerer's Stone", "Chamber of Secrets", "Prizoner of Azkaban"])

with tab1:
  st.title("Analysis of Harry Potter and the Sorcerer's Stone, Chamber of Secrets, and Prizoner of Azkaban")
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.image(image, caption='This will be a description of the chart')
  with col2:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
    fig, ax = plt.subplots()
    st.pyplot(fig)
  st.markdown('This is just some text at the end of each page saying something about the findings of this tab in particular')
  
with tab2:
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  with col2:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  
with tab3:
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  with col2:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  
with tab4:
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  with col2:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
