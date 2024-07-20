import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

df = pd.read_csv('/Users/ghanishtrajoria/Downloads/USvideos.csv')



print(df.head())
print(df.shape)

df = df.drop_duplicates()
print(df)

print(df.describe())
print(df.info())

Columns_to_remove = ['thumbnail_link','description']
df = df.drop(columns=Columns_to_remove)
print(df.info())


import datetime
df[ "trending_date"] = df["trending_date"]. apply(lambda x : datetime.datetime.strptime(x, '%y.%d.%m'))
print(df.head())

df['publish_time'] = pd.to_datetime(df['publish_time'])
print(df.head(2))

df['publish_month'] = df['publish_time'].dt.month
df['publish_day'] = df['publish_time'].dt.day
df['publish_hour'] = df['publish_time'].dt.month
print(df.head())

print (sorted(df["category_id"].unique()))
[1,2,10,15,17,19,20,222,23,24,25,26,27,28,29,30,43]

df['category_name'] = np.nan
df.loc[(df["category_id"] ==1),"category_name"] = 'flim and animation'
df.loc[(df["category_id"] ==2),"category_name"] = 'autos and vehicles'
df.loc[(df["category_id"] ==10),"category_name"] = 'music'
df.loc[(df["category_id"] ==15),"category_name"] = 'pets and animals'
df.loc[(df["category_id"] ==17),"category_name"] = 'sports'
df.loc[(df["category_id"] ==19),"category_name"] = 'travel and events'
df.loc[(df["category_id"] ==20),"category_name"] = 'gaming'
df.loc[(df["category_id"] ==22),"category_name"] = 'people and blogs'
df.loc[(df["category_id"] ==23),"category_name"] = 'comedy'
df.loc[(df["category_id"] ==24),"category_name"] = 'entertainment'
df.loc[(df["category_id"] ==25),"category_name"] = 'News and politics'
df.loc[(df["category_id"] ==26),"category_name"] = 'How to and style'
df.loc[(df["category_id"] ==27),"category_name"] = 'Education'
df.loc[(df["category_id"] ==28),"category_name"] = 'Science and technology'
df.loc[(df["category_id"] ==29),"category_name"] = 'Non profits and activism'
df.loc[(df["category_id"] ==30),"category_name"] = 'movies'
df.loc[(df["category_id"] ==43),"category_name"] = 'Shows'

df['year'] = df['publish_time'].dt.year
yearly_counts = df.groupby ('year')['video_id'].count()

#Create a bar Chart
yearly_counts.plot(kind='bar', xlabel='Year', ylabel='Total Publish Count', title='Total Publish Video Per Year')

#show the chart
plt.show()

#Group by year and sum the views for each year
yearly_views = df.groupby ('year')['views']. sum()
#Create a bar chart
yearly_views. plot(kind='bar', xlabel='Year', ylabel='Total views', title='Total Views per year')
plt.xticks(rotation=0)
plt. tight_layout()
#Show the bar chart
plt.show()


#Group the data oy category_name and calculate the sum of views in each category
category_views = df.groupby('category_name')['views'].sum().reset_index()

#Sort the categories by views in descending orden
top_categories = category_views.sort_values(by='views', ascending=False).head(5)

#create a bar plot to visualize the top 5 categories pIt. bar(top_categories['category_name'], top_categories[ 'views'])
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel ('Category Name', fontsize=12)
plt.ylabel('Total Views', fontsize=12)
plt.title('top 5 categories',fontsize=15)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='category_name', data=df, ordere=df['category_name'].value().index)
plt.xticks(rotation=90)
plt.title('video count by category')
plt.show()

#Count the number of videos published per hour
videos_per_hour = df['publish_hour'].value_counts().sort_index()

#create a bar plot
plt. figure(figsize=(12, 6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, palette='rocket')
plt. title( 'Number of Videos Published per Hour')
plt.xlabel('hour of day')
plt.ylabel('number of videos')
plt.xticks(rotation=45)
plt.show

#scatter ploy between 'Views' and 'likes'
sns.scatterptot(data=df, X= 'views', y='likes')
plt.title ('Views Vs Lakes')
plt.xlabel('views')
plt.ylabel('likes')
plt.show()

plt.figure(figsize=(14,8))
plt.subplots_adjust(wspace = 0.2, hspace = 0.4, top = 0.9)
plt.subplot(2,2,1)
g = sns.countplot(x='comments_disabled', data=df)
g.set_title("comment_disable", fontsize=16)
plt. subplot (2,2,2)
g1 =sns.countplot(x= 'rating disabled',data=df)
g1.set_title("rating_disable",fontsize=16)
plt.subplot(2,2,3)
g2 = sns.countplot(x='video_error_or_removed', data=df)
g2. set_title("Video Error or Removed", fontsize=16)
plt.show

