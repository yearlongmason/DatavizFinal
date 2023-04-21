import streamlit as st
from PIL import Image

st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide")
st.title("Harry Potter Script Analysis")
st.markdown('This is just some text writing a little bit about the project')

tab1, tab2, tab3, tab4 = st.tabs(["All 3", "1", "2", 3])

with tab1:
  image = Image.open('hpChart.png')
  st.image(image, caption='Fake Chart')
  
with tab2:
  image = Image.open('hpChart.png')
  st.image(image, caption='Fake Chart tab 2')
  
with tab3:
  image = Image.open('hpChart.png')
  st.image(image, caption='Fake Chart')
  
with tab4:
  image = Image.open('hpChart.png')
  st.image(image, caption='Fake Chart')
