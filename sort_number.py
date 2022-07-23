#氣泡排序法
'''
83,41,72,58,61,36
將序列由小排到大，序列中的數字兩兩比較，把小的數字往前面移動
'''

def bubble(list):
    for round in range(1,len(list)):          #range起始值是1,結束是序列的長度
        for i in range(0,len(list)-round):    #每一回合要比較的數量是序列的數量扣掉目前回合數
            if list[i]>list[i+1]:             #當目前索引值數字大於下一個索引值數字，就執行交換的動作
                list[i],list[i+1] = list[i+1],list[i]   #執行交換的動作，將右邊的值依序傳給左邊的變數
        print(str(round) + "round:" + str(list))        #印出每一回合的結果，列印list的方式用str轉為字串
    return


if __name__ == "__main__":
    list = [83,41,72,58,61,36]
    print("origin:" + str(list))
    bubble(list)
