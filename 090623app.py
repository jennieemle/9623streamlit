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
result = st.button('click 버튼1')
st.write(result)
if result:
    st.write('message : 버튼1이 클릭되었습니다.')

st.button("Reset", type="primary")
if st.button('Hi 버튼2'):
    st.write('message : 버튼2 클릭하셨습니다.')
else:
    st.write('clear')

result = st.button('버튼3')
if result:
    st.write('message : 버튼3이 클릭되었습니다.')

st.title("Simple Button")
result = st.button('simple_button')
if result:
    st.write('message : simple_button이 클릭되었습니다.')

st.title("Text input : st.text_input")
title = st.text_input('종목코드')
st.write('현재 종목코드는 ', title)
