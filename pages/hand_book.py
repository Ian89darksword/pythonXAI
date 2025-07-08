import streamlit as st

with st.expander("class1的筆記"):
    st.write(
        """
## 🐍 Python 入門筆記

### ✅ 1. 印出東西到螢幕上

```python
print("hello world")
```

- `print()` 是把東西顯示在畫面上的指令。
- 就像把心裡想說的話「講」出來一樣！

---

### 🔢 2. 基本的資料種類（我們叫它「型態」）

這些是電腦能理解的幾種「東西」：

| 資料    | 說明                 | 範例             |
| ------- | -------------------- | ---------------- |
| `int`   | 整數（沒有小數點）   | 1, 2, -5         |
| `float` | 浮點數（有小數點）   | 1.0, 3.14, 0.5   |
| `str`   | 字串（像是字或句子） | "apple", "hello" |
| `bool`  | 布林值（真假）       | `True`, `False`  |

📌 範例：

```python
print(1)         # 整數
print(1.234)     # 小數
print("apple")   # 文字
print(True)      # 真
print(False)     # 假
```

---

### 📦 3. 變數（就像放東西的箱子）

你可以把東西放進變數裡，然後再叫出來用：

```python
a = 10
print(a)  # 顯示10

a = "apple"
print(a)  # 顯示apple
```

📌 `=` 是把右邊的東西放進左邊的變數中。

---

### ➕ 4. 運算子（做數學運算的符號）

| 運算 | 符號 | 範例               |
| ---- | ---- | ------------------ |
| 加法 | `+`  | `1 + 1` 結果是 2   |
| 減法 | `-`  | `3 - 1` 結果是 2   |
| 乘法 | `*`  | `2 * 3` 結果是 6   |
| 除法 | `/`  | `4 / 2` 結果是 2.0 |

📌 範例：

```python
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
```

---

### 🧠 5. 運算子的順序（誰先算？）

算數學時有先後順序喔，像這樣：

1. 括號 `()` 最先算
2. 次方 `**`
3. 除法 `/`
4. 乘法 `*`、取餘數 `%`
5. 加法 `+`、減法 `-`
6. 比較大小 `==`、`!=`、`>`, `<`, `>=`, `<=`
7. 邏輯判斷 `and`, `or`
8. 包含關係 `in`
9. 是不是同一個東西 `is`

---

### 💬 6. 字串的魔法（玩文字）

```python
print("apple" + "banana")  # 連起來變成 applebanana
print("apple" * 3)         # 重複三次變成 appleappleapple
```

---

### 🧩 7. 字串格式化（把變數放進文字裡）

你可以用變數做出像這樣的句子：

```python
name = "apple"
age = 10
print(f"name: {name}, age: {age}")
```

💡 `f""` 裡面加 `{}` 可以把變數放進句子中！

---

### 💡 小提醒

- 想要快速寫「註解」讓自己記錄的話，可以用 `#` 開頭。
- 用 `Ctrl + /` 可以快速加上或取消註解。




"""
    )

with st.expander("class2的筆記"):
    st.write(
        """
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

    """
    )
