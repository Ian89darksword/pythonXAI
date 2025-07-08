import streamlit as st

st.write("## 練習")
score = st.number_input("請輸入一個數字", min_value=0, max_value=100, step=1)
if score >= 90:
    st.write("恭喜你，獲得了 A 級！")
elif score >= 80:
    st.write("恭喜你，獲得了 B 級！")
elif score >= 70:
    st.write("恭喜你，獲得了 C 級！")
elif score >= 60:
    st.write("恭喜你，獲得了 D 級！")
else:
    st.write("很抱歉，你沒有通過考試。請再接再厲！")
