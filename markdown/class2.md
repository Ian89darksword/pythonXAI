## 🐍 Python 超簡單筆記

### 1️⃣ `print()` 印東西到畫面上

我們可以用 `print()` 把東西顯示出來，例如：

```python
print("Hello!")  # 印出 Hello!
```

---

### 2️⃣ `len()` 看東西有多長

```python
print(len("apple"))  # 看 "apple" 有幾個字母，答案是 5
print(len(","))      # 只有一個符號，答案是 1
```

---

### 3️⃣ `type()` 看東西是什麼種類（型態）

```python
print(type(1))         # 是整數 int
print(type(1.0))       # 是小數 float
print(type("apple"))   # 是文字 str
print(type(True))      # 是對錯 boolean（True 或 False）
```

---

### 4️⃣ 型態轉換（把一種資料變成另一種）

```python
print(int(1.0))        # 小數 → 整數
print(float(1))        # 整數 → 小數
print(str(1))          # 整數 → 字串
print(bool(1))         # 整數 → True 或 False（非0都是True）
print(int("1234"))     # 字串 → 整數
print(float("1.234"))  # 字串 → 小數
print(str(1.234))      # 小數 → 字串
```

❗ 注意：不是數字的字串不能轉換，會出錯喔！

---

### 5️⃣ `input()` 讓使用者輸入東西

```python
a = input("請輸入一個數字: ")
print(int(a) + 10)
```

📌 注意：用 `input()` 得到的都是字串，要加數字前要先轉成 int！

---

### 6️⃣ 計算圓面積和圓周長

```python
radius = float(input("請輸入半徑: "))
area = 3.14 * radius * radius
print(f"圓面積是: {area}")

circumference = 2 * 3.14 * radius
print(f"圓周長是: {circumference}")
```

---

### 7️⃣ Streamlit 顯示訊息（網頁用的）

```python
import streamlit as st

st.title("這是標題")
st.write("這是可以顯示各種東西的函數")
st.text("純文字")
st.markdown("* **粗體**\n* *斜體*")
st.info("提示訊息")
st.success("成功了！")
st.warning("小心！")
st.error("出錯了！")
```

---

### 8️⃣ 比較運算子（看看哪個大）

```python
print(1 == 1)   # 一樣嗎？True
print(1 != 1)   # 不一樣嗎？False
print(1 > 0)    # 大於嗎？True
print(1 < 0)    # 小於嗎？False
```

---

### 9️⃣ 邏輯運算子（判斷對錯）

```python
print(True and False)  # and：兩個都要True才會是True
print(not True)        # not：變相反（True變False）
```

---

### 🔟 運算順序（誰先算？）

| 順序 | 內容             |
| ---- | ---------------- |
| 1️⃣   | 括號 ()          |
| 2️⃣   | 次方 \*\*        |
| 3️⃣   | 除法 /           |
| 4️⃣   | 乘法 \*、取餘 %  |
| 5️⃣   | 加法 +、減法 -   |
| 6️⃣   | 比大小 > < == != |
| 7️⃣   | 邏輯 and or      |

---

### 1️⃣1️⃣ 字串的魔法

```python
print("apple" + "banana")  # 合起來變 applebanana
print("apple" * 3)         # 重複三次變 appleappleapple
```

---

### 1️⃣2️⃣ 密碼判斷 if...elif...else

```python
password = input("請輸入密碼: ")
if password == "1234":
    print("密碼正確")
elif password == "12345":
    print("你猜太多了！")
else:
    print("錯了")
```

---

### 1️⃣3️⃣ Streamlit 小考成績等級練習

```python
score = st.number_input("請輸入一個數字", min_value=0, max_value=100)

if score >= 90:
    st.write("A 級！")
elif score >= 80:
    st.write("B 級！")
elif score >= 70:
    st.write("C 級！")
elif score >= 60:
    st.write("D 級！")
else:
    st.write("沒過，加油！")
```
