import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib


data= pd.read_csv('deploy_data.csv')

model = joblib.load('xgb_fraud_model.pkl')


st.image('pngwing.com (3).png', width = 600) 
st.markdown("<br>", unsafe_allow_html= True)

st.markdown("<h1 style = 'color: #0C2D57; text-align: center;  font-family: verdana'>FRAUD PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Project Done By Mmenim-Abasi Udoh</h4>", unsafe_allow_html = True)

st.markdown("<br>", unsafe_allow_html= True)
st.write('This project aims to develop a predictive model for detecting fraudulent activities within a financial institution. The goal is to accurately identify suspicious transactions or behaviors to mitigate financial losses and maintain the integrity of the institution operations.')


st.dataframe(data.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1), use_container_width= True)
st.markdown("<br>", unsafe_allow_html= True)

st.sidebar.image('Sidebarimage.png', caption = 'Dear Esteemed Merchant')

amt = st.sidebar.number_input('Amount To Be Withdrawn', data['amt'].min(), data['amt'].max())
dates = st.sidebar.date_input('Date Of Transaction')
times = st.sidebar.time_input('Time Of Transaction')
category = st.sidebar.selectbox('Category',data['category'].unique())
merchant = st.sidebar.selectbox('Merchant', data['merchant'].unique())
merch_long = st.sidebar.number_input('Current merchant Longitude')
merch_lat = st.sidebar.number_input('Current merchant Latitude')
state = st.sidebar.selectbox('Current State',data.state.unique())
gender = st.sidebar.selectbox('Gender', data.gender.unique())

from datetime import datetime
datetime_obj = datetime.combine(dates, times)

new_unix = int(datetime_obj.timestamp())

st.subheader('Input Variable', divider = True)
inp = pd.DataFrame()
inp['amt'] = [amt]
inp['category'] = [category]
inp['merchant'] = [merchant]
inp['merch_long'] = [merch_long]
inp['merch_lat'] = [merch_lat]
inp['state'] = [state]
inp['gender'] = [gender]
inp['new_unix'] = [new_unix]

st.dataframe(inp)
# ['amt', 'category', 'merchant', 'merch_long', 'merch_lat', 'state', 'gender', 'new_unix', 'is_fraud']

merc_enc = joblib.load('merchant_encoder.pkl')
cat_enc = joblib.load('category_encoder.pkl')
gen_enc = joblib.load('gender_encoder.pkl')
state_enc = joblib.load('state_encoder.pkl')
# job_enc = joblib.load('job_encoder.pkl')

inp['merchant'] = merc_enc.transform(inp['merchant'])
inp['category'] = cat_enc.transform(inp['category'])
inp['gender'] = gen_enc.transform(inp['gender'])
inp['state'] = state_enc.transform(inp['state'])


if st.button('Predict Transaction Type'):
    predicts = model.predict(inp)
    if predicts[0] == 0:
        st.success('Genuine Transaction')
    else:
        st.error('Fraudulent Transaction Detected')

