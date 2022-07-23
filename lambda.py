#lambda 
'''
Python 中函式是物件，基本上是用def定義，但也可以用lambda運算式定義函式
#語法是 lambda input1, input2,... : expression
#lambda不能夠有區塊
'''
#用bmi改寫
bmi2= lambda w,h:w/h**2
print(bmi2(57,1.6))
'''
原始
def bmi(w,h):
   return w/h**2
print(bmi(57,1.6) )
'''
#條件判斷
#lambda x: 執行程式1 if 條件1 else 執行程式2 if 條件2 else 语執行程式3 
#範例：判斷BMI值小於18.5過輕，超過24過重，其他則是正常
bmicheck = lambda x:"體重過輕"  if x<18.5 else "體重過重" if x>=24 else "體重正常"
print(bmicheck(bmi2(70,1.65)))

#filter函式
'''
過濾序列，移除掉不符合條件的元素，並且返回一個迭代器
filter(函式, 序列) 
範例：將序列[8, 9, 10, 11, 12]過濾小於10的元素後回傳
'''
list1=[8,9,10,11,12]
f= filter(lambda x:x>=10,list1)
print(list(f))
#map函式
'''
依據所提供的函式對序列做映射
map(函式, 序列)
範例：將序列[1, 2, 3]各加上後回傳
'''
list2=[1,2,3]
m=map(lambda x:x+1,list2)
print(list(m))