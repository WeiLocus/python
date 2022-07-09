#猜數字遊戲

# secret_num=77
# guess=None #還沒定義，先輸入None

# while secret_num!= guess:
#     guess=int(input("請輸入數字："))
#     if guess > secret_num:
#         print("小一點")
#     elif guess < secret_num:
#         print("大一點")

# print("恭喜贏了")

#進階:只能猜三次
secret_num=77 #設定謎底
guess=None #還沒定義，先輸入None
guess_count=0 #存放的是猜測到第幾次，一開始是0
guess_limit=3 #存放的事最多能猜幾次，這裡定義3次 
out_of_limit=False #布林值

while secret_num!= guess and not(out_of_limit):
    guess_count +=1   #進入迴圈後先把猜測數加一
    if guess_count<= guess_limit:
        guess=int(input("請輸入數字："))
        if guess > secret_num:
            print("小一點")
        elif guess < secret_num:
            print("大一點")
    else:
        out_of_limit=True
if out_of_limit:
    print("抱歉，你輸了～")
else:
    print("恭喜贏了")

