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

result = st.button('버튼')
if result:
    st.write('message : 버튼이 클릭되었습니다.')
