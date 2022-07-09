#建立一個基本計算機
#讀取用戶的兩個輸入：數字

# name=input("請輸入你的名字") #把輸入的名字變成變數name
# age=input("請輸入你的年紀")
# print("哈囉" + name + "你今年" + age + "歲")

number1=input("請輸入第一個數字")
number2=input("請輸入第二個數字")
print(number1+number2) #直接相加會變成字串
print(int(number1)+int(number2)) #int可以把字串變整數
print(float(number1)+float(number2)) #float可以把字串變有小數點的數