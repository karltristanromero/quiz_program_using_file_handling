from utils.miscellaneous_functions import UICleaner
from prompt_functions import PromptValidator
from display_qna_functions import DisplayQnA

class DisplayAnswers():
    
    def __init__(self, qna_list):
        self.qna_list = qna_list
    
    def display_ans(self):
        prompt_check = "Do you want to see the answers? (y/n): "
        valid_response = ["y", "n"]

        response = PromptValidator(prompt_check, valid_response).get_input()

        if response == "y":
            UICleaner.clear_screen()
            UICleaner.ascii_art("Answers\n")

            for number, qna in enumerate(self.qna_list):
                questions = DisplayQnA(qna).display_questions()
                display = f"{number+1}. {questions}{qna[7]}\n"
                print(display)    
                input("Press any key to continue...\n")
            return

        elif response == "n":
            return