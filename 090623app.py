import streamlit as st
view = [100, 150, 30]
st.write('## customer view')
st.write('## raw')
view
st.write('## bar chart')
st.bar_chart(view)
import pandas as pd
sview = pd.Series(view)
sview

st.write("## Simple Button")
result = st.button('simple_button')
if result:
    st.write('message : simple_button이 클릭되었습니다.')

st.write('## 종목코드')
title = st.text_input('종목코드')
st.write('현재 종목코드 : ', title)

st.write('## A Radio Button Widget')
genre = st.radio(
    '시간단위',
    [':rainbow[일봉]', '***주봉***', '월봉 :full_moon:'],
    captions = ['1일 주가를 하나의 막대기로 담은것', '1주일 주가를 하나의 막대기로 담은것', '1달 주가를 하나의 막대기로 담은것'])

if genre == ':rainbow[일봉]':
    st.write('You selected 일봉')
elif genre == '***주봉***':
    st.write('You selected 주봉')
else :
    st.write('You selected 월봉')
