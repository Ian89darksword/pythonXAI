# 比較運算子
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True

# 邏輯運算子
# and 運算子, 只要有一個值為False，結果就是False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# not 運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1. 括號 ()
# 2. 次方 **
# 3. 除法 /
# 4. 乘法 *、取餘數 %
# 5. 加法 +、減法 -
# 6. 比較大小 ==、!=、>、<、>=、<=
# 7. 邏輯判斷 and、or
# 8. 包含關係 in
# 9. 是不是同一個東西 is
# 字串運算
# 字串加法
print("apple" + "banana")  # 連起來變成 applebanana
print("apple" * 3)  # 重複三次變成 appleappleapple
password = input("請輸入密碼: ")  # 讀取使用者輸入的密碼
if password == "1234":
    print("密碼正確")
elif password == "12345":
    print("密碼是1234")
elif password == "123456":
    print("密碼是1234")
