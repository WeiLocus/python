#模組module的使用
#可以給其他python的程式去做引入使用
'''
#python也有很多內建模組可查詢Python Module Index
#假設想import token模組
import token
#想知道內建模組token,py的檔案在哪裡可以先輸入import sys
import sys
print(sys.path)
'''
#pip 套件管理工具
#import numpy as np

#import bmi.py
from module_bmi import *
print(max)
print(bmi(57,1.6))
pro=Profile("wei","32")
pro.showProfile()
