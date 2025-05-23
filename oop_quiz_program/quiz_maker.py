from miscellaneous_functions import UICleaner
from file_handling import PathHandler
import prompt_functions as prompting

class QuizCreator(PathHandler):
    UICleaner.clear_screen()
    UICleaner.ascii_art("Quiz Creator")

    def __init__(self):
        super().__init__()

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
                
if __name__ == "__main__":
    quiz_creator = QuizCreator()
    quiz_creator.create_quiz()                
