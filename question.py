#定義資料形態question
#需要兩個屬性資訊
#第一是問題的描述description，第二是問題的答案answer

class Question:
    def __init__(self,description,answer):
        self.description = description
        self.answer = answer 


