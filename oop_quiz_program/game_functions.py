from file_handling import FileHandler
from miscellaneous_functions import UICleaner
from prompt_functions import ContinueOrExit

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

class ShowFileContents:
    '''This is a code for show_contents()'''

    def __init__(self, file_path):
        self.file_path = file_path

    def show_contents(self):
        if FileHandler.file_empty_warning(self.file_path):
            return
        
        while True:
            UICleaner.clear_screen()

            try:
                with open(self.file_path, "r") as file_qna:
                    content = file_qna.read()
                    print(content)

                    action = ContinueOrExit("Press any key to continue/exit: ")

                    if action or action == "":
                        UICleaner.clear_screen()
                        return
            
            except FileNotFoundError:
                FileHandler.file_not_exists_warning()
                return

if __name__ == "__main__":
    # This will store the objects
    scores = ScoreKeeper([], 23, 1, "a")

    scores.score_counter()

    # This will sote the behavoir of the objects
    print(scores.score_counter())