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

st.write("## Button")
st.button("Reset", type="primary")
if st.button('Hi'):
    st.write('message : 버튼을 클릭하셨습니다.')
else:
    st.write('clear')

st.write("## text input")
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


hide_streamlit_style = """
            <style>
            div div div div button {visibility: hidden;}
            button.styles_terminalButton__JBj5T {visibility: hidden;}
            .styles_terminalButton__JBj5T {display: none;}
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            #manage-app-button {visibility: hidden;}
            svg {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
