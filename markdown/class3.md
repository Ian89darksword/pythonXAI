## 🐍 Python 入門小筆記（適合國小生）

### 🎯 1. 如果要做判斷，要用 `if`、`elif`、`else`

就像玩遊戲時，要看情況決定怎麼做，Python 也可以根據不同的情況，做不一樣的事情。

```python
if 條件1:
    做這件事
elif 條件2:
    換做另一件事
else:
    如果以上都不對，就做這個
```

🔍 小提醒：

- `if` 是先檢查一件事對不對。
- `elif` 是「如果剛剛的條件不對，那看看這個條件」。
- `else` 是「如果都不對，就做這個最後的」。

📌 如果你一直用 `if` 而不用 `elif`，Python 每一條都會檢查，比較慢喔～

---

### 🔁 2. `for` 迴圈：重複做某件事的魔法

有時候我們要讓電腦「重複做某件事」，這時候可以用 `for` 迴圈。

```python
for 變數 in 範圍:
    要做的事情
```

🔸 這裡的「範圍」通常會用 `range()` 來寫。

#### 🧮 range 的用法：

- `range(5)`：從 0 到 4（不包含 5）
- `range(1, 5)`：從 1 到 4
- `range(1, 10, 2)`：從 1 開始，每次跳 2，會得到 1, 3, 5, 7, 9

🧪 範例：

```python
for i in range(5):
    print(i)
    print("Hello")
```

---

### 🖱️ 3. 做出有按鈕的網頁 (用 Streamlit)

你可以讓 Python 做出「會互動」的小網頁，有按鈕、會冒愛心或下雪～
要先匯入 Streamlit：

```python
import streamlit as st
```

#### ✨ 按鈕練習：

```python
st.write("按鈕練習")
st.button("按鈕1", key="button1")

if st.button("按鈕2", key="button2"):
    st.balloons()  # 點按鈕2會冒愛心

if st.button("按鈕3", key="button3"):
    st.snow()  # 點按鈕3會下雪
```

---

### 🔢 4. 數字金字塔（會越來越高）

可以讓使用者輸入一個數字，然後印出像金字塔一樣的數字圖案！

```python
num = st.number_input("請輸入數字 1-9", min_value=1, max_value=9, value=1)

for i in range(1, num + 1):
    st.write(f"{i}" * i)
```

📌 比如輸入 4，就會印出：

```
1
22
333
4444
```

---

### 🎉 總結：

| 學到的東西                  | 用途                       |
| --------------------------- | -------------------------- |
| `if/elif/else`              | 根據不同情況做不同事情     |
| `for + range()`             | 讓電腦重複做事情           |
| `streamlit`                 | 做出有按鈕的互動網頁       |
| `st.balloons()` `st.snow()` | 讓網頁更好玩！             |
| `f"{i}" * i`                | 印出重複的數字（金字塔！） |

---
