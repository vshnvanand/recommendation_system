import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiMainnahibataunga2DoHEmh2Z-wCp_02wW-g"
        }

    data = requests.get(url, headers=headers).json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




def recommend(movie):
    movies_list = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_list]
    movies_abc = sorted(list(enumerate(distances)),reverse=True,key = lambda x : x[1])[1:6]

    recommended = []
    recommended_poster = []
    for i in movies_abc:
        movie_id = movies.iloc[i[0]].movie_id
        recommended.append(movies.iloc[i[0]].title)
        
         # fetch post from api
        recommended_poster.append(fetch_poster(movie_id))
    return recommended , recommended_poster

movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System ')
movies_list = movies_list['title'].values

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies_list),
)

st.write("You selected:", selected_movie_name)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
        st.image(posters[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])

    with col3:
        st.header(names[2])
        st.image(posters[2])

    with col4:
        st.header(names[3])
        st.image(posters[3])
    
    with col5:
        st.header(names[4])
        st.image(posters[4])