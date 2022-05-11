from pickletools import markobject
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
        st.header('Women & AI Art')
        st.write("Welcome to the ATHENA Art Assistant, the first AI-based art assistant that promotes the work of female (and minorities) artists. ")
        st.markdown("**ATHENA will introduce you to a whole new world of AI art based on the work of female artists.**")
        st.image('athena/images/front.png')
        st.image('athena/images/inspiration3.png')
        st.image('athena/images/functionalities.png', width= 150)

        st.subheader("Credits")
        st.image(['athena/images/AIWG.png','athena/images/saai.png'])

elif selection == 'About':
        st.image('athena/images/athena.png')

        st.header("Empowering and inspiring artists through AI")
        st.write('The goal of this project is to bring awareness about the gender gap in both the technology and arts fields.')
        st.image('athena/images/inspiration1.png')

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
            st.image('athena/poetry/words_lgbt.png', width=600)

            st.header('Prior Word')
            p1, p2, p3 = st.columns(3)

            with p1:
                
                st.header("Water")
                st.image('athena/poetry/lgbtq_water.png', width=300)
            with p2:
                st.header("Dream")
                st.image('athena/poetry/lgbtq_dream.png', width=300)

            with p3:
                st.header("Soul")
                st.image('athena/poetry/lgbtq_soul.png', width=300)


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

        st.header("Animated Feminist Quotes")
        st.markdown('ATHENA generates Animated Feminist Quotes to present an abstract representation of inspirational quotes from well known feminist writers.')
        
        st.markdown('The technology behind the images in the animations belongs to the field of *Natural Language Processing* and is able to represent a given text as an image.') 
        st.markdown('For building the animations with ATHENA, selected feminist quotes were processed in the [OpenAI DALLE model](https://openai.com/blog/dall-e/) which associates an image to the whole sentence.')
        st.markdown('Putting multiple generated images together in a video (with selected open source audio music), the quotes serve as an inspiration for the resulting animation.')


        st.subheader('Betty Friedan')
        st.markdown('>*"You can show more of the reality of yourself instead of hiding behind a mask for fear of revealing too much."* - Betty Friedan')
        st.markdown("""[Betty Friedan](https://en.wikipedia.org/wiki/Betty_Friedan) (February 4, 1921 - February 4, 2006), was an American feminist writer 
        and activist. A leading figure in the women's movement in the United States, her 1963 book The Feminine Mystique is often credited with sparking 
        the second wave of American feminism in the 20th century. In 1966, Friedan co-founded and was elected the first president of the 
        National Organization for Women (NOW), which aimed to bring women "into the mainstream of American society now [in] fully equal partnership with men". 
        In 1970, after stepping down as NOW's first president, Friedan organized the nationwide Women's Strike for Equality on August 26, 
        the 50th anniversary of the Nineteenth Amendment to the United States Constitution granting women the right to vote. The national 
        strike was successful beyond expectations in broadening the feminist movement; the march led by Friedan in New York City alone attracted 
        over 50,000 people. In 1971, Friedan joined other leading feminists to establish the National Women's Political Caucus. Friedan was 
        also a strong supporter of the proposed Equal Rights Amendment to the United States Constitution that passed the United States 
        House of Representatives (by a vote of 354-24) and Senate (84-8) following intense pressure by women's groups led by NOW in the early 1970s. 
        Following Congressional passage of the amendment, Friedan advocated for ratification of the amendment in the states and supported other 
        women's rights reforms: she founded the National Association for the Repeal of Abortion Laws but was later critical of the abortion-centered 
        positions of many liberal feminists. Regarded as an influential author and intellectual in the United States, Friedan remained active in 
        politics and advocacy until the late 1990s, authoring six books. As early as the 1960s Friedan was critical of polarized and extreme 
        factions of feminism that attacked groups such as men and homemakers. One of her later books, The Second Stage (1981), critiqued what 
        Friedan saw as the extremist excesses of some feminists.""")


        st.video('athena/animations/v1q1.mp4')

        st.subheader('Virginia Woolf')
        st.markdown('>*"There is no gate no lock no bolt that you can set upon the freedom of my mind together."* - Virginia Woolf')
        st.markdown("""[Virginia Woolf](https://en.wikipedia.org/wiki/Virginia_Woolf) (25 January 1882 - 28 March 1941) was an English writer, 
        considered one of the most important modernist 20th-century authors and a pioneer in the use of stream of consciousness as a narrative device. 
        Woolf was born into an affluent household in South Kensington, London, the seventh child of Julia Prinsep Jackson and Leslie Stephen in a 
        blended family of eight which included the modernist painter Vanessa Bell. She was home-schooled in English classics and Victorian 
        literature from a young age. From 1897 to 1901, she attended the Ladies' Department of King's College London, where she studied 
        classics and history and came into contact with early reformers of women's higher education and the women's rights movement. 
        Encouraged by her father, Woolf began writing professionally in 1900. After her father's death in 1904, the Stephen family moved 
        from Kensington to the more bohemian Bloomsbury, where, in conjunction with the brothers' intellectual friends, they formed the 
        artistic and literary Bloomsbury Group. In 1912, she married Leonard Woolf, and in 1917, the couple founded the Hogarth Press, 
        which published much of her work. They rented a home in Sussex and moved there permanently in 1940. 
        Woolf had romantic relationships with women, including Vita Sackville-West, who also published her books through Hogarth Press. 
        Both women's literature became inspired by their relationship, which lasted until Woolf's death. 
        During the inter-war period, Woolf was an important part of London's literary and artistic society. 
        In 1915, she had published her first novel, The Voyage Out, through her half-brother's publishing house, Gerald Duckworth and Company. 
        Her best-known works include the novels Mrs Dalloway (1925), To the Lighthouse (1927) and Orlando (1928). 
        She is also known for her essays, including A Room of One's Own (1929). 
        Woolf became one of the central subjects of the 1970s movement of feminist criticism and her works have since 
        attracted much attention and widespread commentary for "inspiring feminism". Her works have been translated into more than 50 languages. 
        A large body of literature is dedicated to her life and work, and she has been the subject of plays, novels and films. 
        Woolf is commemorated today by statues, societies dedicated to her work and a building at the University of London. 
        Throughout her life, Woolf was troubled by mental illness. She was institutionalised several times and attempted suicide 
        at least twice. According to Dalsimer (2004) her illness was characterised by symptoms that today would be diagnosed as 
        bipolar disorder, for which there was no effective intervention during her lifetime. 
        In 1941, at age 59, Woolf died by drowning herself in the River Ouse at Lewes.""")
  
        st.video('athena/animations/v2q2.mp4')

        st.subheader('Eleanor Roosevelt')
        st.markdown('>*"Do not stop thinking of life as an adventure. You have no security unless you can live bravely, excitingly, imaginatively; unless you can choose a challenge instead of competence."* - Eleanor Roosevelt')
        st.markdown("""[Eleanor Roosevelt](https://en.wikipedia.org/wiki/Eleanor_Roosevelt) (October 11, 1884 - November 7, 1962) was an American 
        political figure, diplomat, and activist. She served as the first lady of the United States from 1933 to 1945, during her husband 
        President Franklin D. Roosevelt's four terms in office, making her the longest-serving first lady of the United States.
        Roosevelt served as United States Delegate to the United Nations General Assembly from 1945 to 1952.
        President Harry S. Truman later called her the "First Lady of the World" in tribute to her human rights achievements. 
        Roosevelt was a member of the prominent American Roosevelt and Livingston families and a niece of President Theodore Roosevelt.
        She had an unhappy childhood, having suffered the deaths of both parents and one of her brothers at a young age. 
        At 15, she attended Allenswood Boarding Academy in London and was deeply influenced by its headmistress Marie Souvestre. 
        Returning to the U.S., she married her fifth cousin once removed, Franklin Delano Roosevelt, in 1905. 
        The Roosevelts' marriage was complicated from the beginning by Franklin's controlling mother, Sara, and after 
        Eleanor discovered her husband's affair with Lucy Mercer in 1918, she resolved to seek fulfillment in leading a public life of her own. 
        She persuaded Franklin to stay in politics after he was stricken with a paralytic illness in 1921, which cost him the normal use of his legs, 
        and began giving speeches and appearing at campaign events in his place. 
        Following Franklin's election as Governor of New York in 1928, and throughout the remainder of Franklin's public career in government, 
        Roosevelt regularly made public appearances on his behalf; and as First Lady, while her husband served as president, she significantly 
        reshaped and redefined the role. Though widely respected in her later years, Roosevelt was a controversial first lady at the time 
        for her outspokenness, particularly on civil rights for African-Americans. She was the first presidential spouse to hold regular 
        press conferences, write a daily newspaper column, write a monthly magazine column, host a weekly radio show, 
        and speak at a national party convention. On a few occasions, she publicly disagreed with her husband's policies. 
        She launched an experimental community at Arthurdale, West Virginia, for the families of unemployed miners, later widely regarded 
        as a failure. She advocated for expanded roles for women in the workplace, the civil rights of African Americans and Asian Americans, 
        and the rights of World War II refugees. Following her husband's death in 1945, Roosevelt remained active in politics for the 
        remaining 17 years of her life. She pressed the United States to join and support the United Nations and became its first delegate. 
        She served as the first chair of the UN Commission on Human Rights and oversaw the drafting of the Universal Declaration of Human Rights. 
        Later, she chaired the John F. Kennedy administration's Presidential Commission on the Status of Women. 
        By the time of her death, Roosevelt was regarded as "one of the most esteemed women in the world"; 
        The New York Times called her "the object of almost universal respect" in her obituary.
        In 1999, she was ranked ninth in the top ten of Gallup's List of Most Widely Admired People of the 20th Century, 
        and was listed thirteen times as the most admired woman between 1948 and 1961. """)

        st.video('athena/animations/v3q3.mp4')

