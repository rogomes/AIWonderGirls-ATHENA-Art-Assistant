# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image

import style

st.title("Classic Paintings in Female Style: Style transfer outputs (user chooses an image to change and a style to apply")

img = st.sidebar.selectbox(
    'Select Image',
    ('content_1.jpg', 'content_2.jpg', 'content_3.jpg', 'content_4.jpg', 'content_5.jpg', 'content_6.jpg', 'content_7.jpg', 'content_8.jpg', 'content_9.jpg', 'content_10.jpg', 'content_11.jpg', 'content_12.jpg', 'content_13.jpg', 'content_14.jpg')
)

style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie','style_1.jpg','style_2.jpg','style_3.jpg','style_4.jpg','style_5.jpg','style_6.jpg','style_7.jpg','style_8.jpg','style_9.jpg','style_10.jpg','style_11.jpg','style_12.jpg','style_13.jpg','style_14.jpg')
)


model= "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img
output_image = "images/output-images/" + style_name + "-" + img

st.write('### Source image:')
image = Image.open(input_image)
st.image(image, width=400) # image: numpy array

clicked = st.button('Stylize')

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write('### Output image:')
    image = Image.open(output_image)
    st.image(image, width=400)

