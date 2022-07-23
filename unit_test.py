
def calculate(w,h):
    return round(w/h**2,2)
def cmToM(cm):
    return cm/100

if __name__ == "__main__":
    #先建立測試案例，建立一個類別，使它繼承於類別TestCase
    import unittest
    class BmiTestCase(unittest.TestCase):
        #接著類別中的函式命名開頭都要用test，自行定義測試名稱
        def test_calculate(self):
            result = calculate(57,1.6)   #函示裏面是實作測試的結果
            #呼叫bmi計算函式並且將它傳給變數result，下方則是判斷函式是否正確的關鍵
            #使用類別TestCase中的函式assertEqual，可以放置兩個參數，期望的結果和函式計算後的結果
            self.assertEqual(22.27,result)
        def cmToM(self):
            result = cmToM(160)   #函示裏面是實作測試的結果
            self.assertEqual(1.6,result)
#建立好TestCase後，把要測試的案例放到一個list中，直接在類別BmiTestCase中放入要測試的函式
    tests =[
        BmiTestCase("test_calculate"),
        BmiTestCase("cmToM")
    ]
#建立一個物件TestSuite，這個測試套件有一個函式addTests，透過函式將list放入套件中，list可以彈性增加
    suite = unittest.TestSuite()
    suite.addTests(tests)
#使用測試執行器，建立一個物件TestTestRunner
    runner = unittest.TextTestRunner()
    #使用物件中的函式run()進行測試，run函式中將套件suite放入參數中，
    runner.run(suite)