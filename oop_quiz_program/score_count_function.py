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