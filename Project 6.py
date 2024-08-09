import pandas as pd
data = pd.read_csv("/Users/ghanishtrajoria/Downloads/disney_plus_titles.csv")
print(data.info())
print(data.head(3))
print(data.columns.values)
print(data.isnall().sum())


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from texblob import textblob

data['release_year'] = pd.to_datetime(data['release_year'],format='%Y' errors= ='coerce')
data = data.dropna(subset=['release_year'])

plt.figure(figsize=(10,6))
releases_per_year.plot(kind='line')
plt.title('Number of release per year')
plt.xlabel('year')
plt.ylabel('number of Releases')
plt.grid(True)
print(plt.show())

def get_sentiment(text):
    blob = textblob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

data['sentiment'] = data['description'].apply(lambda x= get_sentiment(x)[0])
data['subjectivity'] = data['description'].apply(lambda x= get_sentiment(x)[1])


sns.histplot(data['sentiment'],kde =(True))
plt.title('sentiment polarity distribution')
plt.xlabel('sentiment polarity')
plt.ylabel('Frequency')
print(plt.show())

Vectorizer = TfidfVectorizer(stop_words='english')
X =Vectorizer.fit_transform(data['description'])

KMeans = KMeans(n_clusters=5, random_state=42)
data['cluster'] = KMeans.fit_predict(X)

pca =PCA(n_clusters=5, random_state=42)
X_pca = pca.fit_transform(X.toarray())

plt.scatter(X_pca[:,0], X_pca[:,1], c =data['cluster'],cmap='viridis')
plt.title('kMeans clustering of descriptions')
plt.xlabel('PCA component 1')
plt.ylabel('PCA component 2')
print(plt.show())

print(data.head())
print(data.columns)

data['release_year'] = data['release_year'].dt.year
selected_features = ['release_year', 'rating','cluster']
data_selected = ['selected_features'].dropna()
data_selected['reating'] = data_selected['rating'].astype('category').cat.codes

sns.pairplot(data_selected, hue='cluster',palette='viridis', diag_kind='kde')
plt.suptitle('pair plot of selected feature coloured by cluster', y=1.04)
print(plt.show)