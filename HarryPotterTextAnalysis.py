import streamlit as st
from PIL import Image

st.set_page_config(page_title="Harry Potter Text Analysis", layout="wide")
st.title("Harry Potter Script Analysis")
st.markdown('This is just some text writing a little bit about the project')

testImage = "https://canvasjs.com/wp-content/uploads/images/gallery/javascript-charts/overview/javascript-charts-graphs-index-data-label.png"

image = Image.open(testImage)

st.image(image, caption='Fake Chart')
