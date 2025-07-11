# len : 取得字典有多少組 key-value 配對
d = {"a": 1, "b": 2, "c": 3}
print(len(d))  # 3 字典有3 組 key-value 配對

# 檢查字典是否有某個 key
d = {"a": 1, "b": 2, "c": 3}
print("a" in d)  # True
print("d" in d)  # False

# 檢查list是否有某個元素
l = [1, 2, 3, 4, 5]
print(3 in l)  # True

# 比較複雜的dict
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1,2,3]
print(d["a"][0])  # 1
print(d["b"])
print(d["b"]["c"])  # 4

grade = {
    "小明": {"chinese": 90, "math": 100, "english": 80},
    "小红": {"chinese": 80, "math": 90, "english": 100},
    "小刚": {"chinese": 100, "math": 80, "english": 90},
}

# 取的小明的math分數
print(grade["小明"]["math"])  # 100

# 取的小紅的english分數
print(grade["小红"]["english"])  # 100

# 取的小刚的chinese分數
print(grade["小刚"]["chinese"])  # 100
