import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(
page_title='Demo1'
)

st.title('Enter your inputs')

with open('df.pkl','rb') as file:
    df = pickle.load((file))

with open('final_model.pkl','rb') as file:
    pipeline = pickle.load((file))

property_type = st.selectbox('property_type',sorted(df['property_type'].unique().tolist()))

sector = st.selectbox('sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('bedrooms',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('bathroom',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('balcony',sorted(df['balcony'].unique().tolist()))

age_possession = st.selectbox('age_possession',['New Property', 'Relatively New', 'Old Property',
                                                'Moderately Old','Under Construction'])

super_built_up_area = st.number_input('super_built_up_area',min_value=0,value=100,step=50)

built_up_area = float(st.number_input('built_up_area',min_value=0,value=100,step=50))

carpet_area = float(st.number_input('carpet_area',min_value=0,value=100,step=50))

study_room = float(st.selectbox('study_room : [ 0 = No, 1 = Yes]',sorted(df['study room'].unique().tolist())))

servant_room = float(st.selectbox('servant_room : [ 0 = No, 1 = Yes]',sorted(df['servant room'].unique().tolist())))

furnishing_type = st.selectbox('furnishing_type',sorted(df['furnishing_type'].unique().tolist()))

luxury_cat = st.selectbox('luxury_level',sorted(df['luxury_cat'].unique().tolist()))

floorNum_cat = st.selectbox('floorNum',['low', 'medium', 'high'])

if st.button('predict'):
    data = [[property_type, sector, bedrooms, bathroom, balcony, age_possession,
            super_built_up_area, built_up_area, carpet_area, study_room, servant_room,
            furnishing_type, luxury_cat, floorNum_cat]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'super_built_up_area', 'built_up_area', 'carpet_area',
               'study room', 'servant room', 'furnishing_type', 'luxury_cat',
               'floorNum_cat']

    predict_df = pd.DataFrame(data,columns=columns)

    base_price = np.expm1(pipeline.predict(predict_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    st.text(f'flat/house price between {low:.2f} Cr and {high:.2f} Cr')