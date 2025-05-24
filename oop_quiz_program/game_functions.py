from miscellaneous_functions import UICleaner
from prompt_functions import PromptValidator

class AnswerValidator:
    '''This is a code for validate_answer()'''
    
    def __init__(self, answer, correct_answer):
        self.answer = answer
        self.correct_answer = correct_answer

    def valid_ans(self):
        self.correct_answer = self.correct_answer.split()[0]

        if self.answer == self.correct_answer:
            return 1, self.correct_answer
        else:
            return 0, self.correct_answer

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