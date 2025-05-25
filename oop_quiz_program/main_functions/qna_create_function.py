import game_functions.prompt_functions as prompting
from utils.path_handling import PathHandler
from utils.miscellaneous_functions import UICleaner

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