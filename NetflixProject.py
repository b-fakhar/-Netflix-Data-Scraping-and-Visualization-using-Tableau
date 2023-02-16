from bs4 import BeautifulSoup
import pandas as pd
import requests
import json
import re

#!pip install omdb 
import omdb
# Add your API key
omdb.set_default('apikey', 'XXXXXXXX')
# Add your user_agent
user_agent = 'XXXXXXXX'
HEADERS = {'User-Agent':user_agent , 'Accept-Language': 'en-US, en;q=0.5'}

from google.colab import drive
drive.mount('/content/drive')



def get_data(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a", attrs={'class':'nm-collections-title nm-collections-link'}) 
        data = []
        for link in links:
            href = link.get('href')
            response = requests.get(href, headers=HEADERS)
            if response.status_code == 200:
                soup2 = BeautifulSoup(response.content, "html.parser")
                parsed_data = json.loads(soup2.find("script").text)
                temp = {
                    'name': parsed_data.get("name"),
                    'date': parsed_data.get("dateCreated"),
                    'type': parsed_data.get("@type"),
                    'url': parsed_data.get("url"),
                    'rating': parsed_data.get("contentRating"),
                    'genres': [genre.text for genre in (soup2.find_all("a", attrs={"class":"more-details-item item-genres"}))],
                    'description': parsed_data.get("description")
                }
                data.append(temp)
        df = pd.DataFrame(data)
        duplicateRows = df[df.duplicated(['name'])]
        df = df.drop(duplicateRows.index.values.tolist())
        df = df.reset_index(drop=True)
        return df
    return None

# Movies
# Add the URL for your netflix profile movies for example: "https://www.netflix.com/browse/genre/XXXXX?so=su&order=popularity"
URL = "XXXX"
netflix_movies_df = get_data(URL)
netflix_movies_df

# Remove duplicate movies
duplicateRows_movie = netflix_movies_df[netflix_movies_df.duplicated(['name'])]
netflix_movies_df = netflix_movies_df.drop(duplicateRows_movie.index.values.tolist())
netflix_movies_df = netflix_movies_df.reset_index(drop=True)
netflix_movies_df.to_excel("netflix_movies_df.xlsx", index = False)
netflix_movies_df

# TV shows
# Add the URL for your netflix profile TV shows for example: "https://www.netflix.com/browse/genre/XXXXX?so=su&order=popularity"
URL = "XXXX"
netflix_tvshow_df = get_data(URL)

# Remove duplicate TV shows
duplicateRows_tvshow = netflix_tvshow_df[netflix_tvshow_df.duplicated(['name'])]
netflix_tvshow_df = netflix_tvshow_df.drop(duplicateRows_tvshow.index.values.tolist())
netflix_tvshow_df = netflix_tvshow_df.reset_index(drop=True)
netflix_tvshow_df.to_excel("netflix_tvshow_df.xlsx", index = False)
netflix_tvshow_df

# Concatenate movies and TV shows dataframes
dataset = pd.concat([netflix_movies_df, netflix_tvshow_df], axis=0) 
dataset = dataset.reset_index(drop=True)

# Get the IMDb rating for each title in dataset (if available)
data = []
for name in dataset['name']:
  movie = omdb.title(name)
  if movie:
    temp = {
              'name': name,
              'language':movie['language'], 
              'country':movie['country'],
              'awards':movie['awards'],
              'imdb_rating':movie['imdb_rating'],    
              'imdb_votes':movie['imdb_votes'], 
              'imdb_id':movie['imdb_id']                             
    }
    data.append(temp)
IMDB_rating_df = pd.DataFrame(data)

# Concatenate dataset dataframe and the IMDb rating dataframe
IMDB_rating_df = IMDB_rating_df.rename(columns={'name': 'drop_name'})
df = pd.concat([dataset, IMDB_rating_df], axis =1,join='inner')
df = df.drop('drop_name', axis=1)

# text preprocessing
def text_preprocessing(df,column_name):
  df[column_name] = df[column_name].astype(str)
  for idx in range(len(df[column_name])):
    df[column_name][idx] = re.sub(r'[\[\]\tt\'"]+', '', df[column_name][idx] )
  return df
text_preprocessing(df,'genres')
text_preprocessing(df,'imdb_id')

# Save the data in excel file
df.to_excel("netflix_ratings.xlsx", index=False)
