print([])  # 這行程式碼會印出一個空的列表，表示目前沒有任何內容。
print([1, 2, 3])  # 這行程式碼會印出一個列表，表示目前有三個元素。
print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 這行程式碼會印出一個列表，表示目前有十個元素。
print(
    1, 2, 3, ["a", "b", "c"]
)  # 這行程式碼會印出三個數字和一個列表，表示目前有三個數字和一個列表。
print(
    [1, True, "Hello", 3.14]
)  # 這行程式碼會印出一個列表，包含一個整數、一個布林值、一個字串和一個浮點數。

# list 讀取元素 index 從開始0
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 這行程式碼會印出列表的第一個元素，結果是1。
print(L[1])  # 這行程式碼會印出列表的第二個元素，結果是2。
print(L[2])  # 這行程式碼會印出列表的第三個元素，結果是3。
print(L[3])  # 這行程式碼會印出列表的第四個元素，結果是"a"。

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後 ,每次取2元素
print(
    L[::2]
)  # 這行程式碼會印出列表的第一個元素到最後一個元素，每次取2個元素，結果是[1, 3, "a", "c"]。
print(
    L[1::4]
)  # 這行程式碼會印出列表的第二個元素到最後一個元素，每次取4個元素，結果是[2, "b"]。
print(
    L[1:4:2]
)  # 這行程式碼會印出列表的第二個元素到最後一個元素，每次取2個元素，結果是[2, 3]。

# list 取長度 , 也就是list中有幾個元素 , 不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 這行程式碼會印出列表的長度，結果是6。

# list走訪
# 可以透過index的方式來找到list中的資料
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 1):
    print(L[i])  # 這行程式碼會印出列表中的每個元素，結果是1, 2, 3, "a", "b", "c"。

for i in L:
    print(i)  # 這行程式碼會印出列表中的每個元素，結果是1, 2, 3, "a", "b", "c"。

# call by value
a = 1
b = 2  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]  # a是一個列表
b = a  # b是a的引用，指向同一個列表
b[0] = 2
print(a, b)

a = [1, 2, 3]  # a是一個列表
b = a.copy()  # b是a的複製，指向不同的列表
b[0] = 2
print(a, b)

# list的append , 可以在list中加入新的元素
L = [1, 2, 3]
L.append(4)
print(L)

# list的extend , 可以在list中加入新的元素
L = [1, 2, 3]
L.extend([4, 5, 6])
print(L)

# list的insert , 可以在list中插入新的元素
L = [1, 2, 3]
L.insert(1, 4)
print(L)

# list的remove , 可以在list中刪除指定的元素
L = [1, 2, 3, 4, 5]
L.remove("a")  # 移除第一個"a"
# 代表的是刪除第一個元素
# 想要移除所有的"a"可以使用while迴圈
for i in L:
    if i == "a":
        L.remove(i)
# 2. 使用pop , 可以在list中刪除指定的元素
L = [1, 2, 3, 4, 5]
L.pop(1)  # 刪除第二個元素
print(L)

# sort : 將list中的元素排序 , 由小到大排列
L = [5, 2, 3, 1, 4]
L.sort()
print(L)
# open() 開始模式
# r - 讀取模式 , 檔案必須存在
# w - 寫入模式 , 檔案不存在則會建立
# a - 追加模式 , 檔案不存在則會建立
# r+ - 讀寫模式 , 檔案必須存在
# w+ - 寫入讀取模式 , 檔案不存在則會建立
# a+ - 追加讀取模式 , 檔案不存在則會建立

# 開啟檔案
# 絕對路徑 C:/Users/cloro/Desktop/pythonXAI/pages/class1-1.py
# 相對路徑 ./pages/class1-1.py
f = open("./pages/class1-1.py", "r", encoding="utf-8")
content = f.read()  # 讀取檔案內容
print(content)  # 印出檔案內容
f.close()  # 關閉檔案
##############################################################
with open("./pages/class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()  # 讀取檔案內容
    print(content)  # 印出檔案內容

# 字串的小工具 , 用來檢查字串是否為空
filename = "class1-1.md"
print(filename.endswith(".md"))  # True
filename2 = "notes.txt"
print(filename2.endswith(".md"))  # False
