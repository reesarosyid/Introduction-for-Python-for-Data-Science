import streamlit as st
import requests

st.title("Aplikasi Pengecekan Penumpang Titanic")
pclass = st.selectbox("Passenger Class", [1,2,3])
fare = st.number_input('Fare')
age = st.number_input('Age')
sibsp = st.number_input('Sibling / Spouse')
parch = st.number_input('Parent / Children')
gender = st.selectbox("Gender", [0,1])

URL = "https://pyks10-deploy.herokuapp.com"
param = {'pclass':pclass,
        'sex':fare,
        'age':age,
        'sibsp':sibsp,
        'parch':parch,
        'fare':fare}

r = requests.get(URL, params=param)
res = r.json()
st.title(res['result'])