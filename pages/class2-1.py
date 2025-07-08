print(len("apple"))  # len()函數可以取得字串的長度
print(len(","))  # len()函數可以計算字串的長度
# type()函數可以查看變數的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int("1234"))  # float轉int
print(float("1.234"))  # str轉float
print(float("1.234"))  # str轉float
print(str(1.234))  # float轉str
print(bool(1.234))  # float轉bool
# print(int(hello))  # 這會报錯, 因為字串不是數字

# input()函數使用
print("輸入開始")
# input()是一個函數，可以讀取輸入的內容
# ()裡面的文字是提示訊息會先顯示在終端機上
a = input("請輸入一個數字: ")  # 輸入數字
print("輸入結束")
print(int(a) + 10)
print(int(a))  # 證明透過input()輸入內容都是字串

# 計算圓面積
radius = float(input("請輸入半徑: "))  # 輸入半徑
area = 3.14 * radius * radius  # 計算圓面積
print(f"半徑: {radius} 圓面積: {area}")

# 計算圓周率
radius = float(input("請輸入半徑: "))  # 輸入半徑
circumference = 2 * 3.14 * radius  # 計算圓周率
print(f"半徑: {radius} 圓周率: {circumference}")
