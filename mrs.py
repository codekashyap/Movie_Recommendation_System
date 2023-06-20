import streamlit as st
import pickle
import pandas as pd
import requests


def poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=9c30c559e45bdd17fed4d0db377f7d7f&language=en-US".format(movie_id)
    data = requests.get(url)
    data1 = data.json()
    poster_path = data1['poster_path']
    full_path = "https://image.tmdb.org/t/p/w342" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    # using enumerate to create tuple of similarity with index
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    l1 = []
    l2 = []
    for i in distances[1:6]:
        id = movies.iloc[i[0]].id
        l1.append(movies.iloc[i[0]].title)
        l2.append(poster(id))
    return l1,l2


movies_list = pickle.load(open('mrs.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movies_list)

# title for page
st.title("Movie Recommendation System")
# dropbox for movie
selected_movie = st.selectbox('Select Movie', movies['title'].values)

if st.button('Recommend'):
    st.write("The top 5 recommended movie for you are:")
    names, image = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(image[0])
    with col2:
        st.text(names[1])
        st.image(image[1])

    with col3:
        st.text(names[2])
        st.image(image[2])
    with col4:
        st.text(names[3])
        st.image(image[3])
    with col5:
        st.text(names[4])
        st.image(image[4])
