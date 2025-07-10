import streamlit as st

st.title("欄位元件")
(
    col1,
    col2,
) = st.columns(
    2
)  # 2columns
col1.button("按鈕1", key="btn1")  # co中建立一個按鈕類似st.button("按鈕1")
col1.button("按鈕2", key="btn2")  # co中建立一個按鈕類似st.button("按鈕2")

# 2columns, 可以用比例來設定每個column的寬度,將比例放到list中
(
    col1,
    col2,
) = st.columns(
    [1, 2]
)  # 2columns
col1.button("按鈕3", key="btn3")  # co中建立一個按鈕類似st.button("按鈕3")
col2.button("按鈕4", key="btn4")  # co中建立一個按鈕類似st.button("按鈕4")
# 3columns
col1, col2, col3 = st.columns([1, 2, 1])  # 3columns
col1.button("按鈕5", key="btn5")  # co中建立一個按鈕類似st.button("按鈕5")
col2.button("按鈕6", key="btn6")  # co中建立一個按鈕類似st.button("按鈕6")
col3.button("按鈕7", key="btn7")  # co中建立一個按鈕類似st.button("按鈕7")

col1, col2, col3 = st.columns([1, 2, 1])  # 3columns

col1, col2 = st.columns([1, 2])  # 2columns
with col1:
    st.write("這是col1")  # 在col1中寫入文字
    if st.button("按鈕8", key="btn8"):
        st.balloons()
with col2:
    st.write("這是col2")  # 在col2中寫入文字
    st.button("按鈕9", key="btn9")

# 多個columns
cols = st.columns(4)  # 4columns, cols[0]...cols[3]
for i in range(len(cols)):
    with cols[i]:
        st.button(f"for當中的按鈕{i+10}", key=f"{i+10}")  # 在每個col中建立一個按鈕

st.write("---")
st.title("columns排列元件效果比較")
(
    col1,
    col2,
) = st.columns(
    2
)  # 3columns
with col1:
    st.button("按鈕1", key="btn10")
    st.button("按鈕2", key="btn11")
    st.button("按鈕3", key="btn12")
with col2:
    st.button("按鈕4", key="btn13")
    st.button("按鈕5", key="btn14")
    st.button("按鈕6", key="btn15")

st.write("---")
# 開3個row, 2個columns
for i in range(3):
    col1, col2 = st.columns(2)  # 2columns
    with col1:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+4}")
    with col2:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+5}")

st.write("---")
st.title("文件輸入元件")
text = st.text_input("請輸入文字", key="text_input")
file = st.file_uploader("請選擇檔案", key="這是預設文字")
st.write(f"")

st.write("---")
st.title("session state")
ans = 1  # 設定一個變數ans=1
if st.button("接下去ans加1", key="ans"):
    ans = ans + 1
st.write(f"ans={ans}")

# session_state
if "ans" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("接下去ans加1", key="ans"):
    st.session_state.ans1 = st.session_state.ans1 + 1
st.write(f"ans={st.session_state.ans1}")

if st.button("重新整理畫面", key="banana"):
    st.rerun()
