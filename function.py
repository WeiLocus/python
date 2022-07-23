#函式 預先寫好的程式碼，用到的時候才會執行
#先定義才能呼叫
#只能大小寫、英文跟數字跟底線的組合，開頭不能是數字

#使用def關鍵字定義函式
'''
def 函式名稱(參數1, 參數2):
    函式中執行的程式碼
'''
#Python不支援重載(Overload)

#輸入參數預設值
'''
def 函式名稱(參數名稱=預設值):
    函式中執行的程式碼
'''

#輸入多個不確定數量的參數
'''
def 函式名稱(*參數):
    函式中執行的程式碼
'''

#定義函式
def hello(name,age):
    #print("hello"+ name + "你今年" + age +"歲")
    print("hello"+ name + "你今年" + str(age) +"歲")

#呼叫函式
#hello("小白","50")  #50是數字不能和字串做相加所以用雙引號改字串
hello("小白",50)

def add(num1,num2):
    #print(num1+num2)
    return num1+num2  
print(add(2,3))
#只要函式裡的程式碰到return,就會把retuen的值覆蓋掉原先的呼叫
#用retuen是因為把處理完的數值回傳後，後續還要做更多的運算跟處理

def add(num1,num2):
    print(num1+num2)
    return 10
value=add(3,4)
print(value)
#def的部分是定義函式，程式碼先看到呼叫value=add(3,4)
#往上找出print(num1+num2)，回傳7，再碰到return 10
#retuen會把value=add(3,4)覆蓋掉，value就會變成10

def add(num1,num2):
    print(num1+num2)

value=add(3,4)
print(value)
#如果沒有retuen，python會預設return None
#當函式在運行的時候碰到return，就會直接結束，不會再運行下面的程式