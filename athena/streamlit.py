import streamlit as st
import altair as alt

import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import plotly.figure_factory as ff

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import warnings

warnings.filterwarnings( "ignore")

st.set_option('deprecation.showPyplotGlobalUse', False)
#st.set_page_config(layout="wide")  

#### Application starts
#st.sidebar.image('images/main.jpeg')
st.sidebar.write('Welcome to the ATHENA Art Assistant')
selection = st.sidebar.selectbox("Go to page:", [ 'Home', 'About', 'Poetry', 'Painting Style', 'Feminist Animations', 'Contribute', 'Further Scope & Credits'])



#st.title('ATHENA Art Assistant ')
if selection == 'Home':
        st.image('athena/images/athena.png')
        st.header('Climate Change Effects')
        st.write("blablabla")
        st.write("Place holder.")
        st.image('athena/images/front.png')
        st.image('athena/images/inspiration3.png')

        st.subheader("Credits")
        st.image('athena/images/AIWG.png')
        st.image('athena/images/saai.png')

elif selection == 'Painting Style':
        st.image('athena/images/athena.png')

        st.header("Female Painting Style")
        st.write('About blablabla')

        st.write("Below you can ...")
        source = st.selectbox("Select data source:", ['Mary Cassatt, Self Portrait', 'Painter2', 'Painter3', 'Painter4','Painter5', 'Painter6','Painter7', 'Painter8'])
        if source == 'Mary Cassatt, Self Portrait':
            st.markdown("*Original Style: [Self Portrait](https://npg.si.edu/object/npg_NPG.76.33), by Mary Cassatt")
            st.image('athena/style/style_2.jpg', width=300)
            col1, col2 = st.columns(2)

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_4.jpg", width=230 , caption='["Water Lilies and Japanese Bridge"](https://artmuseum.princeton.edu/collections/objects/31852), by Claude Monet')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s2c4.jpg", width=230)

           
elif selection == 'Feminist Animations':
        st.image('athena/images/athena.png')

        st.header("Feminist Quotes")
        st.write('About blablabla')
        st.markdown('>*"insert quote"*')

        st.video('athena/animations/v1q1.mp4')

elif selection == 'Contribute':
        st.image('athena/images/athena.png')

        st.header("Contribute to this Project")
        st.write('About blablabla')


elif selection == 'Further Scope & Credits':
        st.image('athena/images/athena.png')

        st.image('athena/images/AIWG.png')
        st.subheader('Intended Audience:')
        st.write("The mitigation assistant application can be used by industry,policy makers, communities,and general public in adapting to the climate effects relevant to their sector and helps in climate mitigation solution planning implemetation" )
        st.subheader("This application can be enhanced with ")
        st.write("* QnA NLP system for user to query any topic/solution.")
        st.write("* Adding more portals for climate study and solutions.")
        st.write("* Support industries/communities in implementation of solutions.")
        st.write("* Provide rating  for industries/policies on effeciency and impact of solutions.")
        st.write("* Motivate general public in raising awareness on climate solutions.")
        st.write("* Promote public, private partnerships  in implementation of climate solutions.")

        st.subheader("Credits:")
        st.write("* https://impactlab.org")
        st.write("* https://drawdown.org")
        st.write("* https://datahub.io/core/global-temp")
        st.write("* https://www.epa.gov/climate-indicators/climate-change-indicators-sea-level")
        st.write("* https://databank.worldbank.org/source/millennium-development-goals# ") 







