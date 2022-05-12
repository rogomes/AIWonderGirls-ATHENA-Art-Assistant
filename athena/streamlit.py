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
        st.image('athena/images/front.png', width= 350)

        st.markdown("**ATHENA employs advanced AI technologies to generate multiple forms of art. At the same time, the assistant also helps users to learn more about the work of minorities.**")
        st.markdown("""The application utilizes AI models trained on the work of female, non-binary and transgender artists.""")

        st.markdown('ATHENA create its own art work based on art pieces of female artists. As its initial prototype, ATHENA inspires users to create poems, change the style of pictures and visualize animations based on open source art work from female artists and/or feminist themes')
        st.markdown("""More funcionalities are already in development and soon will be available in the application. If you are interested in contributing to this project, check the **Contribute** page for more information. """)
        st.image('athena/images/functionalities.png', width= 800)
        
        st.markdown('The ATHENA Art Assistant project is one of the winners of the [SAAI Factory hackathon](https://saai-factory.com/) about Art and AI. As part of the prize, this project is currently on display in art exhibitions worldwide.')  
        
        url = 'https://www.youtube.com/watch?v=F4CJyS3ZBoc'
        st.video(url)
        st.markdown('Video exhibited at the [SAAI Factory Exhibition at Spazju Kreattiv (Malta)](https://www.kreattivita.org/en/event/saai-factory-exhibition-on-art-and-ai/).')
        
        st.markdown('The art works are built with open source resources (data and code) as a community effort from both the Arts and AI worlds.')

        st.subheader("Credits")
        st.image(['athena/images/AIWG.png','athena/images/saai.png'])

elif selection == 'About':
        st.image('athena/images/athena.png')

        st.header("Empowering and inspiring artists through AI")
        st.write('The goal of this project is to bring awareness about the gender gap in both the technology and arts fields.')
        st.image('athena/images/inspiration1.png')
        st.markdown('The ATHENA Art Assistant is named after the greek godess of knowledge, reason and handicraft, in order to honor and represent the union of Art and technology in this project.')

        st.markdown('This project started during the SAAI Factory hackathon in August 2021, with the [AI Wonder Girls](https://www.linkedin.com/company/80952123/) team. The AI Wonder Girls are an all-female team from all over the world contributing to open source social impact projects.')
        st.image('athena/images/team.png')

        st.markdown("""Visit this project's page at Devpost:""")
        st.markdown('https://devpost.com/software/athena-art-assistant')
        
        st.markdown("""Visit SAAI Factory's page for more exhibitions:""")
        st.markdown('https://saai-factory.com/')
        
        st.subheader('Intended Audience:')
        st.write("""The ATHENA Art assistant application can be used by a broad public ranging from artists and technology professionals to the 
        general public. Suggestions of use include (but not only):""")
        st.markdown('**Artists:** promote the work of female, transgender and non-binary artists through the general public, as well as provide art inspiration through artificial intelligence technology')
        st.markdown('**General Public:** get familiar with the work of female, transgender and non-binary artists while fostering curiosity and literacy on artificial intelligence technology.')
        st.markdown('**Technology Professional:** engage on a fascinating application of advanced AI techniques through an open source initiative lead by an all-women developers team.')


        st.image(['athena/images/AIWG.png','athena/images/saai.png'])


