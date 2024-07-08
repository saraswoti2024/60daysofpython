class questions:
    def __init__(self,text,answer) -> None:
        self.text = text
        self.answer = answer 

question_1 = questions("A slug's blood is green." ,"True")
user_answer=input(question_1.text + " :")