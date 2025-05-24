class AnswerValidator:
    '''This is a code for validate_answer()'''
    
    def __init__(self, answer, correct_answer):
        self.answer = answer
        self.correct_answer = correct_answer

    def valid_ans(self):
        self.correct_answer = self.correct_answer.split()[0]

        if self.answer == self.correct_answer:
            return 1, self.correct_answer
        else:
            return 0, self.correct_answer