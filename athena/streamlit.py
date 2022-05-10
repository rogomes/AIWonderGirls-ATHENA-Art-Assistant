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
#Function definitions
    

#### Application starts
#st.sidebar.image('images/main.jpeg')
st.sidebar.write('Welcome to the Climate Change Mitigation Assistant')
selection = st.sidebar.selectbox("Go to page:", [ 'Climate Change Effects', 'Further Scope & Credits'])



st.title('Climate Change Mitigation Assistant ')
if selection == 'Climate Change Effects':
       # st.image('images/cce1.jpeg')
        st.header('Climate Change Effects')
        st.write("Most scientists globally have agreed that human activities, especially those involving \
                  burning fossil fuels are causing an accelerated rise in the global temperature. \
                  The Intergovernmental Panel on Climate Change (IPCC), one of the most trustable source \
                  of climate change related research, released its newest report, the Sixth Assessment Report, \
                  in August 2021, containing some alarming details.")
        st.markdown('>*"Faster warming"*')
        st.markdown('>*"Climate change widespread, rapid, and intensifying"*')
        st.write("It is then of utmost important that efforts are performed to mitigate climate change effects. \
                 First, however, we need to understand the effects of climate change.")
        st.write("It is widely known that human activities especially \
                  the burning of fossil fuels have caused global warming \
                  that eventually causes climate change.")
        st.write("Global warming means rising global temperature, which causes \
                  a number of adverse effects.")
        st.write("This includes rising sea level, melting ice caps, and many more.")

        st.subheader("Rising Global Temperature")
        st.write("Below we can see the rising global temperature anomaly over time.")
        st.write("Global temperature anomaly data are sourced from NASA's GISS Surface Temperature \
                  (GISTEMP) analysis and the global component of Climate at a Glance (GCAG).")
        source = st.selectbox("Select data source:", ['GISTEMP', 'GCAG'])
        if source == 'GISTEMP':
            st.image('Rosana.jpg')

        st.subheader("Carbon Emissions by Country")
        st.write('Below is a bar chart race showing the top 10 countries that produce \
                  the highest total ' + 'CO{}'.format('\u2082') + ' emissions over the years.')
        st.video('carbon-emissions.mp4')


elif selection == 'Further Scope & Credits':
        st.image('images/AIWG.png')
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







