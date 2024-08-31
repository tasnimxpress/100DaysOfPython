# create quizzbrain class
class QuizBrain:

    # define attribute
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {
            current_question.question}: (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right")
        else:
            print("That's wrong")
        print(f"Answer is {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}")
        print('\n')
