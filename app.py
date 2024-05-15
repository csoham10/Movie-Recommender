import pickle
import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3d53c73e9cd077f21af5dc0e84ea983c&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


#download movies_dict.pkl and similarity.pkl from google drive: https://drive.google.com/drive/folders/1mA3hC6ifX8z-MySU64uMt_Af-x_Du_YU?usp=sharing

st.header('Movie Recommendation System')
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown", movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.caption(recommended_movie_names[0])

    with col2:
        st.image(recommended_movie_posters[1])
        st.caption(recommended_movie_names[1])

    with col3:
        st.image(recommended_movie_posters[2])
        st.caption(recommended_movie_names[2])

    with col4:
        st.image(recommended_movie_posters[3])
        st.caption(recommended_movie_names[3])

    with col5:
        st.image(recommended_movie_posters[4])
        st.caption(recommended_movie_names[4])




