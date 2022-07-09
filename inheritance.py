#繼承

#從student.py import Student物件
from student import Student

#三個函式，印出名字、年紀、學校
student1=Student("小白",87,"小白國小")
student1.print_school()
student1.print_name()
student1.print_age()
