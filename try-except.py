# try-except例外處理
# 輸入文字後未轉型為整數，並且進行數學運算，發生發生例外(Exceptoion)錯誤時，使用try-except控制
# 當使用者輸入非數字的值，程式發生ValueError時，列印出提示文字
#當程式沒有發生異常被順利執行，在else中執行程式
#不管是否發生異常，都會執行finally中的程式，通常用在關閉資源的時候

try:
    num = input("請輸入一個數字")
    total = int(num) +1
    print(total)
except ValueError:
    print("請輸入數字")
except:
    print("發生錯誤")
else:
    print("成功執行")
finally:
    print("程式結束")