elif selection == 'Contribute':
        st.image('athena/images/athena.png')

        st.header("Contribute to this Project")
        st.markdown('This project is intended to be maintained and expanded by the AI Wonder Girls team as an open source initiative.')
        st.markdown('Contributions on the form of open source data, implementation of new features, documentation and brainstorming on expansions are more than welcome :)')

        st.markdown('If you are an artist looking to promote your work, we will be happy to hear from you!')

        st.markdown('We are also looking for collaborations and partnerships with art institutions, research sponsors and initiatives seeking to promote the work of women in tech. ')

        st.subheader("Open Source Repository")
        st.markdown('*GitHub:* https://github.com/rogomes/AIWonderGirls-ATHENA-Art-Assistant')


        st.header("Get in contact")
        st.markdown('Interested in contributing? Then reach out via your favorite media:')

        st.image('athena/images/contact.png')

        


elif selection == 'Credits':
        st.image('athena/images/athena.png')

        st.markdown('This project is an open source product developed by the AI Wonder Girls team.')
        st.image('athena/images/AIWG.png')
        st.subheader('Intended Audience:')
        st.write("""The ATHENA Art assistant application can be used by a broad public ranging from artists and technology professionals to the 
        general public. Suggestions of use include (but not only):""")
        st.markdown('**Artists:** promote the work of female, transgender and non-binary artists through the general public, as well as provide art inspiration through artificial intelligence technology')
        st.markdown('**General Public:** get familiar with the work of female, transgender and non-binary artists while fostering curiosity and literacy on artificial intelligence technology.')
        st.markdown('**Technology Professional:** engage on a fascinating application of advanced AI techniques through an open source initiative lead by an all-women developers team.')

      
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







