#建立計算機：加減乘除

#3個輸入：要運算的第一個數、第二個數、做什麼運算

#input會把所有的輸入當成字串，所以加float
num1=float(input("請輸入第一個數："))
op=input("請輸入運算符號：(+、-、*、/) ")
num2=float(input("請輸入第二個數："))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("不支援的運算")