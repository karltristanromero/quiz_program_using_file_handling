import os
from prompt_functions import FileRetriever

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

class PathHandler:
    '''This is a code for create_dir(), get_file(), and rename_file()'''
    def __init__(self):
        self.file_name = FileRetriever("Enter a file name: ").get_file_name()

    @staticmethod
    def create_dir():
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        subdir_name = "questionnaire_inventory"

        dir_path = os.path.join(parent_dir, subdir_name)
        os.makedirs(dir_path, exist_ok=True)
        
        return dir_path
    
    def rename_file(self):
        file_name = self.file_name.strip().lower()
        file_name = file_name.replace(" ", "_")
        return file_name

    def get_file_path(self):
        file_path = self.rename_file()
        dir = PathHandler.create_dir()

        full_path = os.path.join(dir, file_path)
        
        if not full_path.endswith(".txt"):
            file_path = f"{full_path}.txt"

        return file_path

if __name__ == "__main__":
    # This will store the objects
    scores = ScoreKeeper([], 23, 1, "a")

    scores.score_counter()

    file_name = PathHandler()
    print(file_name.get_file_path())

    # This will sote the behavoir of the objects
    print(scores.score_counter())