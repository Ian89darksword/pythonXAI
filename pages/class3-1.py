# 連結使用if elif else的差別
# elif可以排除前面有判斷的條件 , 所以縮短判斷條件的複雜度 , 也節省了時間
# 但是如果是使用if來做獨立的判斷 , 則每個if都會被執行 , 所以可能會影響效率

# for 迴圈
# for 會搭配 in 來使用 , in 後面接一個有範圍的東西
# range(5) 會產生 0, 1, 2, 3, 4, 不包含5
# ｉ 是迴圈變數可自己取名
# 迴圈變數每回合會從範圍裏面取一個資料出來
for i in range(5):
    print(i)
    print("Hello ")
# range 可以設定起始值和結束值 , 但不包含結束值
# range(1, 5) 會產生 1, 2, 3, 4
for i in range(1, 5):
    print(i)

# range 可以設定起始值, 結束值, 和間格直 ,但不包含結束值
# range(1, 10, 2) 會產生 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)
