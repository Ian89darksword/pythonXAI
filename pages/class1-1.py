print("hello world")  # print是在終端機顯示文字的指令
# ctrl+ 可以快速住解/取消住解

# 基本型態
print(1)  # int這是整數,-1, 0, 1, 2, 3, 4, 5
print(1.0)  # float這是浮點數, 1.0, 2.0, 3.0, 4.0
print(1.23456789)  # float這是浮點數, 1.0, 2.0, 3.0, 4.0
print(1.23456789e-10)  # float這是浮點數, 1.0, 2.0, 3.0, 4.0
print("apple")  # str這是字串, "apple", "banana", "cherry"
print(True)  # bool這是布林值, True, False
print(False)  # bool這是布林值, True, False

# 變數
a = 10  #  新增一個儲存空間取名為a的變數, "="的功能是將右邊的值儲存到左邊的變數
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改成apple
print(a)  # 在終端機顯示a所存的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法

# 運算子的優先順序
# 1. () 括號
# 2. ** 次方
# 3. / 除法
# 4. + - 加減
# 5. * / %
# 6. + -
# 7. == != > >= < <=
# 8. and or
# 9. in
# 10. is

# 字串運算
print("apple" + "banana")  # 字串加法
print("apple" * 3)  # 字串


# 字串格式化
name = "apple"
age = 10
print(f"name: {name}, age: {age}")  # 字串格式化
