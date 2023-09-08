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
