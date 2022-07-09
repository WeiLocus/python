#類別class、物件object

#假設要定義一個手機

#1.claa是模板，定義手機資料形態，寫一個初始函式用“__init__”
#2.self是物件object的本身，
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os 
        self.number = number
        self.is_waterproof = is_waterproof
    def is_ios(self):   #宣告函式判斷作業系統是不是ios
        if self.os == "ios":
            return True
        else:
            return False
    def add(self,number1,number2):  #假設想要有相加的功能
        return number1+number2

#創建,並把手機的資料存在變數phone1
#可解釋成設定一台手機的作業系統為ios,型號是123,防水功能
phone1 = Phone("ios",123,True)  #phone1是一個物件
phone2 = Phone("andriod",456,False)

#要得到物件裡面的屬性用"phone1."
print(phone1.number)
print(phone2.os)
print(phone1.is_ios())

print(phone1.add(5,6))
