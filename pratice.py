#問答程式
#引入資料形態Question

from question import Question
#from question import Question 是只引入question模組裡面的Question類別

#import question
#import 是引入question.py整個檔案的模組

test=[
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n"
]

#用定義的資料型態Question來表達問題
questions=[
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
]

#定義一個函式會幫我們跑測驗,要傳入一個列表，存放新的資料形態questions
#for 迴圈跑每一題
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer ==question.answer:
            score+=1
    print("你得到"+ str(score)+ "分，共"+str(len(questions))+"題")

run_test(questions)
