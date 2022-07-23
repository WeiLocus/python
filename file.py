#檔案的讀取、寫入

#open("檔案路徑",mode="開啟模式")

#絕對路徑 ex:\Users\yangmbp\Documents\TEST.txt
#相對路徑 ex:以程式的位置做延伸：TEST.txt

'''
mode
r : 讀取檔案，如果沒有檔案會發生錯誤
w : 寫入內容，如果沒有檔案會自動產生
x : 建立檔案
a : 打開文件，並且在最後結尾繼續寫入資料
t : 一般文字檔，default模式使用t
b : 二進位模式，例如模式設定為rb，讀取圖片檔
'''
#try-except寫法
try:
    #file=open("/Users/yangmbp/Documents/TEST.txt",mode="r")  #開啟
    file=open("/Users/yangmbp/Documents/TEST.txt" , mode="w")
    file.write("text1,test2\n")
    file.write("a,b,c,d,e\n")
finally:
    file.close()    #記得把檔案關起來才不會佔用資源

#另一種打開檔案的方式with as（適用在有支援環境管理協定的物件），就不用每次都要寫file.close()
#print(file.read())  #印出讀取的內容用file.read
#print(file.readline())  #只讀取一行file.readline

#1
with open("TEST.txt",mode="r") as f:
    #使用函式read讀取資料，但會讀取所有文字
    print(f.read())
    #s=f.read()
    #print(s)

#2 for迴圈，把每一行都讀出來
with open("TEST.txt",mode="r") as f:
    for line in f:
        print("line content : "+line)

#3 readlines把每一行的資料放到列表裡面
with open("TEST.txt",mode="r") as f:
    print(f.readlines())

'''
#覆寫
#中文情形下若出現亂碼可以用enciding=utf-8
file=open("TEST.txt",mode="a",encoding="utf-8")
file.write(" Mr.white \n 你好")
file.close()
'''