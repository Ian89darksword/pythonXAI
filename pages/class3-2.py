import streamlit as st

st.write("### 按鈕練習")
# st.button()可以在網頁上顯示一個按鈕，當按鈕被點擊時，會返回True
# key是按鈕的識別名稱, 可以用來區分不同的按鈕
# 如果使用者點擊按鈕，則會返回True
st.button("按鈕1", key="button1")
if st.button("按鈕2", key="button2"):
    st.balloons()
if st.button("按鈕3", key="button3"):
    st.snow()
st.write("---")


st.write("### 數字金字塔")
num = st.number_input("請輸入數字 1-9", min_value=1, max_value=9, value=1)
for i in range(1, num + 1):
    st.write(f"{i}" * i)
