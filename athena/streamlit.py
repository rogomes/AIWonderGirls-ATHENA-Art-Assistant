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
        st.header('AI & Women Art')
        st.write("blablabla")
        st.write("Place holder.")
        st.image('athena/images/front.png')
        st.image('athena/images/inspiration3.png')

        st.subheader("Credits")
        st.image('athena/images/AIWG.png')
        st.image('athena/images/saai.png')

elif selection == 'Painting Style':
        st.image('athena/images/athena.png')

        st.header("Empowering and inspiring artists through AI")
        st.write('This project started during the SAAI Factory hackathon in August 2021, with the AI Wonder Girls team.')
        st.image('athena/images/team.png')
        st.image(['athena/images/AIWG.png','athena/images/saai.png'])


elif selection == 'Poetry':
        st.image('athena/images/athena.png')

        st.header("Female Painting Style")
        st.write('About blablabla')


elif selection == 'Painting Style':
        st.image('athena/images/athena.png')

        st.header("Female Painting Style")
        st.write('About blablabla')

        st.write("Below you can ...")
        source = st.selectbox("Select data source:", ['Mary Cassatt, Self Portrait', 'Painter2', 'Painter3', 'Painter4','Painter5', 'Painter6','Painter7', 'Painter8'])
        if source == 'Mary Cassatt, Self Portrait':
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[Self Portrait](https://npg.si.edu/object/npg_NPG.76.33), by Mary Cassatt")
                st.image('athena/style/style_2.jpg', width=300)
            with c2:
                st.markdown("""[Mary Cassatt](https://en.wikipedia.org/wiki/Mary_Cassatt), Mary Stevenson Cassatt (May 22, 1844 - June 14, 1926) 
                was an American painter and printmaker. She was born in Allegheny City, Pennsylvania (now part of Pittsburgh's North Side), 
                but lived much of her adult life in France where she befriended Edgar Degas and exhibited with the Impressionists. 
                Cassatt often created images of the social and private lives of women, with particular emphasis on the intimate bonds 
                between mothers and children. She was described by Gustave Geffroy as one of "les trois grandes dames" (the three great ladies) 
                of Impressionism alongside Marie Bracquemond and Berthe Morisot. In 1879, Diego Martelli compared her to Degas, 
                as they both sought to depict movement, light, and design in the most modern sense.""")
        
            
            col1, col2 = st.columns(2)

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_4.jpg", width=230)
                st.markdown('[*Water Lilies and Japanese Bridge*](https://artmuseum.princeton.edu/collections/objects/31852), by Claude Monet')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s2c4.jpg", width=230)

           
elif selection == 'Feminist Animations':
        st.image('athena/images/athena.png')

        st.header("Feminist Quotes")
        st.write('About blablabla')
        st.markdown('>*"You can show more of the reality of yourself instead of hiding behind a mask for fear of revealing too much."* - Betty Friedan')
        st.markdown('[Betty Friedan](), ')


        st.video('athena/animations/v1q1.mp4')

        st.markdown('>*"There is no gate no lock no bolt that you can set upon the freedom of my mind together."* - Virginia Woolf')
        st.markdown('[Virginia Woolf](), ')
  
        st.video('athena/animations/v2q2.mp4')


        st.markdown('>*"Do not stop thinking of life as an adventure. You have no security unless you can live bravely, excitingly, imaginatively; unless you can choose a challenge instead of competence."* - Eleanor Roosevelt')
        st.markdown('[Eleanor Roosevelt](), ')

        st.video('athena/animations/v3q3.mp4')



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







