# README Poetry with LSTMs 

**Dataset:**
Open source [Poetry Foundation Dataset at Kaggle](https://www.kaggle.com/ultrajack/modern-renaissance-poetry), we relabel the dataset in terms of the gender of poets.

*Labels:*
- `M`: for *male*
- `F`: for *female*
- `T`: for *transgender*
- `NB`: for *non-binary*

**Preprocessing:**
The [preprocesing code](https://github.com/rogomes/AIWonderGirls-ATHENA-Art-Assistant/blob/main/LSTMs/data/creating-dataset.ipynb) generates a `.txt` file containing the poetry from a chosen topic (among the 73 available for the dataset). The notebook also generates visualizations on the text content in terms of most relevant keywords and ngrams.

**Modeling:**
`Long Short Term Memory (LSTM)` neural network [based on a notebook for generation scripts from *The Simpsons*](https://github.com/nehal96/Simpsons-Script-Generation).

**Next Steps:** 
- Finishing tagging the whole dataset
- Allowing for multiple genders per poet
- Generate more poetry samples for other topics
- Trying out other model architectures
