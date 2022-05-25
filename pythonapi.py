
import streamlit as st
from PIL import Image

st.title(" Welcome to My Smallchat Application ".lstrip().upper())
images = Image.open("./app_icon.png")

st.image(images)
st.button("click Here", " Welcome Here ")

