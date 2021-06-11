class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q. {self.question_number}: {current_q.text} ('True' / 'False'): ")
        self.check_answer(user_ans, current_q.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self,user_answer,question_answer):
        if(user_answer.lower() == question_answer.lower()):
            print(f"You got it right!")
            self.score += 1
        else:
            print(f"Sorry, that's wrong.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")