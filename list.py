#列表list、列表的用法
#要存放數字，字串，布林值都可以
scores=[90,70,60,50,80] #存放成績的列表
friends=["小黑","小黃","小綠"]
things=[90,"小黑",True]

#假設要改分數
scores[0]=30 #就可以把90分改成30分

print(scores)
print(friends)
print(things)
print(scores[0]) #代表取出第0位90
print(scores[-1]) #代表取出倒數第1位80
print(scores[0:2]) #代表取出第0位到第2位之前(不包含第2位)
print(scores[1:4]) #代表取出第1位到第4位之前(不包含第4位)
print(scores[1:]) #代表取出第1位70之後的所有數字
print(scores[:4]) #代表取出第4位80之前的所有數字

phrase="Hello Mr.White"
       #0123456789 
print(phrase[3])
print(phrase[0:5])
print(phrase[6:])

#函式

scores.sort() #sort 列表由大到小做排列
print(scores)

scores.extend(friends) #extend 延伸 把scores後面接上friends
print(scores)

scores.append(30) #append 在列表後面加上一個值
print(scores)

scores.insert(2,30) #insert 插入，兩個參數：要插入的位置，要插入的值
print(scores)

print(scores.index(50)) #index 回傳一個要找的值的位置
print(scores.count(50)) #count 回傳有幾個值

scores.remove(30) #remove 刪掉
print(scores)

scores.pop() #pop 移除列表最後一位
print(scores)

scores.reverse() #reverse 列表做反轉
print(scores)

scores.clear() #clear 清除，把列表全部清空
print(scores)


#練習2
#extend
list1=[3,1,5,4,2]
list2=[6,7]
list1.extend(list2)
print(list1)
#append (變成兩個list)
list3=[3,1,5,4,2]
list4=[6,7]
list3.append(list4)
print(list3)
#pop-將索引值為2的元素移除
list3.pop(2)
print(list3)
#remove移除某個特定的值-移除4
list3.remove(4)
print(list3)
#sort、reverse
list1.sort(reverse=True)
print(list1)
list1.reverse()
print(list1)
