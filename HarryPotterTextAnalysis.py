import streamlit as st
from PIL import Image

st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide")
st.title("Harry Potter Script Analysis")
st.markdown('This is just some text writing a little bit about the project')

tab1, tab2, tab3, tab4 = st.tabs(["All 3 Movies", "Sorcerer's Stone", "Chamber of Secrets", "Prizoner of Azkaban"])

with tab1:
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
