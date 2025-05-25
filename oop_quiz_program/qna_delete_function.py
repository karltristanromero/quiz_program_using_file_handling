import time
import prompt_functions as prompting
from miscellaneous_functions import UICleaner
from path_handling import PathHandler
from file_handling import FileHandler
from read_file_function import ShowFileContents

class QuizModifier(PathHandler):

    def __init__(self):
        UICleaner.clear_screen()
        UICleaner.ascii_art("QnA Deleter")

        ask_file = prompting.FileRetriever().get_file_name()
        super().__init__(file_name=ask_file)

    def delete_qna(self):
        full_path = self.get_file_path()
        file_path = FileHandler(full_path)

        if file_path.file_empty_warning():
            return
        
        with open(full_path, "r") as file_qna:
            lines = file_qna.readlines()

            ask = f"Want to check the file's contents first (y/n)? "
            valid_responses = ["y", "n"]

            ask_action = prompting.PromptValidator(ask, valid_responses)
            action = ask_action.get_input()

            if action == "y":
                show_obj = ShowFileContents(full_path)
                show_obj.show_contents()

            while True:
                ask = "Enter index of QnA for deletion. Type 'q' to exit: "
                req_index = prompting.PromptValidator(ask).get_input()
                req_index = req_index.lower()

                if req_index == "q":
                    print("Going back to menu...")
                    time.sleep(3)
                    UICleaner.clear_screen()
                    return
                
                updated_lines = []
                found = False

                for line in lines:
                    parts = line.split(".")[0]

                    if parts.strip() == req_index.strip():
                        found = True
                    else:
                        updated_lines.append(line)

                if found:
                    with open(full_path, "w") as updated_file:
                        updated_file.writelines(updated_lines)
                        print("The line has now been deleted.")
                        time.sleep(3)
                        UICleaner.clear_screen()
                        return
                else:
                    print("Index given does not exist.")