from miscellaneous_functions import UICleaner

class DisplayQnA:

    def __init__(self, qna):
        UICleaner.clear_screen()
        self.qna = qna

    def display_questions(self):
        question_str = self.qna[1] + "\n"

        for i in range(4):
            letter = chr(ord("a") + i)
            question_str += f"{letter}. {self.qna[i+2]}\n"

        return question_str