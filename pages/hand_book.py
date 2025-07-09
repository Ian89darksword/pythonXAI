import streamlit as st
import os

folderPath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderPath)  # 取的資料夾下的所有檔案
print(files)

files.sort()  # 將清單排序 , 預設是由小到大排序

for f in files:  # ['class1.md', 'class2.md'']逐一讀取所有 ,md檔案
    # markdown/class2.md
    with open(os.path.join(folderPath, f), "r", encoding="utf-8") as file:
        content = file.read()

    with st.expander(f[:-3]):
        st.write(content)  # 顯示內容
