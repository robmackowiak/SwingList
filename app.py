import streamlit as st
import pandas as pd
import numpy as np
import utils

st.title('⛳ Driving Range Practice Scheduler')

clubs = st.multiselect(
    'Select clubs:',
    ['Driver', '3-Wood', '5-Wood','2 Iron','3 Iron','4 Iron','5 Iron','6 Iron','7 Iron','8 Iron','9 Iron','PW','GW','AW','SW'])

col1, col2 = st.columns(2)

with col1:
    st.subheader('Main Settings')
    number = st.slider("Select number of balls:", min_value=1, max_value=100, value=50, step=1)

    variability = st.radio("Select variability level:",
                    options=["Low", "Medium", "High"])
    
with col2:
    st.subheader('Optional Settings')
    speed_bool = st.checkbox("Include variable clubspeeds?")
    shot_type_bool = st.checkbox("Include variable shot types?")
    dl_bool = st.checkbox("Include differential learning? (ADVANCED)")

col1,col2,col3 = st.columns(3)
with col2:
    st.text("")
    produce_df = st.button("Create Range Schedule",use_container_width=True)

col1 = st.columns(1)

if produce_df == True:
    clubs_df = utils.create_golf_df(number,variability,speed_bool,clubs,shot_type_bool,dl_bool)
    st.dataframe(clubs_df,use_container_width=True)