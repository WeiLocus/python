#set集合，沒有順序

'''
聯集( | )
交集( & )
差集( - )
排除相同元素( ^ )
'''
'''
V={"a","e","u","i","o"}
F={"d","n","g","i","o"}

print(V|F)  #聯集
print(V&F)  #交集
print(V-F)  #差集
print(V^F)  #排除同元素
'''
#新增( add, update )
a={1,2,3,4}
a.add(5)       #新增單一個
print(a)
a.update({6,7})  #新增多個要用update，用大括弧包起來
print(a)
#刪除( remove, discard )
a.discard(1)
print(a)
#判斷元素是否在集合當中( in )
print(2 in a)
print(9 in a)