#類別Person，兩個屬性，一個是名字一個是年紀

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

#兩個函式，一個印出名字一個印出年紀