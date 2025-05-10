import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer as vec
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'C:\F DRIVE\Python\NLP Chatbot\intent_dataset.csv')   #dataframe loaded

intent_dict = df.groupby('Intent')['Text'].apply(list).to_dict()        #dataframe sorted into a dictionary

text = df['Text']                                                       #text and labels stored
labels = df['Intent']

vectorizer = vec()
X = vectorizer.fit_transform(text)                                      #text is vectorised (converted to integers)

le = LabelEncoder()                                                     #labels are also vectorised
y = le.fit_transform(labels)

