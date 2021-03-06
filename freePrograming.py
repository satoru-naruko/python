#!/usr/bin/env python3

print("free programing start")

# 関数定義
def printwrap(str):
    #インデントする
    print(str)

# 関数呼び出し
printwrap("function test")

str = "apple"

# if文
if str == "apple":
    print("str is apple")
elif str == "orange":
    print("str is orange")
else:
    print("str is else word")

month = 1
day = 2

if month == 1 and day == 2:
    print("month is 1")
elif month == 2 or day == 3:
    print("month is 2")
else:
    print("month is not 1")

# リスト定義(文字列)
fruits = ['apple', 'banana']

for fruit in fruits:
    print(fruit)

# リスト定義(文字列)
numbers = [4,6,7,89,4,21,1]

for num in numbers:
    print(num)

# 辞書型
dict_fruits = { 'banana':100, 'apple':'mac' }

for df in dict_fruits:
    #キーが表示される
    print(df)

for df in dict_fruits.values():
    #値が表示される
    print(df)

for key, val in dict_fruits.items():
    #key value で表示される
    print(key,val)