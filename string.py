#如何使用字串、字串的用法
#print("hello\nmr.white") #\n代表換行

#字串中想加雙引號"hello "mr.white"
#在雙引號前加\，告訴python斜線後面的雙引號不是字串結尾是字串的一部分 
#print("Hello\"Mr.white")

#字串相連用+號
#print("Hello"+"Mr.white")

#用變數方式
phrase ="Hello Mr.White"
print(phrase)

#函式 function
#lower 變成小寫：字串加上.lower()
#print(phrase.lower())
#upper 變成大寫：字串加上.upper()
#print(phrase.upper())
#isupper 判斷字串裡的字母是不是都是大寫true/false
#print(phrase.isupper())
#islower 判斷字串裡的字母是不是都是小寫true/false
#print(phrase.islower())

#函式可以連續做
#print(phrase.lower().islower()) #先變成小寫再判斷

#中括號用法，裡面要寫一個數字，數字代表字串的位置
#所有數字都是從0開始算
print(phrase[4]) #會回傳e

#.index 找到字串中的字在那個位置
print(phrase.index("t")) #如果想要找的字裡面有重複會先回傳最前面的

#.replace() 替換，第一個是想要被替換什麼，第二個是用什麼東西來替換
print(phrase.replace("M","m"))
