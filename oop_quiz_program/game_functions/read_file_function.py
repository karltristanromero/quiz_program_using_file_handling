from miscellaneous_functions import UICleaner
from file_handling import FileHandler
from prompt_functions import ContinueOrExit

class ShowFileContents:
    '''This is a code for show_contents()'''

    def __init__(self, file_path):
        self.file_path = file_path

    def show_contents(self):
        txt_file = FileHandler(self.file_path)

        if txt_file.file_empty_warning():
            return
        
        while True:
            UICleaner.clear_screen()

            try:
                with open(self.file_path, "r") as file_qna:
                    content = file_qna.read()
                    print(content)

                    action = ContinueOrExit()
                    action = action.continue_or_exit()

                    if action or action == "":
                        UICleaner.clear_screen()
                        return
            
            except FileNotFoundError:
                FileHandler.file_not_exists_warning()
                return
