import os
import streamlit as st
from multiapp import MultiApp
from PIL import  Image
from apps import home, movie, lstm, data, animation# import your app modules here

app = MultiApp()

# Title of the main page
col1, col2 = st.beta_columns(2)

original = Image.open('test.png')
#col1.header("Original")
col1.image(original, width = 700)
# Multi-Page App
# Add all your application here
app.add_app("Home ", home.app)
app.add_app("Movie Recommendation: ", movie.app)
app.add_app("AI-Poetry", lstm.app)
app.add_app("Classic Paintings in Female Style: ", data.app)
app.add_app("Feminist AI-Animation", animation.app)
# The main app
app.run()
