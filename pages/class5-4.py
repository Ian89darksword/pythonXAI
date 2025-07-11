import streamlit as st

st.chat_message("user").write(" 這是使用者的訊息")
st.chat_message("assistant").write(" 這是AI的訊息")

history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "哈囉哈囉"},
    {"role": "user", "content": "我是你的小弟弟"},
    {"role": "assistant", "content": "我是你的小弟弟"},
    {
        "role": "assistant",
        "content": "我是你的小弟弟",
    },
]

for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👩‍💻").write(message["content"])
    else:
        st.chat_message("assistant", avatar="👨").write(message["content"])
