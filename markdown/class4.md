---

# 🐍 Python + Streamlit 小學筆記 📘

## 🎨 標題與欄位（columns）

### ✅ 顯示標題

```python
st.title("欄位元件")
```

🔹 可以在網頁上顯示一個大大的標題。

### ✅ 欄位分成兩個或三個

```python
col1, col2 = st.columns(2)  # 分成兩欄
col1.button("按鈕1")        # 第一欄放一個按鈕
col2.button("按鈕2")        # 第二欄放一個按鈕
```

🔹 欄位可以想像成兩塊空間，我們可以在每一塊放不同東西，例如按鈕、文字。

### ✅ 調整欄位寬度

```python
col1, col2 = st.columns([1, 2])
```

🔹 `1, 2` 代表第一欄比較窄，第二欄比較寬。

---

## 🔘 按鈕 + 動作

### ✅ 點按鈕會有氣球

```python
if st.button("按我"):
    st.balloons()
```

🔹 點下去後會有小彩球飛出來，超可愛！

---

## 🔁 使用 for 迴圈製作很多按鈕

```python
cols = st.columns(4)  # 分成4欄
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i}")
```

🔹 一次做出很多個按鈕，每一個都放在不一樣的位置。

---

## 🧺 做一個簡單的「點餐機」

```python
if "order" not in st.session_state:
    st.session_state.order = []

food = st.text_input("請輸入食物")
if st.button("加入"):
    st.session_state.order.append(food)

for i in range(len(st.session_state.order)):
    st.write(st.session_state.order[i])
```

🔹 我們可以輸入食物名稱，然後按加入，就能把食物放進「購物籃」。

---

## ❌ 刪除點的東西

```python
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    col1.write(st.session_state.order[i])
    if col2.button("刪除", key=i):
        st.session_state.order.pop(i)
```

🔹 每個食物旁邊會有「刪除」按鈕，點下去就可以把它從購物籃中移除。

---

## 🧠 記住變數（Session State）

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("加 1"):
    st.session_state.ans1 += 1

st.write(f"答案是：{st.session_state.ans1}")
```

🔹 就像記在小本本裡，不會因為重新整理就忘記。

---

## ✍️ 文字輸入

```python
text = st.text_input("請輸入文字")
st.write(f"你輸入的是：{text}")
```

🔹 使用者可以打字，我們把他打的東西顯示出來。

---

## ➕ 數學運算小抄

```python
a += 1  # 等於 a = a + 1
a -= 1  # 減法
a *= 2  # 乘法
a /= 2  # 除法
a //= 2 # 整除
a %= 2  # 取餘數
a **= 2 # 次方
```

🔹 上面是各種加減乘除的簡寫方式。

---

## 🔄 迴圈與 break

### ✅ while 迴圈（重複做事）

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

🔹 一直重複到 `i` 變成 10。

### ✅ 用 break 停止

```python
while True:
    if 條件成立:
        break
```

---

## 🎲 隨機數字遊戲（猜數字）

```python
import random
ans = random.randint(1, 10)
```

🔹 `random` 可以讓電腦自己選一個隨機數字。

---

## 📚 字典 Dictionary

### ✅ 建立字典

```python
d = {"apple": 20, "banana": 30}
```

🔹 就像是水果的價錢表，一個 key 對應一個 value。

### ✅ 查詢價錢

```python
print(d["apple"])  # 會印出 20
```

### ✅ 加新水果

```python
d["orange"] = 25
```

### ✅ 刪除水果

```python
d.pop("apple")
```

### ✅ 一次印出所有

```python
for k, v in d.items():
    print(f"{k}:{v}")
```

🔹 印出所有的水果和它的價錢。

---

如果你覺得這樣整理還不錯，我也可以幫你整理成圖表版或小卡版本讓你背更輕鬆喔 😊
要不要我幫你做一版適合列印的小筆記本？
