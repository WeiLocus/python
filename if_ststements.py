#if判斷句

#1. 
#如果 我肚子餓
#     我就去吃飯
from ctypes.wintypes import FLOAT
from tkinter import N


hungry=False
if hungry:
    print("我就去吃飯")

#2. 
#如果 今天下雨
#     我就開車去上班
#否則
#     我就走路去上班
rainy=True
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")

#3.
#如果 你考100分
#   我就給你1000元
#或是如果 你考80分以上
#   我給你500元
#或是如果 你考60分以上
#   我給你100元
#否則
#   你給我300元  
score=100
if score==100: #==是指判斷左邊的值和右邊的值有沒有相等
    print("我就給你1000元")
elif score>=80:
    print("我給你500元")
elif score>=60:
    print("我給你100元")
else:
    print("你給我300元 ")

#4.
#如果 你考100分 且 今天下雨
#   我給你1000元
#否則 
#   你給我100元
score=90
rainy=True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")

#5.
#如果 你考100分 或 今天下雨
#   我給你1000元
#否則 
#   你給我100元
score=90
rainy=True
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")

#6.
#如果 你考100分 或 沒有下雨
#   我給你1000元
#否則 
#   你給我100元
score=100
rainy=True
if score==100 or not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")

#7.
#如果 你沒有考100分 或 沒有下雨
#   我給你1000元
#否則 
#   你給我100元
score=100
rainy=True
if score!=100 or not(rainy): #!= 不等於
    print("我給你1000元")
else:
    print("你給我100元")

#練習:輸入3個參數，回傳三個數字那個數字最大
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(10,3,5))

#練習:測量你的BMI值，確認你的體重是否正常？
'''
BMI公式：體重(公斤) / 身高(公尺)的平方
BMI值正常範圍：18.5到24之間
BMI值過重範圍：24到27之間
'''
h = float(input("請輸入你的身高"))
w = float(input("請輸入你的體重"))
bmi = w/(h**2)
print("您的BMI值為:" + str(bmi))

if bmi>18.5 and bmi<24:
    print("體重正常")
elif bmi>=24 and bmi<27:
    print("體重過重")
else:
    print("體重過輕")

#單位換算cm-inch
value=float(input("請輸入長度："))
unit=(input("請輸入單位："))
if unit == "in":
    print("%f in = %f cm" %(value,value*2.54))
elif unit =="cm":
    print("%f cm = %f in" %(value,value/2.54))
else:
    print("請輸入cm或in")

#費氏數列(Fibonacci)
#第0項是0，第1項是1
#第n項是前兩項(n-1), (n-2)的總和:0, 1, 1, 2, 3, 5, 8, 13
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))