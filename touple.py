#元祖touple 
#跟列表很像,但要用小括號

scores=(90,80,60,70,50)
print(scores[0])

print(len(scores)) #len 回傳有幾個值

#差別在元祖一旦創建就不能做新增或者修改
#為什麼需要元祖的資料形態：防止資料被修改
data=(123456,456789) #假設定義位置坐標

#練習-轉成list
t=(3,1,5,4,2)

list1=list(t)
print(type(list1))

#in
print(2 in t)

#count
list2=(3,3,5,4,2)
print(list2.count(3))
