#bmi計算
max=24
min=18.5
def bmi(w,h):
    return round(w/h**2,2)
#print (bmi(57,1.6))

#class Profile
class Profile:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showProfile(self):
        print("Hello,I am %s , I am %s years old." % (self.name,self.age))
#pro=Profile("wei","32")
#pro.showProfile()
print(__name__)
