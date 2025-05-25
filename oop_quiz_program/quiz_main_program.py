import time
from main_functions.qna_create_function import QuizCreator
from main_functions.qna_start_function import QuizInitiator
from main_functions.qna_delete_function import QuizModifier
from game_functions.prompt_functions import PromptValidator, FileRetriever
from utils.miscellaneous_functions import UICleaner
from utils.file_handling import FileHandler
from utils.path_handling import PathHandler
from game_functions.read_file_function import ShowFileContents

class ProgramFunctions:

    @staticmethod
    def start_program():
        UICleaner.clear_screen()
        
        while True:
            UICleaner.ascii_art("Welcome!")
            print("""a. Create/Add QnA to a file
b. Start a quiz
c. Show contents of file
d. Delete a specific QnA in a file
e. Exit program\n""")
        
            ask = "What do you want to do? (a/b/c/d/e): "
            choices = ["a", "b", "c", "d", "e"]

            action = PromptValidator(ask, choices).get_input()

            if action == "a":
                obj_init = QuizCreator()
                obj_init.create_quiz()
            
            elif action == "b":
                txt_file = FileRetriever().get_file_name()
                file_path = PathHandler(txt_file).get_file_path()

                try:
                    if not QuizInitiator().start_quiz():
                        print("Exiting the program...")
                        time.sleep(3)
                        UICleaner.clear_screen()
                        return
                
                except FileNotFoundError:
                    FileHandler.file_empty_warning()
                    continue
                
            elif action == "c":
                txt_file = FileRetriever().get_file_name()
                file_path = PathHandler(txt_file).get_file_path()

                ShowFileContents(file_path).show_contents()

            elif action == "d":
                QuizModifier().delete_qna()
                
            elif action == "e":
                break


if __name__ == "__main__":
    ProgramFunctions.start_program()