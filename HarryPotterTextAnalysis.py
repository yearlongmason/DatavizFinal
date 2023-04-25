import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
from pandasql import sqldf
import base64

st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide") #Setting page title

#Displaying the HogwartsLogo.png at the top of the page
with open("HogwartsLogo.png", "rb") as file:
  contents = file.read()
  imgurl = base64.b64encode(contents).decode("utf-8")
st.markdown(f'<center><img src="data:image/gif;base64,{imgurl}" alt="Hogwarts Logo"></center>', unsafe_allow_html=True)



mainCol1, mainCol2 = st.columns(2)


#with mainCol1:
#  st.title("Harry Potter Script Analysis")
#  st.markdown('This is just some text writing a little bit about the project')
  
#with mainCol2:
#  st.markdown("<h3 style='text-align: center; color: #000000;'>Author: Mason Lee</h3>", unsafe_allow_html=True)
#  st.markdown("As a kid, I was always a huge fan of the Harry Potter movies. There was always something about the idea of magic, the worldbuilding, and the aesthetic that came with the movies that was something really enjoyable as a kid, and was something I never really stopped enjoying. With that in mind, I figured it could be fun to do some sort of an analysis on them. While looking for available data about the movies to analyze as a fun side project, I stumbled across this dataset that contained every line from the first three movies. What started as a fun project to work on in my freetime ended up turning into my final project for my data visualization class!")

st.markdown("<h3 style='text-align: center; color: #000000;'>An analysis of the first three Harry Potter movies by Mason Lee</h3>", unsafe_allow_html=True)
st.markdown("As a kid, I was always a big fan of the Harry Potter movies. There was always something about the idea of magic, the worldbuilding, and the aesthetic that came with the movies that was something really enjoyable as a kid, and was something I never really stopped enjoying. With that in mind, I figured it could be fun to do some sort of analysis on them. While looking for available data about the movies to analyze as a fun side project, I stumbled across this dataset that contained every line from the first three movies. What started as a fun project to work on in my freetime ended up turning into my final project for my data visualization class!")
tab1, tab2, tab3, tab4 = st.tabs(["First 3 Movies Combined", "Sorcerer's Stone", "Chamber of Secrets", "Prizoner of Azkaban"])

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
    #fig, ax = plt.subplots()
    #st.pyplot(fig)
    
    source = pd.DataFrame({'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]})
    chart = alt.Chart(source).mark_bar().encode(x='a', y='b')
    chart = chart.properties(width=700, height=375) #Set figure size
    chart = chart.configure_axis(labelFontSize=12, titleFontSize=16) #Set tick label size and axis title sizes
    chart = chart.configure_title(fontSize=20) #Sets title size
    chart = chart.configure_legend(titleColor='black', titleFontSize=14, labelFontSize=13) #Sets Legend attributes
    chart = chart.configure_view(strokeWidth=2) #Sets a border around the chart
    st.altair_chart(chart)
    
  st.markdown('This is just some text at the end of each page saying something about the findings of this tab in particular')
  
with tab2:
  st.title("Analysis of Harry Potter and the Sorcerer's Stone")
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  with col2:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  
with tab3:
  st.title("Analysis of Harry Potter and the Chamber of Secrets")
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  with col2:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  
with tab4:
  st.title("Analysis of Harry Potter and the Prizoner of Azkaban")
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
  with col2:
    image = Image.open('hpChart.png')
    st.image(image, caption='This will be a description of the chart')
