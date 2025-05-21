

class AnswerValidator:
    '''This is a code for validate_answer()'''
    
    def __init__(self, answer, correct_answer):
        self.answer = answer
        self.correct_answer = correct_answer

    def validate_ans(self):
        self.correct_answer = self.correct_answer.split()[0]

        if self.answer == self.correct_answer:
            return 1, self.correct_answer
        else:
            return 0, self.correct_answer

class ScoreKeeper:
    '''This is a code for score_keeper()'''

    def __init__(self, qna_list, score, point, answer):
        self.qna_list = qna_list
        self.score = score
        self.point = point
        self.answer = answer
    
    def score_counter(self):
        if self.point == 1:
            self.score += self.point
            self.answer = f"Correct! It was {self.answer}"
        else:
            self.answer = f"Incorrect! It was {self.answer}"

        self.qna_list.append(self.answer)

        return self.qna_list, self.score

# This will store the objects
scores = ScoreKeeper([], 23, 1, "a")

# This will sote the behavoir of the objects
print(scores.score_counter())