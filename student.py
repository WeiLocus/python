#類別Student，三個屬性，名字、年紀、學校

# class Student:
#     def __init__(self,name,age,school):
#         self.name = name
#         self.age = age
#         self.school = school 

#     def print_name(self):
#         print(self.name)

#     def print_age(self):
#         print(self.age)

#     def print_school(self):
#         print(self.school)

#三個函式，印出名字、年紀、學校

#繼承，用student繼承person
#相當於person.py裡面的東西複製一份到student類別的最上面
#可以把重複的name和age刪掉,但初始函式不能刪掉,兩個是不一樣的
from person import Person 
class Student(Person):

#初始函式__init__(self,name,age,school)會覆蓋__init__(self,name,age)
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school 

    def print_school(self):
        print(self.school)