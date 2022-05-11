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
selection = st.sidebar.selectbox("Go to page:", [ 'Home', 'About', 'Poetry', 'Painting Style', 'Feminist Animations', 'Contribute', 'Credits'])



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

elif selection == 'About':
        st.image('athena/images/athena.png')

        st.header("Empowering and inspiring artists through AI")
        st.write('This project started during the SAAI Factory hackathon in August 2021, with the AI Wonder Girls team.')
        st.image('athena/images/team.png')
        st.image(['athena/images/AIWG.png','athena/images/saai.png'])


elif selection == 'Poetry':
        st.image('athena/images/athena.png')

        st.header("ATHENA Poetry inspired by Female & Non-binary artists")
        st.write('About blablabla')
        st.write("Below you can ...")
        source = st.selectbox("Select data source:", ['LGBTQ', 'Race', 'Topic3', 'Topic4','Topic5', 'Topic6'])
  
        if source == 'LGBTQ':
            st.subheader("Wordcloud")
            st.markdown('The wordcloud shows the most common words present in the poems used as inspiration for ATHENA.')
            st.image('athena/poetry/words_lgbt.png', width=500)
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("#Prior word: Soul")
               # st.image('athena/poetry', width=300)
            with c2:
                st.markdown("**Prior word: Body**")
                #st.image('athena/poetry/.jpg', width=300)



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

        st.subheader('Betty Friedan')
        st.markdown('>*"You can show more of the reality of yourself instead of hiding behind a mask for fear of revealing too much."* - Betty Friedan')
        st.markdown('[Betty Friedan](), ')


        st.video('athena/animations/v1q1.mp4')

        st.subheader('Virginia Woolf')
        st.markdown('>*"There is no gate no lock no bolt that you can set upon the freedom of my mind together."* - Virginia Woolf')
        st.markdown('[Virginia Woolf](), ')
  
        st.video('athena/animations/v2q2.mp4')

        st.subheader('Eleanor Roosevelt')
        st.markdown('>*"Do not stop thinking of life as an adventure. You have no security unless you can live bravely, excitingly, imaginatively; unless you can choose a challenge instead of competence."* - Eleanor Roosevelt')
        st.markdown('[Eleanor Roosevelt](), ')

        st.video('athena/animations/v3q3.mp4')

elif selection == 'Contribute':
        st.image('athena/images/athena.png')

        st.header("Contribute to this Project")
        st.markdown('Get in contact')
        
        st.subheader("This application can be enhanced with ")
        st.write("* QnA NLP system for user to query any topic/solution.")



elif selection == 'Credits':
        st.image('athena/images/athena.png')

        st.image('athena/images/AIWG.png')
        st.subheader('Intended Audience:')
        st.write("The mitigation assistant application can be used by industry,policy makers, communities,and general public in adapting to the climate effects relevant to their sector and helps in climate mitigation solution planning implemetation" )
      
        st.subheader('Credits')
        st.markdown('**Music**')
        st.markdown('*Demised To Shield* by Ghostrifter Official | https://soundcloud.com/ghostrifter-official') 
        st.markdown('Music promoted by https://www.chosic.com/free-music/all/ Creative Commons CC BY-SA 3.0 https://creativecommons.org/licenses/by-sa/3.0/')
        st.markdown('*I have not fear* by Damiano Baldoni | https://soundcloud.com/damiano_baldoni')
        st.markdown('Music promoted by https://www.chosic.com/free-music/all/ Creative Commons CC BY 4.0 https://creativecommons.org/licenses/by/4.0/')
        st.markdown('*The Road Home* by Alexander Nakarada | https://www.serpentsoundstudios.com')
        st.markdown('Music promoted by https://www.chosic.com/free-music/all/ Creative Commons CC BY 4.0 https://creativecommons.org/licenses/by/4.0/')
        
        st.markdown('**Codes**')
        st.markdown('All code rights for generating video animations from images and mp3 music reserved to https://www.codespeedy.com/convert-audio-to-video-using-static-images-in-python/')
        st.markdown('All images in the animations were generated using Dalle-mini code from Hugging Face : https://github.com/borisdayma/dalle-mini')







