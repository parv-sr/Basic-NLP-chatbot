import pandas as pd
import sklearn as sk
from sklearn.feature_extraction.text import TfidfVectorizer as vec
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'C:\F DRIVE\Python\NLP Chatbot\intent_dataset.csv')
print(df)



intent_dict = df.groupby('Intent')['Text'].apply(list).to_dict()

text = df['Text']
print(text)
labels = df['Intent']

vectorizer = vec()
X = vectorizer.fit_transform(text)

le = LabelEncoder()
y = le.fit_transform(labels)