elif selection == 'Poetry':
        st.image('athena/images/athena.png')

        st.header("ATHENA Poetry inspired by Female & Non-binary artists")
        st.markdown('ATHENA applies [**Recurrent Neural Networks**](https://en.wikipedia.org/wiki/Recurrent_neural_network) to learn text patterns from poetry generated by female, non-binary and transgender artists.')
        st.markdown('The models learn from poetry data collected from the [Poetry Foundation](https://www.poetryfoundation.org) which are classified by topic.')
        st.markdown('An AI model for each topic is created and can generate ATHENA poetry for a given *Prime Word* (initial word in the poem) and length.')
        
        st.write("Below you can select the topics of poetry that you would like to see.")
        st.markdown('🚧 This module is under construction, so you may find new poetry in the future.')
        
        source = st.selectbox("Select data source:", ['LGBTQ'])
  
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

        st.markdown('ATHENA applies [*Style Transfer*](https://en.wikipedia.org/wiki/Neural_style_transfer) techniques to learn the style of an image and apply it to another one.')
        st.markdown('In this module of ATHENA, you can learn more about female artists work and see how their painting style changes the perspective of famous paintings.')
        st.markdown('🚧 This module is under construction, so you may find new poetry in the future.')
        st.write("Below you can select the artist you would like to see the style.")
        source = st.selectbox("Select data source:", ['Romaine Brooks, Self Portrait', 'Mary Cassatt, Self Portrait', 'Joan Mitchell, My Landscape II', 'Suzy Frelinghuysen, Composition - Toreador Drinking',"Georgia O'Keeffe, Manhattan", 'Lila Oliver Asher, Piano concerto'])
        if source == 'Romaine Brooks, Self Portrait':
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[Self Portrait]( https://womenshistory.si.edu/object/saam_1966.49.1), by Romaine Brooks")
                st.image('athena/style/style_1.jpg', width=300)
            with c2:
                st.markdown("""[Romaine Brooks](https://en.wikipedia.org/wiki/Romaine_Brooks) (born Beatrice Romaine Goddard; May 1, 
                1874 - December 7, 1970) was an American painter who worked mostly in Paris and Capri. 
                She specialized in portraiture and used a subdued tonal palette keyed to the color gray. 
                Brooks ignored contemporary artistic trends such as Cubism and Fauvism, drawing on her own original aesthetic inspired by the 
                works of Charles Conder, Walter Sickert, and James McNeill Whistler. Her subjects ranged from anonymous models to titled aristocrats. 
                She is best known for her images of women in androgynous or masculine dress, including her self-portrait of 1923, 
                which is her most widely reproduced work. Brooks had an unhappy childhood after her alcoholic father abandoned the family; 
                her mother was emotionally abusive and her brother mentally ill. By her own account, her childhood cast a shadow over her whole life. 
                She spent several years in Italy and France as a poor art student, then inherited a fortune upon her mother's death in 1902. 
                Wealth gave her the freedom to choose her own subjects. She often painted people close to her, 
                such as the Italian writer and politician Gabriele D'Annunzio, the Russian dancer Ida Rubinstein, and her partner of 
                more than 50 years, the writer Natalie Barney. Although she lived until 1970, it is erroneously believed that she painted very 
                little after 1925 despite evidence to the contrary. She made a series of drawings during the 1930s, using an 
                *unpremeditated* techniques predating automatic drawing. She spent time in New York City in the mid 1930s, 
                completing portraits of Carl Van Vechten and Muriel Draper. Many of her works are unaccounted for, 
                but photographic reproductions attest to her ongoing artwork. 
                It is thought to have culminated in her 1961 portrait of Duke Uberto Strozzi. (*source: Wikipedia*)""")
        
            
            col1, col2 = st.columns(2)

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_2.jpg", width=300)
                st.markdown('[*The Tooth Puller*](https://en.wikipedia.org/wiki/Paintings_attributed_to_Caravaggio), by Caravaggio')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s1c2.jpg", width=230)

        if source == 'Mary Cassatt, Self Portrait':
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[Self Portrait](https://npg.si.edu/object/npg_NPG.76.33), by Mary Cassatt")
                st.image('athena/style/style_2.jpg', width=250)
            with c2:
                st.markdown("""[Mary Cassatt](https://en.wikipedia.org/wiki/Mary_Cassatt), Mary Stevenson Cassatt (May 22, 1844 - June 14, 1926) 
                was an American painter and printmaker. She was born in Allegheny City, Pennsylvania (now part of Pittsburgh's North Side), 
                but lived much of her adult life in France where she befriended Edgar Degas and exhibited with the Impressionists. 
                Cassatt often created images of the social and private lives of women, with particular emphasis on the intimate bonds 
                between mothers and children. She was described by Gustave Geffroy as one of "les trois grandes dames" (the three great ladies) 
                of Impressionism alongside Marie Bracquemond and Berthe Morisot. In 1879, Diego Martelli compared her to Degas, 
                as they both sought to depict movement, light, and design in the most modern sense. (*source: Wikipedia*)""")
        
            
            col1, col2 = st.columns(2)

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_1.jpg", width=150)
                st.markdown('[*Monalisa*](https://en.wikipedia.org/wiki/Mona_Lisa), by Leonardo da Vinci')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s2c1.jpg", width=230)
                st.markdown('')

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_4.jpg", width=230)
                st.markdown('[*Water Lilies and Japanese Bridge*](https://artmuseum.princeton.edu/collections/objects/31852), by Claude Monet')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s2c4.jpg", width=230)

        if source == 'Joan Mitchell, My Landscape II':
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[My Landscape II](https://womenshistory.si.edu/object/saam_1980.137.82), by Joan Mitchell")
                st.image('athena/style/style_3.jpg', width=250)
            with c2:
                st.markdown("""[Joan Mitchell](https://en.wikipedia.org/wiki/Joan_Mitchell) (February 12, 1925 - October 30, 1992) was an American artist who 
                worked primarily in painting and printmaking, and also used pastel and made other works on paper. 
                She was an active participant in the New York School of artists in the 1950s. A native of Chicago, 
                she is associated with the American abstract expressionist movement, even though she lived in France for much of her career. 
                Mitchell's emotionally intense style and its gestural brushwork were influenced by nineteenth-century post-impressionist painters, 
                particularly Henri Matisse. Memories of landscapes inspired her compositions; she famously told art critic Irving Sandler, 
                "I carry my landscapes around with me." Her later work was informed and constrained by her declining health. 
                Mitchell was one of her era's few female painters to gain critical and public acclaim. Her paintings, drawings, 
                and editioned prints can be seen in major museums and collections around the world, and have sold for record-breaking prices. 
                In 2021, the San Francisco Museum of Modern Art and Baltimore Museum of Art co-organized a comprehensive retrospective of her work.
                In her will, Mitchell provided for the creation of the Joan Mitchell Foundation, a non-profit corporation that awards grants 
                and fellowships to working artists and maintains her archives. (*source: Wikipedia*)""")
        
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image("athena/style/content_6.jpg", width=230)
                st.markdown('[*Flaming_June*](https://en.wikipedia.org/wiki/Flaming_June), by Frederic Leighton')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s3c6.jpg", width=230)
                st.markdown('')

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_7.jpg", width=270)
                st.markdown('[*The Starry Night*](https://en.wikipedia.org/wiki/The_Starry_Night), by Vincent Van Gogh')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s3c7.jpg", width=230)

        if source == 'Suzy Frelinghuysen, Composition - Toreador Drinking': 
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[Composition - Toreador Drinking](https://womenshistory.si.edu/object/saam_1994.28), by Suzy Frelinghuysen")
                st.image('athena/style/style_4.jpg', width=250)
            with c2:
                st.markdown("""[Suzy Frelinghuysen](https://en.wikipedia.org/wiki/Suzy_Frelinghuysen) (May 7, 1911 - March 19, 1988), also known as **Suzy Morris**, was an American abstract painter and opera singer. (*source: Wikipedia*)""")
        
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image("athena/style/content_6.jpg", width=230)
                st.markdown('[*Flaming_June*](https://en.wikipedia.org/wiki/Flaming_June), by Frederic Leighton')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s4c6.jpg", width=230)
                st.markdown('')

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_7.jpg", width=270)
                st.markdown('[*The Starry Night*](https://en.wikipedia.org/wiki/The_Starry_Night), by Vincent Van Gogh')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s4c7.jpg", width=230)

        if source == 'Suzy Frelinghuysen, Composition - Toreador Drinking': 
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[Composition - Toreador Drinking](https://womenshistory.si.edu/object/saam_1994.28), by Suzy Frelinghuysen")
                st.image('athena/style/style_4.jpg', width=250)
            with c2:
                st.markdown("""[Suzy Frelinghuysen](https://en.wikipedia.org/wiki/Suzy_Frelinghuysen) (May 7, 1911 - March 19, 1988), also known as **Suzy Morris**, was an American abstract painter and opera singer. (*source: Wikipedia*)""")
        
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image("athena/style/content_6.jpg", width=230)
                st.markdown('[*Flaming_June*](https://en.wikipedia.org/wiki/Flaming_June), by Frederic Leighton')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s4c6.jpg", width=230)
                st.markdown('')

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_7.jpg", width=270)
                st.markdown('[*The Starry Night*](https://en.wikipedia.org/wiki/The_Starry_Night), by Vincent Van Gogh')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s4c7.jpg", width=230)


        if source == "Georgia O'Keeffe, Manhattan": 
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[Manhattan](https://womenshistory.si.edu/object/saam_1995.3.1), by Georgia O'Keeffe")
                st.image('athena/style/style_5.jpg', width=250)
            with c2:
                st.markdown("""[Georgia O'Keeffe](https://en.wikipedia.org/wiki/Georgia_O%27Keeffe) (November 15, 1887 - March 6, 1986) 
                was an American modernist artist. She was known for her paintings of enlarged flowers, New York skyscrapers, 
                and New Mexico landscapes. O'Keeffe has been called the "Mother of American modernism". In 1905, O'Keeffe began art training 
                at the School of the Art Institute of Chicago[3] and then the Art Students League of New York. 
                In 1908, unable to fund further education, she worked for two years as a commercial illustrator and then taught in Virginia, 
                Texas, and South Carolina between 1911 and 1918. She studied art in the summers between 1912 and 1914 and was introduced 
                to the principles and philosophies of Arthur Wesley Dow, who created works of art based upon personal style, design, 
                and interpretation of subjects, rather than trying to copy or represent them. This caused a major change in the way 
                she felt about and approached art, as seen in the beginning stages of her watercolors from her studies at the 
                University of Virginia and more dramatically in the charcoal drawings that she produced in 1915 that led to total abstraction. 
                Alfred Stieglitz, an art dealer and photographer, held an exhibit of her works in 1917. Over the next couple of years, 
                she taught and continued her studies at the Teachers College, Columbia University. 
                She moved to New York in 1918 at Stieglitz's request and began working seriously as an artist. 
                They developed a professional and personal relationship that led to their marriage in 1924. 
                O'Keeffe created many forms of abstract art, including close-ups of flowers, such as the Red Canna paintings, 
                that many found to represent vulvas, though O'Keeffe consistently denied that intention. 
                The imputation of the depiction of women's sexuality was also fueled by explicit and sensuous photographs of 
                O'Keeffe that Stieglitz had taken and exhibited. O'Keeffe and Stieglitz lived together in New York until 1929, 
                when O'Keeffe began spending part of the year in the Southwest, which served as inspiration for her paintings of New Mexico 
                landscapes and images of animal skulls, such as Cow's Skull: Red, White, and Blue and Ram's Head White Hollyhock and Little Hills. 
                After Stieglitz's death, she lived in New Mexico at Georgia O'Keeffe Home and Studio in 
                Abiquiú until the last years of her life, when she lived in Santa Fe. In 2014, O'Keeffe's 1932 painting 
                Jimson Weed/White Flower No. 1 sold for $44,405,000, more than three times the previous world auction record for any female artist.
                After her death, the Georgia O'Keeffe Museum was established in Santa Fe. (*source: Wikipedia*)""")
        
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image("athena/style/content_8.jpg", width=230)
                st.markdown('[*The Scream*](https://en.wikipedia.org/wiki/The_Scream), by Edvard Munch')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s5c8.jpg", width=270)
                st.markdown('')

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_13.jpg", width=270)
                st.markdown('[*Whistler Mother*](https://en.wikipedia.org/wiki/Whistler%27s_Mother), by James Abbott McNeill Whistler')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s5c13.jpg", width=270)

#style 7 Parting the Waters, from the portfolio Drawn to Stone, Ruth Weisberg https://womenshistory.si.edu/object/saam_1998.156.26
#style 8 Noble Numbers, Alice Baber, https://womenshistory.si.edu/object/saam_1965.20
#style 9 Beatrice wood, by Alice Matzkin https://womenshistory.si.edu/object/npg_S_NPG.94.127
#style 10 The Artist as a Young Woman, portfolio,    Carol Sutton https://womenshistory.si.edu/object/saam_1968.144.5
#style 11 Deuxieme Peril, from the portfolio Les 7 Perils Spectraux
#Dorothea Tanning https://womenshistory.si.edu/object/saam_1995.43.2
#Dorothea Tanning Second Peril (Deuxième péril) from The 7 Spectral Perils (Les 7 périls spectraux) 1950
#https://en.wikipedia.org/wiki/Dorothea_Tanning
#style 12 Quill-Leaf Tillandsia (Tillandsia fasciculata) Mary Vaux Walcott https://womenshistory.si.edu/object/saam_1970.355.736
#style 13 Quarry Spider Sheila Hicks https://womenshistory.si.edu/object/chndm_2006-13-7
#style 14 beds for dream Carmen Lomas Garza https://womenshistory.si.edu/object/hmsg_96.5

#content 1 https://en.wikipedia.org/wiki/Mona_Lisa Monalisa (Leonardo da Vinci)
#content 2 https://en.wikipedia.org/wiki/Paintings_attributed_to_Caravaggio (The Tooth Puller - Caravaggio)
#content 3 https://en.wikipedia.org/wiki/Dogs_Playing_Poker ( Cassius Marcellus Coolidge)
#content 4 Water Lilies and Japanese Bridge (claude Monet) 
#content 5 https://en.wikipedia.org/wiki/Self-Portrait_with_Thorn_Necklace_and_Hummingbird (Frida Kahlo)
#content 6 https://en.wikipedia.org/wiki/Flaming_June (	Frederic Leighton)
#content 7 https://en.wikipedia.org/wiki/The_Starry_Night (Vincent Van Gogh)
#content 8 https://en.wikipedia.org/wiki/The_Scream (	Edvard Munch)
#content 9 https://en.wikipedia.org/wiki/The_Kiss_(Klimt)  (Gustav Klimt) 
#content 10 https://en.wikipedia.org/wiki/Girl_with_a_Pearl_Earring Johannes Vermeer)
#content 11 https://en.wikipedia.org/wiki/The_Birth_of_Venus (Sandro Botticelli)
#content 12 https://en.wikipedia.org/wiki/The_Weeping_Woman (Pablo Picasso)
#content 13 https://en.wikipedia.org/wiki/Whistler%27s_Mother (r James Abbott McNeill Whistler)
#content 14 https://en.wikipedia.org/wiki/The_School_of_Athens (Raphael)


        if source == 'Lila Oliver Asher, Piano concerto': 
            st.header("Original Style")
            c1, c2 = st.columns(2)

            with c1:
                
                st.markdown("[Piano concerto](https://womenshistory.si.edu/object/saam_1998.59), by Lila Oliver Asher")
                st.image('athena/style/style_6.jpg', width=300)
            with c2:
                st.markdown("""[ Lila Oliver Asher](https://www.lilaoliverasher.com) was born in Philadelphia, Pa. She studied there with Joseph Grossman, Frank B.A. Linton and at the Fleischer Memorial Art School. She was also a pupil of Prof. Gonippo Raggi and held a four year scholarship to the now University of the Arts. She moved to Washington D.C. in 1946 and established a studio for painting, sculpture and prints. She taught art at the college level from 1947, as instructor in the Art Department of Howard University 1947-51, at Wilson Teachers College 1953-54, returning to Howard University in 1961, promoted to Assistant Professor in 1964, to Associate Professor in 1966, and to full Professor in 1971. She was named a Howard University Professor Emeritus upon her retirement from teaching in 1991, and continued to work in her studio producing works until her death in February 2021.(*source: https://www.lilaoliverasher.com/bio*)""")
        
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image("athena/style/content_5.jpg", width=230)
                st.markdown('[*Self Portrait_with_Thorn_Necklace_and_Hummingbird*](https://en.wikipedia.org/wiki/Self-Portrait_with_Thorn_Necklace_and_Hummingbird), by [Frida Kahlo](https://en.wikipedia.org/wiki/Frida_Kahlo)')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s6c5.jpg", width=300)
                st.markdown('')

            with col1:
                st.header("Original Image")
                st.image("athena/style/content_9.jpg", width=270)
                st.markdown('[*The Kiss*](https://en.wikipedia.org/wiki/The_Kiss_(Klimt)), by Gustav Klimt')

            with col2:
                st.header("Athena Generated")
                st.image("athena/style/s6c9.jpg", width=270)




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
        st.header('Credits')

        st.subheader('**Data**')
        st.markdown('*Poetry* was collected from the open source [Poetry Foundation](https://www.poetryfoundation.org/) dataset from Kaggle | https://www.kaggle.com/datasets/johnhallman/complete-poetryfoundationorg-dataset')
        st.markdown('*Paintings* were collected from the open source Smithsonian exhibitiion *Because of her Story*  | https://womenshistory.si.edu/')


        st.subheader('**Music**')
        st.markdown('All music in the animations is promoted by https://www.chosic.com/free-music/all/')

        st.markdown('- *Demised To Shield* by Ghostrifter Official | https://soundcloud.com/ghostrifter-official.   <br> Creative Commons CC BY-SA 3.0 https://creativecommons.org/licenses/by-sa/3.0/', unsafe_allow_html=True)
        
        st.markdown('- *I have not fear* by Damiano Baldoni | https://soundcloud.com/damiano_baldoni. <br> Creative Commons CC BY 4.0 https://creativecommons.org/licenses/by/4.0/', unsafe_allow_html=True)
        
        st.markdown('- *The Road Home* by Alexander Nakarada | https://www.serpentsoundstudios.com. <br> Creative Commons CC BY 4.0 https://creativecommons.org/licenses/by/4.0/' , unsafe_allow_html=True)
        
        st.subheader('**Code**')
        st.markdown('All images in the animations were generated using Dalle-mini code from Hugging Face : https://github.com/borisdayma/dalle-mini')
        st.markdown('This application is built with Streamlit | https://streamlit.io/')

        st.subheader('Other')
        st.markdown('All artists biographies displayed in this application were taken from Wikipedia | https://www.wikipedia.org')
        st.markdown('All code rights for generating video animations from images and mp3 music reserved to https://www.codespeedy.com/convert-audio-to-video-using-static-images-in-python')






