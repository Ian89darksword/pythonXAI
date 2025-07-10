# # 算數指定暈算字
# a = 1
# a += 1  # a = a + 1
# print(a)
# a -= 1  # a = a - 1
# print(a)
# a *= 2  # a = a * 2
# print(a)
# a /= 2  # a = a / 2
# print(a)
# a //= 2  # a = a // 2
# print(a)
# a %= 2  # a = a % 2
# print(a)
# a **= 2  # a = a ** 2
# print(a)

# # 優先順序
# # 1.() 括號
# # 2.次方
# # 3.取余
# # 4.加減乘除
# # 5.運算子

# # while 迴圈
# # while 會搭配  會搭配一個條件來使用
# # 條件式為 True 或 False
# # True會一直執行
# # False會一直不執行
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# # break 可以跳出迴圈
# # 先判斷break屬於哪個迴圈 , 然後跳出回圈
# i = 0
# while i < 10:
#     print(i)
#     i += 1
#     if i == 5:
#         break


# for i in range(10):
#     print(i)
#     if i == 3:
#         break

# import random  # 匯入Random模組

# print(random.randrange(7))
# print(random.randint(1, 7))
# print(random.choice([1, 7, 2]))
# print(random.randint(1, 6))

# ans = random.randint(1, 10)  #
# while True:
#     num = int(input(f"請輸入1~10之間的數字: "))

#     if num < 0 or num > 10:
#         print("請輸入1~10之間的數字")
#     elif num > ans:
#         print("數字小於上一次輸入")
#     elif num < ans:
#         print("數字大於上一次輸入")
#     else:
#         print("數字相同")
#         break

# 字典(Dictionary) :用來儲存[key, value]的對應關係
d = {"apple": 20, "banana": 30, "orange": 25}
print(d)


# 建立字典: 使用{}  , key 和 value 冒號

d = {"apple": 20, "banana": 30, "orange": 25}
print(d["apple"])

# 從字典中取特定key對應的value
# 如果 key 不存在則會KeyError
d = {"apple": 20, "banana": 30, "orange": 25}
print(d["apple"])

# 遍歷字典
d = {"apple": 20, "banana": 30, "orange": 25}
# 法1- 直接遍歷
for k in d:
    print(k)
    print(d[k])

# 法2-明確使用keys
for k in d.keys():
    print(k)
    print(d[k])

# 法3- 使用values
for v in d.values():
    print(v)  # 直接印出value 不知key是甚麼

# 法4- 使用items
for k, v in d.items():
    print(f"{k}:{v}")

# 新增/修改字典
d = {"apple": 20, "banana": 30, "orange": 25}
d["apple"] = 10
print(d)
d["wax apple"] = 15
print(d)

# 刪除字典
d = {"apple": 20, "banana": 30, "orange": 25}
d.pop("apple")
popitem = d.pop("wax apple", "不存在這筆資料")
print(d)
print(popitem)
