import prompt_functions as prompting
import time
import random
from path_handling import PathHandler
from miscellaneous_functions import UICleaner
from file_handling import FileHandler
from score_count_function import ScoreKeeper
from read_file_function import ShowFileContents
from display_qna_functions import DisplayQnA
from check_function import AnswerValidator
from display_qna_functions import DisplayQnA
from display_correct_answers_function import DisplayAnswers

class QuizCreator(PathHandler):

    def __init__(self):
        UICleaner.clear_screen()
        UICleaner.ascii_art("Quiz Creator")

        ask_file = prompting.FileRetriever().get_file_name()
        super().__init__(file_name=ask_file)


    def write_to_file(self, questionnaire, qna_index, question, choices, ans):
        entry = f"{qna_index}. | {question} | {choices} | {ans}"
        questionnaire.write(entry + "\n")

    def create_quiz(self):
        file_path = self.get_file_path()

        with open(file_path, "a+") as questionnaire:
            questionnaire.seek(0)

            lines = questionnaire.readlines()

            if not lines:
                qna_index = 1  

            else:
                last_line = lines[-1]
                index_part = last_line.split(".")[0]

                qna_index = int(index_part) + 1

            while True:
                UICleaner.clear_screen()
                UICleaner.ascii_art("QnA Camp")

                question = prompting.QuestionEntry().get_question()
                choices = prompting.ChoicesEntry().get_choices()
                cor_answer = prompting.CorrAnsEntry().get_correct_answer()

                self.write_to_file(questionnaire, qna_index, question, choices, cor_answer)

                if prompting.ContinueOrExit().continue_or_exit() == "n":
                    print("Exiting the program...")
                    UICleaner.clear_screen()
                    return
                
                qna_index += 1



class QuizInitiator(PathHandler):
    
    def __init__(self):
        UICleaner.clear_screen()
        UICleaner.ascii_art("Quiz Camp")

        ask_file = prompting.FileRetriever().get_file_name()
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

                guess = prompting.PromptValidator(prompt_guess, valid_guess)
                guess = guess.get_input()

                point, corr_ans = AnswerValidator(guess, parts[6]).valid_ans()

                parts, score = ScoreKeeper(parts, score, point, corr_ans).score_counter()

                questionnaire_list.append(parts)

            UICleaner.clear_screen()
            UICleaner.ascii_art("Quiz Results")
            print(f"Your score is: {score}/{len(shuffled_list)}\n")
            DisplayAnswers(questionnaire_list).display_ans()

            response = prompting.ContinueOrExit().continue_or_exit()

            if response == "y":
                UICleaner.clear_screen()
                return True
            else:
                return False