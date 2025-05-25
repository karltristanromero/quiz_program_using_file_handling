import random

from path_handling import PathHandler
from miscellaneous_functions import UICleaner
from file_handling import FileHandler
from prompt_functions import FileRetriever, PromptValidator, ContinueOrExit
from display_qna_functions import DisplayQnA
from display_correct_answers_function import DisplayAnswers
from check_function import AnswerValidator
from score_count_function import ScoreKeeper

class QuizInitiator(PathHandler):
    
    def __init__(self):
        UICleaner.clear_screen()
        UICleaner.ascii_art("Quiz Camp")

        ask_file = FileRetriever().get_file_name()
        super().__init__(file_name=ask_file)
    
    def start_quiz(self):
        full_path = self.get_file_path()
        file_path = FileHandler(full_path)

        if file_path.file_empty_warning():
            return True
        
        with open(full_path, "r") as questionnaire:
            list_of_qna = questionnaire.readlines()
            shuffled_list = random.sample(list_of_qna, len(list_of_qna))

            score = 0
            questionnaire_list = []
            for qna in shuffled_list:
                parts = qna.split(" | ")

                print(DisplayQnA(parts).display_questions())

                prompt_guess = "Enter your answer (a/b/c/d): "
                valid_guess = ["a", "b", "c", "d"]

                guess = PromptValidator(prompt_guess, valid_guess)
                guess = guess.get_input()

                point, corr_ans = AnswerValidator(guess, parts[6]).valid_ans()

                parts, score = ScoreKeeper(parts, score, point, corr_ans).score_counter()

                questionnaire_list.append(parts)

            UICleaner.clear_screen()
            UICleaner.ascii_art("Quiz Results")
            print(f"Your score is: {score}/{len(shuffled_list)}\n")
            DisplayAnswers(questionnaire_list).display_ans()

            response = ContinueOrExit().continue_or_exit()

            if response == "y":
                UICleaner.clear_screen()
                return True
            else:
                return False