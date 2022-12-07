 # Importing modules
import pickle # For loading model
import streamlit as st # For web app
import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


#page config
st.set_page_config(
    page_title="BALINEST|Rekomendasi Wisata",
    page_icon="https://code.iconify.design/2/2.2.1/iconify.min.js",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Loading data frame
rec_wisata = pickle.load(open('rec_wisata1.pkl','rb'))
wisata = rec_wisata.index

# Loading similarity file
similarity = pickle.load(open('similarity1.pkl','rb'))

# Main heading
st.image("images/logobalinest.png")
st.title('REKOMENDASI WISATA DI BALI')

test = st.text_input('Input keyword tempat wisata yang ingin Anda kunjungi :')

#def get_index_place_name(place_name):
    
def recommend(rec_wisata):
    index = rec_wisata[rec_wisata.place_name == rec_wisata]["index"].values[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_image = []
    recommended_place_name = []
    recommended_city = []
    recommended_description = []
    recommended_weekend = []
    recommended_weekday = []
    for i in distances[1:6]:
        recommended_image.append(rec_wisata.iloc[i[0]].image)
        recommended_place_name.append(rec_wisata.iloc[i[0]].place_name)
        recommended_city.append(rec_wisata.iloc[i[0]].city)
        recommended_description.append(rec_wisata.iloc[i[0]].description)
        recommended_weekend.append(rec_wisata.iloc[i[0]].weekend_price)
        recommended_weekday.append(rec_wisata.iloc[i[0]].weekday_price)

    return recommended_image, recommended_place_name, recommended_city, recommended_description, recommended_weekend, recommended_weekday


if st.button('Tampilkan Rekomendasi'):
    recommended_image, recommended_place_name, recommended_city, recommended_description, recommended_weekend, recommended_weekday = recommend(test)

    #display with the columns
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[0], width=200, caption=recommended_place_name[0])
        with col2:
            st.subheader(recommended_place_name[0])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[0])
            with st.expander("Deskripsi"):
                st.write(recommended_description[0])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[0])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[0])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[1], width=200, caption=recommended_place_name[1])
        with col2:
            st.subheader(recommended_place_name[1])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[1])
            with st.expander("Deskripsi"):
                st.write(recommended_description[1])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[1])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[1])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[2], width=200, caption=recommended_place_name[2])
        with col2:
            st.subheader(recommended_place_name[2])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[2])
            with st.expander("Deskripsi"):
                st.write(recommended_description[2])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[2])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[2])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[3], width=200, caption=recommended_place_name[3])
        with col2:
            st.subheader(recommended_place_name[3])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[3])
            with st.expander("Deskripsi"):
                st.write(recommended_description[3])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[3])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[3])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[4], width=200, caption=recommended_place_name[4])
        with col2:
            st.subheader(recommended_place_name[4])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[4])
            with st.expander("Deskripsi"):
                st.write(recommended_description[4])
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[4])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[4])