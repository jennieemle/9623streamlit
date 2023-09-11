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

st.title("Making a Button")
result = st.button('click')
st.write(result)
if result:
    st.write('message : 버튼이 클릭되었습니다.')

st.button("Reset", type="primary")
if st.button('Hi'):
    st.write('message : 버튼을 클릭하셨습니다.')
else:
    st.write('clear')

result = st.button('버튼3')
if result:
    st.write('message : 버튼3이 클릭되었습니다.')

st.write("## text input")
title = st.text_input('종목코드')
st.write('현재 종목코드 : ', title)

st.write("## Simple Button")
result = st.button('simple_button')
if result:
    st.write('message : simple_button이 클릭되었습니다.')

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
